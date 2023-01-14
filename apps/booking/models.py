from django.db import models
from django.db.models import CheckConstraint, F, Q
from django.utils.translation import gettext_lazy as _

from apps.base.models import BaseModel
from apps.booking.enums import StatusChoice
from apps.utils.validators import time_future_validation


class Booking(BaseModel):
    start_time = models.DateTimeField("start_time", validators=[time_future_validation])
    end_time = models.DateTimeField("end_time")
    status = models.CharField(
        "status",
        choices=StatusChoice.get_status(),
        max_length=128,
        default=StatusChoice.active.value,
        help_text=_("Status"),
    )
    user = models.ForeignKey(to="users.User", on_delete=models.DO_NOTHING, help_text=_("User"))
    room = models.ForeignKey(to="rooms.Room", on_delete=models.DO_NOTHING, help_text=_("Room"))

    class Meta:
        ordering = ["-start_time"]
        constraints = [
            CheckConstraint(check=Q(end_time__gte=F("start_time")), name="start_end_time_check"),
        ]

    def __str__(self):
        return f"Room:{self.room} is booked by user:{self.user}"
