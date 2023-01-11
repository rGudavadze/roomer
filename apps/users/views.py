from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.users.serializers import RegisterSerializer, UserSerializer
from apps.users.models import User


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


class ListUserAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser, )


class DetailUserAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    http_method_names = ("get", "patch", "delete")

    def get_object(self):
        return self.request.user
