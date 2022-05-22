from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import UserProfile, BlogPost
from .serializers import BlogPostSerializer


@shared_task
def get_posts_and_send_email():

    all_users = User.objects.all()
    for user in all_users:  
        current_userprofile = user.userprofile

        current_userprofile_follows = UserProfile.objects.filter(
            followed_by=current_userprofile)

        cur_user_follow = User.objects.filter(
            userprofile__in=current_userprofile_follows)

        blog_posts = BlogPost.objects.filter(user__in=cur_user_follow).exclude(
            post_read_by=current_userprofile).exclude(user=user).order_by('-created_at')

        if len(blog_posts) >= 5:
            blog_posts = blog_posts[:5]

        serializer = BlogPostSerializer(blog_posts, many=True)

        send_mail(
            subject="Check out latest blogposts!",
            message=f"Greetings, {user.username}, check out 5 latest blogpost: \n {serializer.data}",
            from_email='djnagotestmailkek@gmail.com',
            recipient_list=[f'{user.email}'],)
