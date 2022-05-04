from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)

    USERNAME_FIELD = 'email'
    REQUIRED = []
