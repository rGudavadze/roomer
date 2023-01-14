from django.urls import path

from apps.booking.views import BookingDetailsView, BookingListCreateView

urlpatterns = [
    path("", BookingListCreateView.as_view(), name="bookings-list"),
    path("<uuid:pk>", BookingDetailsView.as_view(), name="bookings-detail"),
]
