from rest_framework import serializers
from htmx_test.models import Opera


class OperaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opera
        fields = '__all__'
