from email.policy import default
import re
from tokenize import blank_re
import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from pyparsing import null_debug_action
from requests import request
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnDiscPlaceholderImage
from rest_framework.authtoken.models import Token as Auth_Token
from django.dispatch import receiver
from django.db.models import signals
from libs.serializers import ImageKeySerializer
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

# from djoser.views import UserViewSet

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    profile_picture = VersatileImageField(
        upload_to='user_images/',
        blank=True,
        null=True,
        # placeholder_image=OnDiscPlaceholderImage(
        #     path=os.path.join(
        #         '/home/bibek/Projects/Staffin/staffin/media/user_images/user_default.jpg',
        #     )
        # )
        # default = 'user_images/user_default.jpg'
    )

    # def get_token(self):
    #     return Token.objects.get(user=self)

    # my_token = property(get_token)

    SIZES = {
        'profile_picture' : {
            'full' : 'url',
            'listing': 'thumbnail__200x200',
            'details': 'crop__500x500'
        }
    }

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'profile_picture']


# class Token(Auth_Token):
#     @property
#     def get_image(self):
#         return self.user.profile_picture

#     user_image = get_image


# @receiver(signals.post_save, sender=Auth_Token)
# def create_token(sender, instance, **kwargs):
#     Token.objects.create(
#         key = instance.key,
#         user = instance.user,
#         user_image = instance.user.image
#     )



@receiver(signals.post_save, sender=User)
def warm_user_images(sender, instance, **kwargs):
    warmer = VersatileImageFieldWarmer(
        instance_or_queryset = instance,
        rendition_key_set = 'profile_picture',
        image_attr = 'profile_picture'
    )

    if instance.profile_picture:
        num_created, failed_to_create = warmer.warm()
        # print('\n\n', num_created, failed_to_create, '\n\n')

    else:
        return



