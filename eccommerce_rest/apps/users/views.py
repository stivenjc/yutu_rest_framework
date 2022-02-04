from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.api.serializers import CustonTokenObtainParSerializer, CustomUseSerializer
from apps.users.models import User


class Login(TokenObtainPairView):
    serializer_class = CustonTokenObtainParSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password

        )
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUseSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'inicio de sesion exitoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'contraseña o nombre de usuario incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'contraseña o nombre de usuario incorrecta'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'sesion cerrada correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'no existe este eusuario.'}, status=status.HTTP_400_BAD_REQUEST)
