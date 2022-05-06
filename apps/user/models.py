from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
from pyparsing import null_debug_action
from versatileimagefield.fields import VersatileImageField
# from djoser.views import UserViewSet

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    profile_picture = VersatileImageField(upload_to='user_images/', blank=True, null=True)

    SIZES = {
        'image': {'listing': 'thumbnail__250x250', 'details': 'crop__500x500'}
    }

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


