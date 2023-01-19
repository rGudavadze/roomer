from uuid import UUID

from celery import shared_task

from apps.booking.enums import StatusChoice
from apps.booking.models import Booking


@shared_task
def finish_booking(pk: UUID) -> None:
    """
    Celery task to change booking status after it's finished.
    :param pk: booking id
    :return:
    """

    instance = Booking.objects.filter(pk=pk).first()

    if instance and instance.status == StatusChoice.active.value:
        instance.status = StatusChoice.finished.value
        instance.save()
