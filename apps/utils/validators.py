from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class PasswordMatchValidator:
    def __call__(self, attrs, **kwargs):
        """
        Validation checks that password and password_confirm have the same value.
        """

        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")

        if password != password_confirm:
            raise serializers.ValidationError({"password_confirm": "Passwords are not matched!"})


class StartTimeValidator:
    def __call__(self, value, **kwargs):
        """
        Validation checks that the booking has not occurred in the past.
        """

        if value < timezone.now():
            raise ValidationError(_("You can not choose the past time."), code="past_time_err")
