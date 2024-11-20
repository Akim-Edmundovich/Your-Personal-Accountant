from rest_framework import serializers

from apps.account.models import CustomUser


class UserSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super(UserSerializerClass, self).create(validated_data)
        user.set_password(user.password)
        user.save()
        return user
