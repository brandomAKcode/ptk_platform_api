from rest_framework.permissions import BasePermission

class IsAdminPTK(BasePermission):
    """
    Custom permission to allow object creation only if a specific condition is met.
    """

    def has_permission(self, request, view):
        # Implement your logic here to determine if the user can create
        # For example, check user role or specific data in the request
        user = request.user
        if user.role == 'ADM':  # Allow staff users to create
            return True
        return False