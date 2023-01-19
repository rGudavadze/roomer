from datetime import timedelta
from unittest.mock import patch

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from apps.booking.enums import StatusChoice
from apps.booking.factories import BookingFactory
from apps.rooms.factories import RoomFactory
from apps.users.factories import UserFactory
from apps.utils.logger import logger


class BookingCreateTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create()
        self.url = reverse("bookings-list")
        self.client.force_authenticate(self.user)

        self.room = RoomFactory.create()
        self.prev_booking = BookingFactory.create(room=self.room)
        self.body = dict(
            start_time=str(timezone.now() + timedelta(minutes=30)),
            end_time=str(timezone.now() + timedelta(minutes=210)),
            room=self.room.id,
        )

    @patch("apps.booking.signals.finish_booking")
    @patch.object(logger, "info")
    def test_booking_create_end_time_lt_prev_booking_start_time(self, mock_logger, mock_receiver):
        self.body.update({"end_time": str(timezone.now() + timedelta(minutes=60))})

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get("start_time"))

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_booking_create_end_time_eq_prev_booking_start_time(self, mock_logger, mock_receiver):
        self.body.update({"end_time": self.prev_booking.start_time})

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get("start_time"))

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_booking_create_end_time_in_range(self, mock_logger, mock_receiver):
        self.body.update({"start_time": str(timezone.now() + timedelta(minutes=120))})

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("detail")[0], "Room is not available at this time.")

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_booking_create_end_time_eq_prev_booking_end_time(self, mock_logger, mock_receiver):
        self.body.update({"end_time": self.prev_booking.end_time})

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("detail")[0], "Room is not available at this time.")

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_booking_create_start_time_and_end_time_out_of_range(self, mock_logger, mock_receiver):
        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("detail")[0], "Room is not available at this time.")

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_booking_create_start_time_eq_prev_booking_start_time_end_time_in_range(
        self, mock_logger, mock_receiver
    ):
        self.body.update(
            {
                "start_time": self.prev_booking.start_time,
                "end_time": str(timezone.now() + timedelta(minutes=120)),
            }
        )

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("detail")[0], "Room is not available at this time.")

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_booking_create_start_time_end_time_eq_prev_booking_start_time_end_time(
        self, mock_logger, mock_receiver
    ):
        self.body.update(
            {
                "start_time": self.prev_booking.start_time,
                "end_time": self.prev_booking.end_time,
            }
        )

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("detail")[0], "Room is not available at this time.")

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_booking_create_start_time_in_range_end_time_eq_prev_booking_end_time(
        self, mock_logger, mock_receiver
    ):
        self.body.update(
            {
                "start_time": str(timezone.now() + timedelta(minutes=120)),
                "end_time": self.prev_booking.end_time,
            }
        )

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("detail")[0], "Room is not available at this time.")

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_booking_create_start_time_eq_prev_booking_start_time_end_time_out_of_range(
        self, mock_logger, mock_receiver
    ):
        self.body.update(
            {
                "start_time": self.prev_booking.start_time,
            }
        )

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("detail")[0], "Room is not available at this time.")

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_booking_create_start_time_in_range_end_time_out_of_range(self, mock_logger, mock_receiver):
        self.body.update(
            {
                "start_time": str(timezone.now() + timedelta(minutes=120)),
            }
        )

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("detail")[0], "Room is not available at this time.")

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_booking_create_start_time_eq_prev_booking_end_time(self, mock_logger, mock_receiver):
        self.body.update(
            {
                "start_time": self.prev_booking.end_time,
            }
        )

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get("start_time"))

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_booking_create_start_time_gt_prev_booking_end_time(self, mock_logger, mock_receiver):
        self.body.update({"start_time": str(timezone.now() + timedelta(minutes=180))})

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get("start_time"))

    @patch("apps.booking.signals.finish_booking_signal")
    @patch.object(logger, "info")
    def test_create_cancelled_prev_booking(self, mock_logger, mock_receiver):
        self.prev_booking.status = StatusChoice.cancelled.value
        self.prev_booking.save()

        response = self.client.post(self.url, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get("start_time"))
