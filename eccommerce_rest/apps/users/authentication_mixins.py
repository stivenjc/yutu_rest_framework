from rest_framework import status, authentication, exceptions
from rest_framework.authentication import get_authorization_header
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from apps.users.authentication import ExpiringTokenAuthentication


class Authentication(authentication.BaseAuthentication):
    user = None

    def get_user(self, request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None

            token_expire = ExpiringTokenAuthentication()
            user = token_expire.authenticate_credentials(token)
            if user != None:
                self.user = user
                return user
        return None

    def authenticate(self, request):
        self.get_user(request)
        if self.user is None:
            raise exceptions.AuthenticationFailed('no se an encontrado las credenciales')

        return (self.user, None)
