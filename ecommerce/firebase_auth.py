from django.contrib.auth.backends import ModelBackend
from api.models import User
from firebase import firebase
from django.core import serializers

class FirebaseBackend(ModelBackend):
    def authenticate(self, request, email, password):
        auth = firebase.auth()
        firebase_user = auth.sign_in_with_email_and_password(email, password)
        if firebase_user:
            print('firebase user ok!')
            uid = firebase_user['localId']
            user = User.objects.get(uid=uid)
            print(user)
            return user
        else:
            print('firebase auth failed')
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        