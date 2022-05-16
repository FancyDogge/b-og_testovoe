from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def all_profiles(request):
    all_profiles = UserProfile.objects.exclude(user=request.user)
    context = {'all_profiles': all_profiles}
    return render(request, 'blog/all_profiles.html', context)