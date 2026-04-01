from rest_framework.permissions import BasePermission, SAFE_METHODS

class RoleBasedPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        # Viewer → read only
        if user.role == 'viewer':
            return request.method in SAFE_METHODS

        # Analyst → read only
        if user.role == 'analyst':
            return request.method in SAFE_METHODS

        # Admin → full access
        if user.role == 'admin':
            return True

        return False