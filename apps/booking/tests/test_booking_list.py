from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.booking.enums import StatusChoice
from apps.booking.factories import BookingFactory
from apps.users.factories import UserFactory


class BookingListTestCase(APITestCase):
    def setUp(self) -> None:
        self.bookings = BookingFactory.create_batch(6)
        self.user = UserFactory.create()
        self.url = reverse("bookings-list")
        self.client.force_authenticate(self.user)

    def test_list_booking(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    def test_list_booking_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data.get("detail"), "Authentication credentials were not provided.")

    def test_list_booking_with_status_cancelled(self):
        BookingFactory.create_batch(3)
        BookingFactory.create_batch(2, status=StatusChoice.cancelled.value)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 9)
