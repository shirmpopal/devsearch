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

@receiver(post_delete, sender=Profile)
def delete_user(instance, **kwargs):
  user = instance.user
  user.delete()