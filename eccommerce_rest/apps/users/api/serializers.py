from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustonTokenObtainParSerializer(TokenObtainPairSerializer):
    pass


class CustomUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    ## en caso de actaulizar tod el con el mism serializador
    # def update(self, instance, validated_data):
    #     update_user = super().update(instance, validated_data)
    #     update_user.set_password(validated_data['password'])
    #     update_user.save()
    #     return update_user


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')

    # def update(self, instance, validated_data):
    #     update_user = super().update(instance, validated_data)
    #     update_user.set_password(validated_data['password'])
    #     update_user.save()
    #     return update_user


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        # recuerda estos datos   que estas aqui deves pintarlos en .values('id', 'username', 'email', 'name')despues de la c0onsulta
        return {
            'id': instance['id'],
            'name': instance['name'],
            'email': instance['email'],
            'username': instance['username']
        }

# @api_view(['GET', 'POST'])
# def user_api_view(request):
#     # List
#     if request.method == 'GET':
#         users = User.objects.all().values('id', 'username', 'email', 'password', 'name')
#         user_serializer = UserListSerializers(users, many=True)
#         return Response(user_serializer.data, status=status.HTTP_200_OK)
#
#     # create
#     elif request.method == 'POST':
#         user_serializer = UserSerializers(data=request.data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return Response(user_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail_api_view(request, pk=None):
#     # queryset
#     user = User.objects.filter(id=pk).first()
#
#     # validation
#     if user:
#
#         # retrieve
#         if request.method == 'GET':
#             user = User.objects.filter(id=pk).first()
#             user_serializer = UserSerializers(user)
#             return Response(user_serializer.data, status=status.HTTP_200_OK)
#
#         # update
#         elif request.method == 'PUT':
#             user = User.objects.filter(id=pk).first()
#             user_serializer = UserSerializers(user, data=request.data)
#             if user_serializer.is_valid():
#                 user_serializer.save()
#                 return Response(user_serializer.data, status=status.HTTP_200_OK)
#             return Response(user_serializer.errors)
#
#         # delete
#         elif request.method == 'DELETE':
#             user = User.objects.filter(id=pk).first()
#             user.delete()
#             return Response({'message': 'usuário eliminado'})
#
#     return Response({'messge': 'no se ha encontrado un usurio con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
