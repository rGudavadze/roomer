from rest_framework.viewsets import ModelViewSet

from apps.app_helpers.models import Inventory, PhoneCode
from apps.app_helpers.serializers import (
    InventorySerializer,
    PhoneCodeSerializer,
)
from apps.utils.schemas import SharedSwaggerSchema


class PhoneCodeView(ModelViewSet):
    schema = SharedSwaggerSchema()
    serializer_class = PhoneCodeSerializer
    queryset = PhoneCode.objects.all()
    http_method_names = ("get",)


class InventoryViewSet(ModelViewSet):
    schema = SharedSwaggerSchema()
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    http_method_names = ("get",)
