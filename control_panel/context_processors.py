from api.models import Market

def user_market_data(request):
    if request.user.is_authenticated:
        try:
            market = Market.objects.get(owner=request.user)
            return {'market': market}
        except Market.DoesNotExist:
            return {}
    return {}
    