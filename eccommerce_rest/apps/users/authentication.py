from datetime import timedelta
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


# timpo de expicaion del token
class ExpiringTokenAuthentication(TokenAuthentication):

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=TOKEN_EXPIRED_AFTER_SECONDSS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            self.expired = True
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user=user)

        return token

    def authenticate_credentials(self, key):
        """
        return:
            * user         : instance user tha sended request to
            * token        : new token or actual token for username
            * message      : error messages
            * expired      : tru if token is alive for false if token is expired
        """
        user = None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            token = self.token_expire_handler(token)
            user = token.user
        except self.get_model().DoesNotExist:
            pass

        return user
