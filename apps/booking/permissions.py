from rest_framework.permissions import BasePermission


class IsBookingOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return not request.user.is_anonymous and request.user == obj.user
