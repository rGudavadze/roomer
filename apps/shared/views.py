from rest_framework.viewsets import ModelViewSet

from apps.shared.models import PhoneCode
from apps.shared.serializers import PhoneCodeSerializer


class PhoneCodeView(ModelViewSet):
    serializer_class = PhoneCodeSerializer
    queryset = PhoneCode.objects.all()
    http_method_names = ("get", "post", "patch", "delete")
