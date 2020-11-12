from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if view.action == "list":
            return request.user.is_authenticated and request.user.is_superuser
        elif view.action in ['retrieve', 'update']:
            return True
    def has_object_permission(self, request, view, obj):
        return request.user and request.user == obj
