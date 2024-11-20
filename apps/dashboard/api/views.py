from rest_framework import viewsets

from apps.dashboard.api.serializers import CategorySerializerClass
from apps.transactions.models import *


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializerClass
    queryset = Transaction.objects.all()
