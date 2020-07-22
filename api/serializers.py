from rest_framework import serializers
from .models import User, Product, ProductImage, Market, Transaction, Favourites, Rated

class UserSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    class Meta:
        model = ProductImage
        fields = '__all__'

class MarketSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    class Meta:
        model = Market
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    images = serializers.SlugRelatedField(slug_field='remoteURL', many=True, read_only=True)
    market = serializers.SlugRelatedField(slug_field='name', many=False, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'categories', 'market', 'images']

class FavouritesSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    class Meta:
        model = Favourites
        fields = '__all__'

class RatedSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    class Meta:
        model = Rated
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    class Meta:
        model = Transaction
        fields = '__all__'