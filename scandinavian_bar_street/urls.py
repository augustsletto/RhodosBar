from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from bars.views import BarViewSet, PostViewSet
from events.views import EventViewSet
from chats.views import MessageViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configure Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Scandinavian Bar Street API",
        default_version='v1',
        description="API documentation for the Scandinavian Bar Street Social Media App",
        contact=openapi.Contact(email="contact@scandinavianbarstreet.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Configure REST framework router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bars', BarViewSet)
router.register(r'posts', PostViewSet)
router.register(r'events', EventViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
