from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.rooms.views import InventoryViewSet, RoomViewSet

router = DefaultRouter()

router.register("inventories", InventoryViewSet, basename="inventories")
router.register("", RoomViewSet, basename="rooms")


urlpatterns = [
    path("", include(router.urls)),
]
