from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from apps.booking.models import Booking
from apps.booking.tasks import finish_booking


@receiver(post_save, sender=Booking)
def finish_booking_signal(sender, instance, created, **kwargs):
    if not created:
        return

    timer = instance.end_time - timezone.now()
    finish_booking.apply_async((instance.id,), countdown=timer.seconds)
