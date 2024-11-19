from rest_framework.viewsets import ModelViewSet


from apps.transactions.models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer