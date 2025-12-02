from rest_framework import viewsets, permissions
from .models import Product, Category, Location, ShoppingListItem, Unit
from .serializers import (
    ProductSerializer, CategorySerializer, LocationSerializer, ShoppingListItemSerializer, UnitSerializer
)
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pantry.utils import create_default_locations
import uuid

class RegisterAnonymousUser(APIView):
    def post(self, request):
        uid = str(uuid.uuid4())
        user = User.objects.create_user(username=uid)
        create_default_locations()
        return Response({"uid": uid}, status=status.HTTP_201_CREATED)

# Доступ только для авторизованных пользователей, свои данные
class UserDataPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return hasattr(obj, 'user') and obj.user == request.user

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Category.objects.all()

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Location.objects.all()

class ShoppingListViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingListItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return ShoppingListItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)