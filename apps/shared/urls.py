from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.shared.views import InventoryViewSet, PhoneCodeView

router = DefaultRouter()

router.register("phone-codes", PhoneCodeView, basename="phone-codes")
router.register("inventories", InventoryViewSet, basename="inventories")


urlpatterns = [
    path("", include(router.urls)),
]
