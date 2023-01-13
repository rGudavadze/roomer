from rest_framework.viewsets import ModelViewSet

from apps.rooms.models import Inventory, Room
from apps.rooms.permissions import IsAdminOrReadOnly
from apps.rooms.serializers import InventorySerializer, RoomSerializer


class InventoryViewSet(ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
    permission_classes = (IsAdminOrReadOnly,)


class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
