from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.shared.factories import InventoryFactory


class BaseInventoryTestCase(APITestCase):
    def setUp(self) -> None:
        self.inventories = InventoryFactory.create_batch(5)
        self.current_inventory = self.inventories[0]
        self.url_list = reverse("inventories-list")
        self.url_detail = reverse("inventories-detail", kwargs={"pk": self.current_inventory.id})
        self.body = dict(name="TV")


class InventoryListRetrieveTestCase(BaseInventoryTestCase):
    def test_inventory_list(self):
        response = self.client.get(self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_inventory_retrieve(self):
        response = self.client.get(self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get("name"))
