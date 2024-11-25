from rest_framework import viewsets
from rest_framework import generics

from apps.account.api.serializers import UserSerializerClass
from apps.account.models import CustomUser


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializerClass


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializerClass



