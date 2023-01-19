from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from apps.booking.models import Booking
from apps.booking.tasks import finish_booking


@receiver(post_save, sender=Booking)
def finish_booking_signal(sender, instance: Booking, created: bool, **kwargs) -> None:
    """
    Signal to execute finish_booking function as background task after several seconds.
    :param sender: Booking model
    :param instance: Booking instance
    :param created: bool
    :param kwargs:
    :return:
    """

    if not created:
        return

    timer = instance.end_time - timezone.now()
    finish_booking.apply_async((instance.id,), countdown=timer.seconds)
