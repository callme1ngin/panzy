from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProductViewSet, CategoryViewSet, LocationViewSet, ShoppingListViewSet, RegisterAnonymousUser

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'locations', LocationViewSet, basename='locations')
router.register(r'shopping-list', ShoppingListViewSet, basename='shopping-list')

urlpatterns = router.urls
urlpatterns += [
    path('register/', RegisterAnonymousUser.as_view(), name='register'),
]
