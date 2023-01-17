from django.core.exceptions import ValidationError
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from apps.booking.enums import StatusChoice
from apps.rooms.models import Room
from apps.rooms.permissions import IsAdminOrReadOnly
from apps.rooms.serializers import RoomSerializer


class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["seats", "bookings__start_time", "bookings__end_time"]

    def get_queryset(self):
        attrs = self.request.GET
        start_time = attrs.get("bookings__start_time")
        end_time = attrs.get("bookings__end_time")

        if (start_time and not end_time) or (not start_time and end_time):
            raise ValidationError("start_time and end_time both or none")

        if start_time and end_time:
            return self._available_rooms(start_time, end_time)

        return self.queryset

    @staticmethod
    def _available_rooms(start_time, end_time):
        rooms = Room.objects.exclude(
            Q(bookings__start_time__gte=start_time, bookings__start_time__lt=end_time)
            | Q(bookings__end_time__gt=start_time, bookings__end_time__lte=end_time)
            | Q(bookings__start_time__lte=start_time, bookings__end_time__gte=end_time),
            bookings__status=StatusChoice.active.value,
        ).prefetch_related("bookings")

        return rooms
