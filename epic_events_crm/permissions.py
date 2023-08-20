from rest_framework import permissions


class IsCommercialEmployeeOrReadOnly(permissions.BasePermission):
    message = "Seul le commercial affecté à ce client peut le mettre à jour."

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.role == 'SUPPORT':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.commercial_contact == request.user
