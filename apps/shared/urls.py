from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.shared.views import PhoneCodeView

router = DefaultRouter()

router.register("phone-codes", PhoneCodeView, basename="phone-codes")


urlpatterns = [
    path("", include(router.urls)),
]
