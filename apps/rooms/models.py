from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import BaseModel

# TODO: add Floor Model


class Room(BaseModel):
    name = models.CharField(_("name"), max_length=256, help_text=_("Room Name"))
    seats = models.IntegerField(
        _("seats"), validators=[MinValueValidator(1)], help_text=_("Number of seats")
    )
    inventories = models.ManyToManyField(to="app_helpers.Inventory", help_text=_("Inventories"))

    def __str__(self):
        return self.name
