from rest_framework import serializers
from apps.users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TestUserserializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):
        if 'adrian' in value:
            raise serializers.ValidationError('este nombre ya esta en uso, use otro')
        return value

    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError('tiene que indicar un correo')
        return value

    def validate(self, data):
        if data['name'] in data['email']:
            raise serializers.ValidationError('el email no puede contener el nombre')
        return data

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create(**validated_data)
