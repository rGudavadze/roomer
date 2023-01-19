from rest_framework import serializers

from apps.users.models import User
from apps.utils.logger import logger
from apps.utils.validators import PasswordMatchValidator


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
        validators = [PasswordMatchValidator()]

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
