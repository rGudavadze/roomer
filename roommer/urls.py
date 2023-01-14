from django.contrib import admin
from django.urls import include, path

from roommer.spectacular import urlpatterns as swagger_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("apps.users.urls")),
    path("shared/", include("apps.shared.urls")),
    path("rooms/", include("apps.rooms.urls")),
    path("bookings/", include("apps.booking.urls")),
] + swagger_urls
