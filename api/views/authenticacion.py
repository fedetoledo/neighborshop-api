from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import User
from django.contrib.auth.hashers import make_password

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import json

@csrf_exempt
def user_mobile_signup(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8') 
        json_data = json.loads(data)
        hashed_password = make_password(json_data['password'])
        new_user = {
            'first_name'    : json_data['firstName'],
            'last_name'     : json_data['lastName'],
            'username'      : json_data['username'],
            'email'         : json_data['email'],
            'password'      : hashed_password,
            'phone_number'  : '12345678',
        }
        user = User.objects.create(**new_user)
        Token.objects.create(user=user)

        return JsonResponse({
            'token': Token.objects.get(user=user).key,
            'id': user.id
        })
    return JsonResponse({'emtpy':'empty'})

class CustomAuthtoken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
        })
