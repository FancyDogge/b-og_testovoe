from django.urls import path, include
from .views import getRoutes, getProfiles, getUserProfile, getUserFeed, postMarkAsRead, MyTokenObtainPairView
#from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    #path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', getRoutes, name='routes'),
    path('profiles/', getProfiles, name='profiles'),
    path('userprofile/<int:pk>/', getUserProfile, name='userprofile'),
    path('feed/', getUserFeed, name='feed'),
    path('post/mark_as_read/<int:pk>', postMarkAsRead, name='mark_as_read'),
]