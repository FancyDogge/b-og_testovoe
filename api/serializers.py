from rest_framework import serializers
from .models import UserProfile, BlogPost
  
  
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'follows', 'posts_read']

    
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
    
    