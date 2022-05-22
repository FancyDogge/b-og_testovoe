from django.urls import path
from . import views
#from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    #path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.getRoutes, name='routes'),
    path('profiles/', views.getProfiles, name='profiles'),
    path('feed/', views.getUserFeed, name='feed'),

    path('userprofile/<int:pk>/', views.getUserProfile, name='userprofile'),
    path('userprofile/follow/<int:pk>/', views.postUserProfileFollow, name='follow'),
    path('userprofile/unfollow/<int:pk>/', views.postUserProfileUnfollow, name='unfollow'),
    path('post/mark_as_read/<int:pk>/', views.postMarkAsRead, name='mark_as_read'),
]