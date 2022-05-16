from django.urls import path
from .views import profiles, userprofile


urlpatterns = [
    path('', profiles, name='profiles'),
    path('userprofile/<int:pk>', userprofile, name='userprofile'),
]