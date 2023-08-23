from rest_framework import permissions

modify_delete_methods = ("PUT", "DELETE")

class ClientAccess(permissions.BasePermission):
    message = "Vous ne pouvez pas ajouter de client ou modifier, supprimer un client qui ne vous est pas affecté."
    
    def has_permission(self, request, view):
        if request.method == "POST" and request.user.role == 'SUPPORT':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        elif request.method in modify_delete_methods:
            if request.user == obj.commercial_contact:
                return True
            elif request.user.role == "MANAGEMENT":
                return True

class ContractAccess(permissions.BasePermission):
    message = "Vous ne pouvez pas consulter, ajouter, modifier ou supprimer de contrat."

    def has_permission(self, request, view):
        if request.method == "POST" and request.user.role == 'SUPPORT':
            return False
        elif request.user.role == 'MANAGEMENT':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        if request.method in modify_delete_methods:
            if request.user.role == 'SUPPORT':
                return False
            return True
            if request.user == obj.commercial_contact or request.user == obj.client.commercial_contact:
                return True
