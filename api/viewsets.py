from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Product, Market, Transaction, ProductRating, Favourites, Category
from .serializers import (
    TransactionSerializer, ProductRatingSerializer, FavouritesSerializer, 
    UserSerializer, ProductSerializer, MarketSerializer, CategorySerializer
)
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser, IsSellerOrAdmin

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    search_fields = ['name', 'categories']
    filter_backends = (filters.SearchFilter,)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsSellerOrAdmin]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            permission_classes = [IsSellerOrAdmin, IsLoggedInUserOrAdmin]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ProductRatingViewSet(viewsets.ModelViewSet):
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer

    def get_queryset(self):
        queryset = ProductRating.objects.all()
        product_id = self.request.query_params.get('product', None)
        if product_id is not None:
            queryset = queryset.filter(product__id=product_id)
        total = 0
        for i in range(queryset.count()):
            total += queryset[i].rating_value
        return queryset

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