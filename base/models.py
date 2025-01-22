from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    image = models.FileField()
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField()
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    department = models.ManyToManyField('Department', blank=True)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    vendor = models.ForeignKey('Vendor', on_delete=models.SET_NULL, null=True)
    
class Sell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=300, null=True)

class Department(models.Model):
    name = models.CharField(max_length=100)
    floor = models.CharField(max_length=20)
    
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)