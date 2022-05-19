from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserProfileSerializer, BlogPostSerializer
from .models import UserProfile, BlogPost

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # что будет добавленно в шифрованный токен
        data['username'] = self.user.username
        data['user_id'] = self.user.id
        data['profile_id'] = self.user.userprofile.id
        # ...

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/profiles',
        'api/dashboard',

        'api/userprofile/<id>',
        'api/userprofile/follow/<id>',
        'api/userprofile/unfollow/<id>',

        'api/userprofile/posts',
        'api/userprofile/posts/<id>',
        'api/userprofile/posts/<id>/like',
    ]
    return Response(routes)


@api_view(['GET'])
def getProfiles(request):
    profiles = UserProfile.objects.exclude(user = request.user)
    serializer = UserProfileSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getUserProfile(request, pk):
    userprofile = get_object_or_404(UserProfile, pk=pk)
    serializer = UserProfileSerializer(userprofile)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getUserFeed(request):
    blog_posts = BlogPost.objects.exclude(user = request.user)
    serializer = BlogPostSerializer(blog_posts, many=True)
    #posts_to_return = 
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def postMarkAsRead(request, pk):
    userprofile = request.user.userprofile
    blog_post = BlogPost.objects.get(pk=pk)
    blog_post.post_read_by.add(userprofile)
    blog_post.save()

    userprofile_serializer = UserProfileSerializer(userprofile, many=False)
    blogpost_serializer = BlogPostSerializer(blog_post, many=False)

    data_to_return = {
        'userprofile': userprofile_serializer.data,
        'blog_post': blogpost_serializer.data,
        'message': f'blog post id:{blog_post.id} was tagged as read by user id {userprofile.id}'
    }

    return Response(data_to_return, status=status.HTTP_200_OK)