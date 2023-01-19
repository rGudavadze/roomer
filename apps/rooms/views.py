from datetime import datetime

from django.core.exceptions import ValidationError
from django.db.models import Q, QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from apps.booking.enums import StatusChoice
from apps.booking.models import Booking
from apps.rooms.models import Room
from apps.rooms.permissions import IsAdminOrReadOnly
from apps.rooms.serializers import RoomSerializer


class RoomViewSet(ModelViewSet):
    """
    ViewSet to handle all request methods.
    """

    serializer_class = RoomSerializer
    queryset = Room.objects.all().prefetch_related("inventories")
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["bookings__end_time", "bookings__start_time", "seats"]

    def get_queryset(self):
        attrs = self.request.GET
        start_time = attrs.get("bookings__start_time")
        end_time = attrs.get("bookings__end_time")

        if (start_time and not end_time) or (not start_time and end_time):
            raise ValidationError("start_time and end_time both or none")

        if start_time and end_time:
            # TODO: remove query params from filter.
            return self._available_rooms(start_time, end_time)

        return self.queryset

    def _available_rooms(self, start_time: datetime, end_time: datetime) -> QuerySet:
        """
        Method to find all available rooms in specific range of time.
        :param start_time:
        :param end_time:
        :return:
        """

        reserved_room_ids = Booking.objects.filter(
            Q(start_time__gte=start_time, start_time__lt=end_time)
            | Q(end_time__gt=start_time, end_time__lte=end_time)
            | Q(start_time__lte=start_time, end_time__gte=end_time),
            status=StatusChoice.active.value,
        ).values_list("room_id", flat=True)

        rooms = self.queryset.exclude(id__in=set(reserved_room_ids))

        return rooms
