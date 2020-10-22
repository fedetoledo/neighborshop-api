from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import (
    User, Product, ProductImage, Market,
    Transaction, Favourites, ProductRating, Category
)
class ProductImageSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    class Meta:
        model = ProductImage
        fields = ['image']

    def to_representation(self, instance):
        url = instance.image.url
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url

class ProductMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ['name', 'phone_number']

class MarketSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    class Meta:
        model = Market
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    images = ProductImageSerializer(many=True, read_only=True)
    market = serializers.PrimaryKeyRelatedField(queryset=Market.objects.all())
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'categories', 'market', 'images']

class FavouritesSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    product = ProductSerializer(many=False, read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Favourites
        depth = 1
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['id','username','email','phone_number',
            'image','first_name','last_name', 'password', 'is_seller']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user


class ProductRatingSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    class Meta:
        model = ProductRating
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    id: serializers.ReadOnlyField()
    class Meta:
        model = Transaction
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
