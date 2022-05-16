from django.urls import path
from .views import all_profiles


urlpatterns = [
    path('', all_profiles, name='all_profiles'),
]