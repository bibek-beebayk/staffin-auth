from requests import request
from rest_framework import serializers as rest_serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import User
from rest_framework.authtoken.models import Token
from libs.serializers import ImageKeySerializer
# from django.contrib.sites.models import Site

# current_site = Site.objects.get_current()
# domain = current_site.domain


class UserListSerializer(rest_serializers.ModelSerializer):
    profile_picture = ImageKeySerializer('listing')
    # print('Profile Picture: ', vars(profile_picture))

    class Meta:
        model = User
        fields = ['username', 'email', 'profile_picture']


class UserDetailsSerializer(rest_serializers.ModelSerializer):
    profile_picture = ImageKeySerializer('details')

    class Meta:
        model = User
        fields = ['username', 'email', 'last_login', 'profile_picture']


class TokenSerializer(rest_serializers.ModelSerializer):

    auth_token = rest_serializers.CharField(source='key')
    user_image = ImageKeySerializer('listing', source='user.profile_picture' ,read_only=True, use_url=True)
    class Meta:
        model = Token
        fields = ("auth_token",
                  "user_image",
                  )