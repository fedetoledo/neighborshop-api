from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from api.utils.models import (
    market_dir_path,
    user_dir_path,
    product_dir_path,
    category_dir_path
)

DEFAULT_USER_IMAGE = 'default/no-user-image.jpg'
DEFAULT_PRODUCT_IMAGE = 'default/no-product-image.jpg'

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to=user_dir_path, blank=True,            default=DEFAULT_USER_IMAGE)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class Market(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    logo = models.ImageField(upload_to=market_dir_path, blank=True, default=DEFAULT_USER_IMAGE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = ArrayField(models.CharField(max_length=20))
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_dir_path, blank=True, default=DEFAULT_PRODUCT_IMAGE)

class Favourites(models.Model):
    user = models.ForeignKey(User, related_name='favourite_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

class Rated(models.Model):
    user = models.ForeignKey(User, related_name='rated_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating_value = models.FloatField()

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    market = models.IntegerField()
    product = models.IntegerField()
    product_qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to=category_dir_path)