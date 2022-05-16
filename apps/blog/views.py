from django.shortcuts import render
from .models import UserProfile
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.
def profiles(request):
    profiles = UserProfile.objects.exclude(user=request.user)
    context = {'profiles': profiles}
    return render(request, 'blog/profiles.html', context)


def userprofile(request, pk):
    profile = UserProfile.objects.get(pk=pk)
    if request.method == 'POST':
        current_user_profile = request.user.userprofile
        action = request.POST.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    context = {'profile': profile}
    return render(request, 'blog/userprofile.html', context)