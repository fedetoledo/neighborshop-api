from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import User, Product, Market, Transaction, Rated, Favourites, Category
from .serializers import (
    TransactionSerializer, RatedSerializer, FavouritesSerializer, 
    UserSerializer, ProductSerializer, MarketSerializer, CategorySerializer
)

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    search_fields = ['name', 'categories']
    filter_backends = (filters.SearchFilter,)

class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class RatedViewSet(viewsets.ModelViewSet):
    queryset = Rated.objects.all()
    serializer_class = RatedSerializer

class FavouritesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Favourites.objects.all()
    serializer_class = FavouritesSerializer

    def get_queryset(self):
        queryset = Favourites.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(user__id=id)
        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer