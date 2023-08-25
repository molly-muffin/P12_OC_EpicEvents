from rest_framework import permissions

modify_delete_methods = ("PUT", "DELETE")


class UserAccess(permissions.BasePermission):
    message = "Vous ne pouvez pas créer, modifier ou supprimer d'utilisateur si vous n'êtes pas dans l'équipe Gestion."

    def has_permission(self, request, view):
        if request.method == "POST" and request.user.role != 'MANAGEMENT':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        elif request.method in modify_delete_methods:
            if request.user.role != 'MANAGEMENT':
                return False
            return True


class ClientAccess(permissions.BasePermission):
    message = "Vous ne pouvez pas créer ou supprimer de client si vous n'êtes pas dans l'équipe Vente. Vous pouvez consulter tous les clients mais ne pouvez modifier que les clients qui vous sont affectés."

    def has_permission(self, request, view):
        if request.method == "POST":
            if request.user.role == 'SUPPORT' or request.user.role == 'MANAGEMENT':
                return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        elif request.method in modify_delete_methods:
            if request.user == obj.commercial_contact:
                return True


class ContractAccess(permissions.BasePermission):
    message = "Vous ne pouvez pas créer, modifier ou supprimer de contrat si vous n'êtes pas dans l'équipe Vente ou si le contrat ne vous est pas affecté. Vous pouvez seulement consulter les contrats."

    def has_permission(self, request, view):
        if request.method == "POST":
            if request.user.role == 'SUPPORT' or request.user.role == 'MANAGEMENT':
                return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        if request.method in modify_delete_methods:
            if request.user.role != 'COMMERCIAL':
                return False
            elif request.user != obj.commercial_contact or request.user != obj.client.commercial_contact:
                return False
            return True


class EventAccess(permissions.BasePermission):
    message = "Vous ne pouvez pas créer ou supprimer d'évènement si vous n'êtes pas dans l'équipe Vente. Vous pouvez consulter tous les évènements mais ne pouvez modifier que les évènements qui vous sont affectés."

    def has_permission(self, request, view):
        if request.method == "POST":
            if request.user.role == 'SUPPORT' or request.user.role == 'MANAGEMENT':
                return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True

        elif request.method in modify_delete_methods:
            if request.user == obj.support_contact or request.user == obj.contract.commercial_contact or request.user == obj.contract.client.commercial_contact:
                return True
