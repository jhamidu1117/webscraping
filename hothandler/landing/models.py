from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import hashlib
from base64 import b64encode

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_id = models.CharField(max_length=25, blank=True)
    uname_id = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        email_id = hashlib.md5(bytes(instance.email, encoding='utf-8')).digest()
        email_id = b64encode(email_id).decode(encoding='utf-8')
        uname_id = hashlib.md5(bytes(instance.username, encoding='utf-8')).digest()
        uname_id = b64encode(uname_id).decode(encoding='utf-8')
        Profile.objects.create(user=instance, email_id=email_id, uname_id=uname_id)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
