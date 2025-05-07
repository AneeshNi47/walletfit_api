from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WalletUser, UserProfile


@receiver(post_save, sender=WalletUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # If profile info was already attached before saving, skip
        if not hasattr(instance, 'profile'):
            UserProfile.objects.create(user=instance)
