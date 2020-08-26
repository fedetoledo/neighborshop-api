from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import User, Product, Market, Transaction, Rated, Favourites
from .serializers import (
    TransactionSerializer, RatedSerializer, FavouritesSerializer, 
    UserSerializer, ProductSerializer, MarketSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'uid'

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
        uid = self.request.query_params.get('uid', None)
        if uid is not None:
            queryset = queryset.filter(user__uid=uid)
        return queryset