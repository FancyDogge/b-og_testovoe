from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import UserProfile, BlogPost


class UserProfileInline(admin.StackedInline):
    model = UserProfile

class BlogPostInline(admin.StackedInline):
    model = BlogPost


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [UserProfileInline, BlogPostInline]


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)