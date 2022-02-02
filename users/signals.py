from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(
      user = instance,
      username = instance.username,
      email = instance.email,
      name = instance.first_name,
    )

@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
  profile = instance 
  user = profile.user
  
  if not created:
    user.first_name = profile.name
    user.username = profile.username
    user.email = profile.email
    user.save()

@receiver(post_delete, sender=Profile)
def delete_user(instance, **kwargs):
  user = instance.user
  user.delete()