from rest_framework import serializers
from .models import Product, Category, Location, ShoppingListItem, Unit, Icon

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = ['id', 'name', 'image']

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ["id", "name"]

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True, required=False
    )
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), source='location', write_only=True, required=False
    )
    class Meta:
        model = Product
        fields = [
            'id', 'user', 'name', 'category', 'category_id', 'location', 'location_id',
            'quantity', 'unit', 'expiration_date', 'barcode', 'note',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class ShoppingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = '__all__'
        read_only_fields = ['user']