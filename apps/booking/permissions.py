from rest_framework.permissions import BasePermission


class IsBookingOwner(BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        """
        Checks if current user owns the booking object.
        :param request:
        :param view:
        :param obj:
        :return: bool
        """

        return not request.user.is_anonymous and request.user == obj.user
