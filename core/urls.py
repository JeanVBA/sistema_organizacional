# core/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from organizacional.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'position', PositionViewSet)
router.register(r'branch', BranchViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'project', ProjectViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API Organizacional",
        default_version='v1',
        description="Documentação aberta da API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],  # <- aqui está a chave
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
