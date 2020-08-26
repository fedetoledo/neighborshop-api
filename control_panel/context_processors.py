from api.models import Market
from django.contrib.auth.decorators import login_required

def market(request):
    if request.user.is_authenticated:
        try:
            market = Market.objects.get(owner=request.user)
        except Market.DoesNotExist:
            market = {}
        return {'market': market}
    return {}