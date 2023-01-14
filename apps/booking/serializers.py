from rest_framework import serializers

from apps.booking.enums import StatusChoice
from apps.booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Booking
        fields = ["id", "start_time", "end_time", "status", "user", "room"]
        extra_kwargs = {
            "id": {"read_only": True},
            "status": {"read_only": True},
        }

    def validate(self, attrs):
        attrs = super().validate(attrs)

        if attrs.get("start_time") >= attrs.get("end_time"):
            raise serializers.ValidationError({"end_time": "End time must be greater than start time."})

        if not self._check_room_availability(attrs):
            raise serializers.ValidationError({"detail": "Room is not available at this time."})

        return attrs

    def _check_room_availability(self, attrs):
        room = attrs.get("room")
        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")

        bookings = self.Meta.model.objects.filter(
            room=room,
            status=StatusChoice.active.value,
            start_time__gte=start_time,
            end_time__lte=end_time,
        )

        return not bookings.exists()
