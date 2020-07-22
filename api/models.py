from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

class User(models.Model):
    uid = models.CharField(max_length=35, unique=True)
    fullName = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    userPicture = models.ImageField(upload_to=None, null=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=10)

    def __str__(self):
        return self.username
    

class Market(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=None, null=True)

# Create your models here.
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
    image = models.ImageField(upload_to='temp/')
    remoteURL = models.CharField(max_length=200, null=True)

class Favourites(models.Model):
    useruid = models.CharField(max_length=35)
    productID = models.IntegerField()

class Rated(models.Model):
    useruid = models.CharField(max_length=35)
    productID = models.IntegerField()

class Transaction(models.Model):
    useruid = models.CharField(max_length=35)
    marketID = models.IntegerField()
    productID = models.IntegerField()
    quantity = models.IntegerField()
    totalPrice = models.DecimalField(max_digits=6, decimal_places=2)
