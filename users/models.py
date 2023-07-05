from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    image_profile = models.ImageField()

    def __str__(self):
        return self.first_name