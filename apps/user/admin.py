from django.contrib import admin
from apps.user.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']

# @admin.register(Token)
# class TokenAdmin(admin.ModelAdmin):
#     list_display = [ 'token', 'user', 'user_image']
