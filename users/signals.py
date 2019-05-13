# This file is created to handle automatic creation of profile for every user getting created with default profile pic
from django.db.models.signals import post_save                  # fired when post.save is envoked
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)               # this will just create an instance of profile
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)               # this will save the instance of profile
def save_profile(sender, instance, **kwargs):
    instance.profile.save()