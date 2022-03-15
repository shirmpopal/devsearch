from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    profile = Profile.objects.create(
      user = instance,
      username = instance.username,
      email = instance.email,
      name = instance.first_name,
    )
    subject = 'Welcome to devsearch'
    message = 'We are glad that you joind this website.'
    send_mail(
      subject,
      message,
      settings.EMAIL_HOST,
      [profile.email],
      fail_silently=False 
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