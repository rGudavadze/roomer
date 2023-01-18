from celery import shared_task

from apps.booking.enums import StatusChoice
from apps.booking.models import Booking


@shared_task
def finish_booking(pk):
    instance = Booking.objects.get(pk=pk)

    if instance.status == StatusChoice.active.value:
        instance.status = StatusChoice.finished.value
        instance.save()
