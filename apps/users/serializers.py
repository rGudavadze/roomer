from rest_framework import serializers

from apps.users.models import User
from apps.utils.logger import logger


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(help_text="Password Confirm Field")

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "password_confirm",
            "first_name",
            "last_name",
            "phone_code",
            "phone_number",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "password_confirm": {"write_only": True},
        }

    def validate(self, attrs):
        attrs = super().validate(attrs)

        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")

        if password != password_confirm:
            raise serializers.ValidationError({"password_confirm": "Passwords are not matched!"})

        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        instance = User.objects.create_user(**validated_data)
        return instance

    def to_representation(self, instance):
        logger.info(f"User has been registered - ID: {instance.id}")
        return {"detail": f"{instance.email} you created your account."}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "phone_code", "phone_number"]
        extra_kwargs = {
            "id": {"read_only": True},
            "email": {"read_only": True},
        }
