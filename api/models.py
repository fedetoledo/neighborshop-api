from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    uid = models.CharField(max_length=35, unique=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=10)
    user_picture = models.ImageField(upload_to=None, null=True, blank=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class Market(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    logo = models.ImageField(upload_to=None, null=True)

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
    image = models.ImageField(upload_to='')
    remote_url = models.CharField(max_length=200, null=True)

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
