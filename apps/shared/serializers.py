from rest_framework import serializers

from apps.shared.models import PhoneCode


class PhoneCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneCode
        fields = ["id", "country", "code"]
        extra_kwargs = {"id": {"read_only": True}}
