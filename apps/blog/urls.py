from django import views
from django.urls import path, include
from .views import profiles, userprofile
from rest_framework import routers
from .views import UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)


urlpatterns = [
    path('', profiles, name='profiles'),
    path('root/', include(router.urls)),
    path('userprofile/<int:pk>', userprofile, name='userprofile'),
]