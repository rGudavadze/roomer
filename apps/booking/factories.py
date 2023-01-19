from datetime import timedelta

import factory
from django.db.models import signals
from django.utils import timezone
from factory.django import DjangoModelFactory

from apps.booking.enums import StatusChoice
from apps.rooms.factories import RoomFactory
from apps.users.factories import UserFactory


@factory.django.mute_signals(signals.post_save)
class BookingFactory(DjangoModelFactory):
    start_time = str(timezone.now() + timedelta(minutes=90))
    end_time = str(timezone.now() + timedelta(minutes=150))
    user = factory.SubFactory(UserFactory)
    room = factory.SubFactory(RoomFactory)
    status = StatusChoice.active.value

    class Meta:
        model = "booking.Booking"
