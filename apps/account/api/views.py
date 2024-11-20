from rest_framework import viewsets

from apps.account.api.serializers import UserSerializerClass
from apps.account.models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializerClass
    queryset = CustomUser.objects.filter(is_active=True)