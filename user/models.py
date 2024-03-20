from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_img = models.URLField(default="https://lh3.googleusercontent.com/a/ACg8ocIcAiQQxIElxmMp_3z5RAmSwyJGuK_mKmFu1JT0rFRANLQ=s360-c-no")    

    def __str__(self):
        return self.get_full_name()