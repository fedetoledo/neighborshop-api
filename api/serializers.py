from rest_framework import serializers
from .models import User, Product, ProductImage, Market, Transaction, Favourites, Rated

class ProductSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    images = serializers.SlugRelatedField(slug_field='remote_url', many=True, read_only=True)
    market = serializers.SlugRelatedField(slug_field='name', many=False, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'categories', 'market', 'images']

class FavouritesSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    product = ProductSerializer(many=False, read_only=True)
    #product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Favourites
        depth = 1
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    #favourite_products = serializers.SlugRelatedField(slug_field='product', many=True, read_only=True)
    favourite_products = FavouritesSerializer(many=True)
    class Meta:
        model = User
        fields = ['id','uid','username','email','phone_number','user_picture','first_name','last_name','favourite_products']

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