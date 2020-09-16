from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from api.models import User, Favourites, Product
import json

@csrf_exempt
@require_POST
def check_favourite(request):
    if request.method == 'POST':
        print(request.body)
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        user_id = json_data['user']
        product_id = json_data['product']
        try:
            fav = Favourites.objects.filter(product=product_id).get(user=user_id)
            response = {'isAlreadyFav': True}
        except Favourites.DoesNotExist:
            response = {'isAlreadyFav': False}
        return JsonResponse(response)

@csrf_exempt
def toggle_favourite(request):
    if request.method == 'POST':
        print(request.body)
        data = request.body.decode('utf-8')
        json_data = json.loads(data)
        user_id = json_data['user']
        product_id = json_data['product']

        try:
            fav = Favourites.objects.filter(product=product_id).get(user=user_id)
            fav.delete()
            response = {'result': 'favourite deleted'}
        except Favourites.DoesNotExist:
            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)
            new_fav = Favourites(user=user, product=product)
            new_fav.save()
            response = {'result': 'favourite added'}
        return JsonResponse(response)
