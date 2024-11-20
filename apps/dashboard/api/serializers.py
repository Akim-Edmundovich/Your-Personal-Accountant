from rest_framework import serializers

from apps.transactions.models import *


class CategorySerializerClass(serializers.ModelSerializer):
    id = serializers.CharField(source='name')

    class Meta:
        model = Category
        fields = '__all__'

