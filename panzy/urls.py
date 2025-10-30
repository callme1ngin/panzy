from django.urls import path, re_path, include
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# urlpatterns = [
#     path('api/', include('pantry.urls')),
#     path('api-auth/', include('rest_framework.urls')),  # для login/logout в браузере
# ]

schema_view = get_schema_view(
   openapi.Info(
      title="Panzy API",
      default_version='v1',
      description="Документация REST API для приложения Panzy",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include('pantry.urls')),
    # Swagger UI
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Redoc
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
]