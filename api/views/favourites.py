from api.models import User, Favourites, Product
from rest_framework.response import Response
from rest_framework.views import APIView
import json

class CheckFavourite(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        user = data['user']
        product = data['product']
        try:
            Favourites.objects.get(product=product, user=user)
            response = {'isAlreadyFav': True}
        except Favourites.DoesNotExist:
            response = {'isAlreadyFav': False}
        return Response(response)

class ToggleFavourite(APIView):

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        user = data['user']
        product = data['product']
        try:
            Favourites.objects.get(product=product, user=user).delete()
            response = {'result': 'favourite deleted'}
        except Favourites.DoesNotExist:
            user = User.objects.get(id=user)
            product = Product.objects.get(id=product)
            Favourites.objects.create(user=user, product=product)
            response = {'result': 'favourite added'}
        return Response(response)


