from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializers, UserListSerializers


@api_view(['GET', 'POST'])
def user_api_view(request):
    # List
    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'email', 'password', 'name')
        user_serializer = UserListSerializers(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        user_serializer = UserSerializers(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    # queryset
    user = User.objects.filter(id=pk).first()

    # validation
    if user:

        # retrieve
        if request.method == 'GET':
            user = User.objects.filter(id=pk).first()
            user_serializer = UserSerializers(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            user = User.objects.filter(id=pk).first()
            user_serializer = UserSerializers(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors)

        # delete
        elif request.method == 'DELETE':
            user = User.objects.filter(id=pk).first()
            user.delete()
            return Response({'message': 'usuário eliminado'})

    return Response({'messge': 'no se ha encontrado un usurio con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
