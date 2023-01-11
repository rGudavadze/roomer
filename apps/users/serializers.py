from rest_framework import serializers

from apps.users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(help_text="Password Confirm Field")

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "password", "password_confirm"]
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
            raise serializers.ValidationError(
                {"password_confirm": "Passwords are not matched!"}
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        instance = User.objects.create_user(**validated_data)
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]
        extra_kwargs = {"id": {"read_only": True}}
