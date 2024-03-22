from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=0)
    is_superuser = models.BooleanField(default=0)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    profile_img = models.URLField(default="https://fakeimg.pl/100x100")    

    def __str__(self):
        return self.username