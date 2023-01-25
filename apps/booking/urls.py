from django.urls import path

from apps.booking.views import (
    BookingDetailsView,
    BookingListCreateView,
    FinishBookingAPIView,
)

urlpatterns = [
    path("", BookingListCreateView.as_view(), name="bookings-list"),
    path("<uuid:pk>/", BookingDetailsView.as_view(), name="bookings-detail"),
    path("finish/", FinishBookingAPIView.as_view(), name="booking-finish"),
]
