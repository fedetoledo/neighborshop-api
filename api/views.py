from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core import serializers
from api.models import User, Favourites, Product
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import json
from control_panel.utils import save_profile_image_to_database

@csrf_exempt
@require_POST
def checkFavourite(request):
    if request.method == 'POST':
        print('CHECK FAVOURITE')
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        user_id = json_data['user']
        product_id = json_data['product']

        print('user: ', user_id)
        print('product: ', product_id)
        try:
            Favourites.objects.filter(product=product_id).get(user=user_id)
            response = {'isAlreadyFav': True}
        except Favourites.DoesNotExist:
            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)
            new_fav = Favourites(user=user, product=product)
            new_fav.save()
            response = {'isAlreadyFav': False}
        return JsonResponse(response)

@csrf_exempt
def userMobileSignup(request):
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

@csrf_exempt
@require_POST
def user_upload_picture(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        image_data = body['image_data']
        user_id = body['user_id']
        save_profile_image_to_database(image_data, user_id)
    return JsonResponse({'empty': 'empty'})


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
