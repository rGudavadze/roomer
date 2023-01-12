from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import BaseModel
from apps.users.managers import CustomUserManager


class User(AbstractUser, BaseModel):
    email = models.CharField(
        _("email"),
        max_length=256,
        unique=True,
        help_text="Email Field",
        validators=[EmailValidator()],
    )
    username = models.CharField(
        max_length=256,
        help_text=_("Username Field"),
        null=True,
        blank=True,
        validators=[MinLengthValidator(6)],
    )
    first_name = models.CharField(
        _("first_name"),
        max_length=256,
        help_text="First Name Field",
    )
    last_name = models.CharField(
        _("last_name"),
        max_length=256,
        help_text="Last Name Field",
    )
    password = models.CharField(
        _("password"),
        max_length=512,
        help_text="Password Field",
        validators=[
            MinLengthValidator(6),
        ],
    )
    phone_code = models.ForeignKey(
        to="shared.PhoneCode",
        help_text=_("Phone Code"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    phone_number = models.CharField(
        _("phone_number"), max_length=256, help_text=_("Phone Number"), null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        app_label = "users"

    def __str__(self):
        return self.email
