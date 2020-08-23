from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from api.models import Favourites
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.views.generic import CreateView
from api.models import User


@csrf_exempt
def checkFavourite(request):
	if request.method == 'POST':
		print(request.POST)
		user_id = request.POST.get('user')
		product_id = request.POST.get('product')
		try:
			fav = Favourites.objects.filter(product=product_id).get(user=user_id)
			response = {'isAlreadyFav': True}
		except Favourites.DoesNotExist:
			response = {'isAlreadyFav': False}
		return JsonResponse(response)
	return JsonResponse({})

@csrf_exempt
def userMobileSignup(request):
	if request.method == 'POST':
		print(request.POST)
	return JsonResponse({'emtpy':'empty'})
