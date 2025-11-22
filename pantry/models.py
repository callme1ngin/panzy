from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)

class Icon(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='icons/')

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True, blank=True)

class Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    expiration_date = models.DateField(null=True, blank=True)
    barcode = models.CharField(max_length=100, blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ShoppingListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    checked = models.BooleanField(default=False)  # куплено/нет
    created_at = models.DateTimeField(auto_now_add=True)

class ProductHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    action = models.CharField(max_length=20)  # added, updated, removed, consumed и т.д.
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)
