from django.contrib import admin
from django.urls import path, include
from roommer.spectacular import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("apps.users.urls")),

] + swagger_urls
