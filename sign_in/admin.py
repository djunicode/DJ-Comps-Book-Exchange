"""UserProfile from signup.models for admin site."""
from django.contrib import admin
from signup.models import UserProfile
# Register your models here.
admin.site.register(UserProfile)
