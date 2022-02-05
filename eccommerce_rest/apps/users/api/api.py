from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from apps.users.models import User
from apps.users.api.serializers import UserSerializers, UserListSerializers, UpdateUserSerializer


class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializers
    list_serializer_class = UserListSerializers
    queryset = None

    def get_object(self, pk):
        """
        #esto es para poder traer un solo objejo de la vase de datos no todos
        """
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.filter(is_active=True).values('id', 'username',
                                                                             'email', 'name')
        return self.queryset

    def list(self, request):
        users = self.get_queryset()
        user_serialzer = self.list_serializer_class(users, many=True)
        return Response(user_serialzer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'Usuario registrado Correctamente'}, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'hay errores en el registro',
            'error': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'usuario actualizado correctamente'}, status=status.HTTP_200_OK)
        return Response({'message': 'hay errore en la actualizacion',
                         'error': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = self.model.objects.filter(id=pk).update(is_active=False)
        if user == 1:
            return Response({'message': 'usuario eliminado corectamente'})
        return Response({'message': 'el usuario no existe'})
