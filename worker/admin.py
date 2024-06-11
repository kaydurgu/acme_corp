from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
# Register your models here
# .
class ProfileAdmin(UserAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)