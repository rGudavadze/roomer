from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.booking.enums import StatusChoice
from apps.booking.factories import BookingFactory
from apps.users.factories import UserFactory


class BaseBookingDetailTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.booking = BookingFactory.create(user=self.user)
        self.url = reverse("bookings-detail", kwargs={"pk": self.booking.id})
        self.client.force_authenticate(self.user)


class BookingRetrieveTestCase(BaseBookingDetailTestCase):
    def test_booking_retrieve(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get("id"))

    def test_booking_retrieve_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data.get("detail"), "Authentication credentials were not provided.")

    def test_booking_retrieve_non_owner_user(self):
        user = UserFactory.create()
        self.booking.user = user
        self.booking.save()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response.data.get("detail"), "You do not have permission to perform this action."
        )


class BookingDestroyTestCase(BaseBookingDetailTestCase):
    def test_booking_destroy(self):
        response = self.client.delete(self.url)

        self.booking.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.booking.status, StatusChoice.cancelled.value)
