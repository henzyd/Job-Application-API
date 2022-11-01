from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class CustomUser(AbstractUser):
    email = models.EmailField(blank=False, unique=True)
#     first_name = models.CharField(blank=False, max_length=150)
#     last_name = models.CharField(blank=False, max_length=150)



# class UserProfile(models.Model):
#     owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     phone_number = models.BigIntegerField(unique=True, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.owner} Profile'



# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(owner=instance)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_profile(sender, instance, **kwargs):
#     instance.userprofile.save()



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)