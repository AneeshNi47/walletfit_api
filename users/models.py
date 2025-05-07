from django.contrib.auth.models import AbstractUser
from django.db import models


class Household(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WalletUser(AbstractUser):
    household = models.ForeignKey(Household, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)

    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('member', 'Member'),
        ('viewer', 'Viewer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='member')


class UserProfile(models.Model):
    user = models.OneToOneField(WalletUser, on_delete=models.CASCADE, related_name='profile')

    # Personal Info
    phone_number = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    # Preferences
    currency = models.CharField(max_length=10, default='AED')
    theme = models.CharField(max_length=20, choices=[
        ('light', 'Light'),
        ('dark', 'Dark'),
    ], default='light')

    likes = models.TextField(blank=True)
    dislikes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
