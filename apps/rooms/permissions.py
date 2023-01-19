from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        """
        Checks if request method is GET or current user is admin.
        :param request:
        :param view:
        :return:
        """

        safe_methods = ("GET",)
        if request.method in safe_methods:
            return True

        return request.user.is_superuser
