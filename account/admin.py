from django.contrib import admin
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()

# Register your models here.

class UserAdminDisplay(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

admin.site.register(User, UserAdminDisplay)



