from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.factories import UserFactory
from apps.utils.logger import logger


class AccountRegisterTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory.create(email="userexists@gmail.com")
        self.url = reverse("register-user")

        self.body = dict(
            email="email@gmail.com",
            password="123456",
            password_confirm="123456",
            first_name="firstname",
            last_name="lastname",
        )

    @patch.object(logger, "info")
    def test_register_correct(self, result_logger):
        response = self.client.post(
            self.url,
            data=self.body,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data.get("detail"), f"{self.body.get('email')} you created your account."
        )

    def test_register_existing_email(self):
        self.body.update({"email": "userexists@gmail.com"})
        response = self.client.post(
            self.url,
            data=self.body,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get("email")[0],
            "user with this email already exists.",
        )

    def test_register_unmatched_password(self):
        self.body.update({"password_confirm": "otherpassword"})
        response = self.client.post(
            self.url,
            data=self.body,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get("password_confirm")[0],
            "Passwords are not matched!",
        )

    def test_register_password_less_than_6(self):
        self.body.update({"password": "pasw", "password_confirm": "pasw"})
        response = self.client.post(
            self.url,
            data=self.body,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get("password")[0],
            "Ensure this field has at least 6 characters.",
        )

    def test_register_invalid_email(self):
        self.body.update({"email": "email"})
        response = self.client.post(
            self.url,
            data=self.body,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("email")[0], "Enter a valid email address.")
