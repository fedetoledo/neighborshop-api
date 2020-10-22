from api.models import ProductRating

def get_average_rating(ratings):
    size = ratings.count()
    total = 0
    try:
        for rating in ratings:
            total += rating.rating_value
        return total / size
    except ZeroDivisionError:
        return 0

def check_already_rated(user, product):
    try:
        ProductRating.objects.get(product__id=product, user__id=user)
        response = True
    except ProductRating.DoesNotExist:
        response = False
    return response
    