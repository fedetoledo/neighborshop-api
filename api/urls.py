from django.urls import path, include
from rest_framework import routers
from api.viewsets import (
	FavouritesViewSet, ProductRatingViewSet, TransactionViewSet, 
	UserViewSet, ProductViewSet, MarketViewSet, CategoryViewSet
)

from api.views.authenticacion import (
    CustomAuthtoken, 
    UpdateUserProfile,
    user_mobile_signup,
)
from api.views.favourites import (
    CheckFavourite,
    ToggleFavourite,
)

from api.views.products import ProductRatingAverage

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet, basename='products')
router.register('markets', MarketViewSet)
router.register('favourites', FavouritesViewSet)
router.register('rating', ProductRatingViewSet)
router.register('transactions', TransactionViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product/rating/<int:product>', ProductRatingAverage.as_view()),
    path('user/check-favourite', CheckFavourite.as_view()),
    path('user/toggle-favourite', ToggleFavourite.as_view()),
    path('user/update-profile/<int:id>', UpdateUserProfile.as_view()),
	path('user/token', CustomAuthtoken.as_view()),
    path('user/signup-mobile', user_mobile_signup),
    # path('user/upload-picture', user_upload_picture),
	
]
