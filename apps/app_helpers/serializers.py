from rest_framework import serializers

from apps.app_helpers.models import Inventory, PhoneCode


class PhoneCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneCode
        fields = ["id", "country", "code"]
        extra_kwargs = {"id": {"read_only": True}}


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ["id", "name"]
        extra_kwargs = {"id": {"read_only": True}}
