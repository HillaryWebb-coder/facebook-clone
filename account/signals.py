from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
# Custom Imports
from .models import Profile


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a new user profile if a new user registers successfully
    """
    if created:
        Profile.objects.create(user=instance)
