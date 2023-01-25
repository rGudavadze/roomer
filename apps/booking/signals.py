from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from apps.booking.models import Booking
from apps.utils import cloud_task_client
from apps.utils.logger import logger


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
    logger.info(f"Room - {instance.room_id} has been reserved by user - {instance.user_id}")
    timer = instance.end_time - timezone.now()
    cloud_task_client.create_task(instance.id, timer)
