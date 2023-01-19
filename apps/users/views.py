from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.users.models import User
from apps.users.serializers import RegisterSerializer, UserSerializer


class RegisterAPIView(CreateAPIView):
    """
    APIView to register users.
    """

    serializer_class = RegisterSerializer


class ListUserAPIView(ListAPIView):
    """
    APIView to get all users data.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class DetailUserAPIView(RetrieveUpdateDestroyAPIView):
    """
    APIView to retrieve, update or delete specific user by ID.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    http_method_names = ("get", "patch", "delete")

    def get_object(self):
        return self.request.user
