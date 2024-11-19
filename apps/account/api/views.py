from rest_framework.viewsets import ModelViewSet

from apps.account.models import CustomUser
from apps.account.serializers import CustomUserSerializer


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
