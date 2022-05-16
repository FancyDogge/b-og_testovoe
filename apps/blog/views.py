from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def profiles(request):
    profiles = UserProfile.objects.exclude(user=request.user)
    context = {'profiles': profiles}
    return render(request, 'blog/profiles.html', context)


def userprofile(request, pk):
    profile = UserProfile.objects.get(pk=pk)
    context = {'profile': profile}
    return render(request, 'blog/userprofile.html', context)