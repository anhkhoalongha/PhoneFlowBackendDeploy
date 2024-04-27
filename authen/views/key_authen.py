from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import KeyActive
from rest_framework.permissions import AllowAny
import pytz


class KeyAuthentication(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        key = request.data.get('key')
        try:
            key_active = KeyActive.objects.get(key=key)
        except KeyActive.DoesNotExist:
            return Response({"message": "Invalid key"}, status=status.HTTP_401_UNAUTHORIZED)

        if key_active.is_login and key_active.expire and key_active.expire < datetime.now(tz=pytz.UTC):

            return Response({"message": "Key expired"}, status=status.HTTP_401_UNAUTHORIZED)
        is_login = key_active.is_login
        key_active.is_login = True
        key_active.save()
        return Response({"message": "Authentication successful", "is_login": is_login, "role": key_active.role, "key_active_id": key_active.id}, status=status.HTTP_200_OK)


class Logout(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')
        print(token)
        key_active = KeyActive.objects.get(key=token)
        key_active.is_login = False
        key_active.save()
        return Response(status=status.HTTP_200_OK)
