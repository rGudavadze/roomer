import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.managers import BaseManager


class BaseModel(models.Model):
    id = models.UUIDField(
        _("id"), primary_key=True, default=uuid.uuid4, editable=False, help_text=_("ID")
    )
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True, help_text=_("Created At"))
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True, help_text=_("Updated At"))
    deleted = models.BooleanField(_("deleted"), default=False, help_text=_("Deleted"))

    objects = BaseManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()
