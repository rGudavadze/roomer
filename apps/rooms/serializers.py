from rest_framework import serializers

from apps.rooms.models import Inventory, Room


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["id", "name"]
        extra_kwargs = {"id": {"read_only": True}}


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name", "seats", "inventories"]
        extra_kwargs = {"id": {"read_only": True}}
