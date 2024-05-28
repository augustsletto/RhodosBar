from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from bars.views import BarViewSet, PostViewSet
from events.views import EventViewSet
from chats.views import MessageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bars', BarViewSet)
router.register(r'posts', PostViewSet)
router.register(r'events', EventViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
