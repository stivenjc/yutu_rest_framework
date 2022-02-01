# creando token
from datetime import datetime

from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api.serializers import UserTokenSerializer


# craando el loggin
class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    print('hasta aqui')
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'inicio de sexion Exitoso'
                    }, status=status.HTTP_201_CREATED)
                else:
                    # all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                    # if all_sessions.exists():
                    #     for session in all_sessions:
                    #         session_data = session.get_decoded()
                    #         if user.id == int(session_data.get('_auth_user_id')):
                    #             session.delete()
                    # token.delete()
                    # token = Token.objects.create(user=user)
                    # return Response({
                    #     'token': token.key,
                    #     'user': user_serializer.data,
                    #     'message': 'inicio de sexion Exitoso'
                    # }, status=status.HTTP_201_CREATED)
                    token.delete()
                    return Response({'error': 'ya se ah iniciado sesion con este usuario'})

            else:
                return Response({'error': 'este usuario no puede iniciar secion'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'nombre del usuario o contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje': 'hola desde response'}, status=status.HTTP_200_OK)


# creando el logout
class Logout(APIView):

    def get(self, request, *arg, **kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key=token).first()
            print(token)

            if token:
                user = token.user

                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()

                token.delete()

                session_message = 'sesion edel usuario eliminadas.'
                token_message = 'token eliminado.'
                return Response({'token_message': token_message, 'session_message': session_message},
                                status=status.HTTP_200_OK)
            return Response({'error': 'no se a encontrado un usuario con estascredenciales'},
                            status=status.HTTP_400_BAD_REQUEST)
        except:
            Response({'error': 'no se a encontrdo token en descripcion'}, status=status.HTTP_409_CONFLICT)
