from django.utils import timezone

from apps.utils.exceptions import (
    InvalidStartTimeException,
    PasswordMismatchException,
)


class PasswordMatchValidator:
    def __call__(self, attrs, **kwargs):
        """
        Validation checks that password and password_confirm have the same value.
        """

        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")

        if password != password_confirm:
            raise PasswordMismatchException()


class StartTimeValidator:
    def __call__(self, value, **kwargs):
        """
        Validation checks that the booking has not occurred in the past.
        """

        if value < timezone.now():
            raise InvalidStartTimeException()
