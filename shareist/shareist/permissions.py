from rest_framework import permissions


class UserPermissions(permissions.BasePermission):
    """
    Handles permissions for users.  The basic rules are

     - owner may GET, PUT, POST, DELETE
     - nobody else can access
     """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            return False 