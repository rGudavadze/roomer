from rest_framework import serializers

from apps.rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name", "seats", "inventories"]
        extra_kwargs = {"id": {"read_only": True}}
