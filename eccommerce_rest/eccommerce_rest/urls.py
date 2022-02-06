from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users.views import Login, Logout
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Documentacion de API",
        default_version='v0.1',
        description="Documentacion publica de API de ecomeerce",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jimenezcardenasad@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # rutasd sobre la documentacion de de las vistas
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # rutas de la app simplejwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # mis rutas
    path('users/', include('apps.users.api.routers')),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('products/', include('apps.products.api.routers')),
]

urlpatterns += [
    re_path(r'^media/(?P<patn>.*)$', serve, {
        'documento_root': settings.MEDIA_ROOT,
    }),
]
