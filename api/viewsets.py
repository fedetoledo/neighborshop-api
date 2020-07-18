from rest_framework import viewsets, filters
from .models import User, Product, Business, Transaction, Rated, Favourites
from .serializers import TransactionSerializer, RatedSerializer, FavouritesSerializer, UserSerializer, ProductSerializer, BusinessSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    search_fields = ['name', 'categories']
    filter_backends = (filters.SearchFilter,)

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class TransactionViewSet(viewsets.ModelViewSet):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

class RatedViewSet(viewsets.ModelViewSet):
	queryset = Rated.objects.all()
	serializer_class = RatedSerializer

class FavouritesViewSet(viewsets.ModelViewSet):
	queryset = Favourites.objects.all()
	serializer_class = FavouritesSerializer