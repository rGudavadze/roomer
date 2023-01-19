from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.booking.enums import StatusChoice
from apps.booking.models import Booking
from apps.booking.permissions import IsBookingOwner
from apps.booking.serializers import BookingSerializer


class BookingListCreateView(ListCreateAPIView):
    """
    APIView to create booking or list all the bookings.
    """

    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return self.queryset.all()

        return self.queryset.filter(status=StatusChoice.active.value)


class BookingDetailsView(RetrieveDestroyAPIView):
    """
    APIView to get specific booking by id data or delete it.
    """

    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (IsBookingOwner,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoice.cancelled.value
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
