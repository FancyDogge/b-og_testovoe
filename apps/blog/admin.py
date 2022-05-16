from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import UserProfile, BlogPost


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [UserProfileInline]


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(BlogPost)