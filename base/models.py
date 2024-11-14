from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.FileField()
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

class Department(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField()
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    stock = models.IntegerField()
    
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    
class Sell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    customer_name = models.TextField(max_length=300, null=True)
