from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "admin"
        )


class IsDepartmentHead(permissions.BasePermission):
    """
    Allows access only to department head users.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "department_head"
        )


class IsProfessor(permissions.BasePermission):
    """
    Allows access only to professor users.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "professor"
        )


class IsAdminOrDepartmentHead(permissions.BasePermission):
    """
    Allows access to admin and department head users.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role in ["admin", "department_head"]
