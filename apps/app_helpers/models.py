from django.db import models
from django.utils.translation import gettext_lazy as _


class PhoneCode(models.Model):
    country = models.CharField(_("country"), max_length=255)
    code = models.CharField(_("code"), max_length=255)

    def __str__(self):
        return f"{self.country} {self.code}"

    class Meta:
        app_label = "app_helpers"
        verbose_name = "Phone Code"
        verbose_name_plural = "Phone Codes"
        ordering = ["country"]


class Inventory(models.Model):
    name = models.CharField(_("name"), max_length=256, help_text=_("Inventory Name"))

    def __str__(self):
        return self.name
