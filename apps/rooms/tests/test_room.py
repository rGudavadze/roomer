from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.rooms.factories import InventoryFactory, RoomFactory
from apps.rooms.models import Room
from apps.users.factories import UserFactory


class BaseRoomTestCase(APITestCase):
    def setUp(self) -> None:
        self.inventories = InventoryFactory.create_batch(3)
        self.rooms = RoomFactory.create_batch(5)
        self.current_room = self.rooms[0]
        self.url_list = reverse("rooms-list")
        self.url_detail = reverse("rooms-detail", kwargs={"pk": self.current_room.id})
        self.body = dict(
            name="Room #69",
            seats=4,
            inventories=[inventory.id for inventory in self.inventories],
        )


class RoomCreateTestCase(BaseRoomTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.admin_user = UserFactory.create(is_staff=True, is_superuser=True)
        self.client.force_authenticate(self.admin_user)

    def test_room_create_correct(self):
        response = self.client.post(self.url_list, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get("name"))

    def test_room_create_empty_name(self):
        self.body.update({"name": ""})
        response = self.client.post(self.url_list, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("name")[0], "This field may not be blank.")

    def test_room_create_without_name(self):
        del self.body["name"]
        response = self.client.post(self.url_list, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("name")[0], "This field is required.")

    def test_room_create_non_admin_user(self):
        user = UserFactory.create()
        self.client.force_authenticate(user)
        response = self.client.post(self.url_list, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response.data.get("detail"), "You do not have permission to perform this action."
        )

    def test_room_create_anonymous_user(self):
        self.client.logout()
        response = self.client.post(self.url_list, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data.get("detail"), "Authentication credentials were not provided.")


class RoomListRetrieveTestCase(BaseRoomTestCase):
    def test_room_list(self):
        response = self.client.get(self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_room_retrieve(self):
        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get("name"))


class RoomUpdateTestCase(BaseRoomTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.admin_user = UserFactory.create(is_staff=True, is_superuser=True)
        self.client.force_authenticate(self.admin_user)

    def test_room_update_correct(self):
        self.body.update({"name": "room#4"})
        response = self.client.put(self.url_detail, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "room#4")

    def test_room_update_without_name(self):
        del self.body["name"]
        response = self.client.put(self.url_detail, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data.get("name")[0], "This field is required.")

    def test_room_partial_update_correct(self):
        self.body.update({"name": "room#4"})
        response = self.client.patch(self.url_detail, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "room#4")

    def test_room_partial_update_empty_name(self):
        self.body.update({"name": ""})
        response = self.client.patch(self.url_detail, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("name")[0], "This field may not be blank.")

    def test_room_partial_update_without_name(self):
        del self.body["name"]
        response = self.client.patch(self.url_detail, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get("name"))

    def test_room_partial_update_string_seats(self):
        self.body.update({"seats": "string"})
        response = self.client.patch(self.url_detail, data=self.body)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("seats")[0], "A valid integer is required.")


class RoomDeleteTestCase(BaseRoomTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.admin_user = UserFactory.create(is_staff=True, is_superuser=True)
        self.client.force_authenticate(self.admin_user)

    def test_room_delete_correct(self):
        response = self.client.delete(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Room.objects.all()), 4)
