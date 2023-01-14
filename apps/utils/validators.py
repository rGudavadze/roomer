from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def time_future_validation(value):
    if value < timezone.now():
        raise ValidationError(_("You can not choose the past time."), code="past_time_err")
