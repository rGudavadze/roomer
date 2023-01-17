from rest_framework.viewsets import ModelViewSet

from apps.shared.models import Inventory, PhoneCode
from apps.shared.serializers import InventorySerializer, PhoneCodeSerializer
from apps.utils.schemas import SharedSwaggerSchema


class PhoneCodeView(ModelViewSet):
    serializer_class = PhoneCodeSerializer
    queryset = PhoneCode.objects.all()
    http_method_names = ("get",)


class InventoryViewSet(ModelViewSet):
    schema = SharedSwaggerSchema()
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    http_method_names = ("get",)
