from django.conf import settings
from django.contrib.auth.hashers import check_password
from models import DJ_user_client

class CustomUserAuth(object):

    def authenticate(self, username=None, password=None):
        try:
            user = DJ_user_client.objects.get(DJ_user=username)
            if user.check_password(password):
                return user
        except DJ_user_client.DoesNotExist:
            return None

    def get_user(self, DJ_id_client):
        try:
            user = DJ_user_client.objects.get(pk=DJ_id_client)
            if user.is_active:
                return user
            return None
        except DJ_user_client.DoesNotExist:
            return None