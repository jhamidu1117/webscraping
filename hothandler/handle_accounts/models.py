from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Platform(models.Model):
    user_account = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=1)
    platform_name = models.CharField(max_length=100, blank=True)
    platform_user_name = models.CharField(max_length=80, blank=True)
    platform_user_password = models.CharField(max_length=80, blank=True)
