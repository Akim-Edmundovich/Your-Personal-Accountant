from rest_framework import serializers
from apps.transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Transaction
        fields = '__all__'
