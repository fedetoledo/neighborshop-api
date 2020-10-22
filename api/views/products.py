import json
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import ProductRating

from api.utils.views import (
    get_average_rating,
    check_already_rated
)

class ProductRatingAverage(APIView):
    def post(self, request, product):
        user = json.loads(request.body)['user']
        ratings = ProductRating.objects.filter(product=product)
        average_rating = get_average_rating(ratings)
        is_rated = check_already_rated(user, product)
        return Response({
            "has_ratings": True if average_rating != 0 else False,
            "product": product,
            "is_rated": is_rated,
            "average_rating": average_rating
        })
        