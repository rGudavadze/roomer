from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.views import (
    DetailUserAPIView,
    ListUserAPIView,
    RegisterAPIView,
)

urlpatterns = [
    path("", ListUserAPIView.as_view(), name="list-user"),
    path("register/", RegisterAPIView.as_view(), name="register-user"),
    path("login/", TokenObtainPairView.as_view(), name="login-user"),
    path("me/", DetailUserAPIView.as_view(), name="detail-user"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
