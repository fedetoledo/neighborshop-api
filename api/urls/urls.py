from django.urls import path, include
from rest_framework import routers
from api.viewsets import FavouritesViewSet, RatedViewSet, TransactionViewSet, UserViewSet, ProductViewSet, BusinessViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet, basename='products')
router.register('business', BusinessViewSet)
router.register('favourites', FavouritesViewSet)
router.register('rated', RatedViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
