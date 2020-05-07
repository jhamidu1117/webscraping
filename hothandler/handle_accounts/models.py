from django.db import models
from handle_accounts.fields import EnField


# Create your models here.


class Platform(models.Model):
    platform_name = models.CharField(max_length=100)
    platform_user_name = EnField(max_length=64)
    platform_user_password = EnField(max_length=64)