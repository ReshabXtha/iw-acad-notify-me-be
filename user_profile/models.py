from django.contrib.auth import get_user_model
from django.db import models

from users.models import User

USER = get_user_model


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, unique=False, null=True, blank=True)
    last_name = models.CharField(max_length=50, unique=False, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to='media/user-images/', null=True, blank=True)
    # picture = models.FileField(upload_to='media/user-images/', null=True, blank=True)


    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)