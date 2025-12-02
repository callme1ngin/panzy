# pantry/admin.py
from django.contrib import admin
from .models import Product, Category, Location, ShoppingListItem

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(ShoppingListItem)
