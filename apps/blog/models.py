from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', symmetrical=False, related_name='followed_by', blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        #если создается юзер, создается и юзерпрофайл
        user_profile = UserProfile(user=instance)
        user_profile.save()
        #фолловим сами себя
        user_profile.follows.add(instance.userprofile)
        user_profile.save()
