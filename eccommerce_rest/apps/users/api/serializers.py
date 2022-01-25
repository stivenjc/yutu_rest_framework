from rest_framework import serializers
from apps.users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TestUserserializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
