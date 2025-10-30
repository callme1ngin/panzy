from django.contrib.auth.models import User
from rest_framework import authentication, exceptions

class UidAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        uid = request.headers.get('X-USER-UID')
        if not uid:
            return None  # нет заголовка — не аутентифицируем
        try:
            user = User.objects.get(username=uid)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')
        return (user, None)
