from django.urls import path, include
from rest_framework import routers
from api.viewsets import (
	FavouritesViewSet, RatedViewSet, TransactionViewSet, 
	UserViewSet, ProductViewSet, MarketViewSet, CategoryViewSet
)
from api.views import checkFavourite, userMobileSignup

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet, basename='products')
router.register('markets', MarketViewSet)
router.register('favourites', FavouritesViewSet)
router.register('rated', RatedViewSet)
router.register('transactions', TransactionViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('check-favourite', checkFavourite),
    path('signup-mobile', userMobileSignup),
]
