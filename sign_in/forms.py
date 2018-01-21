from django import forms
from .models import Profile
from django.contrib.auth.models import User


class Register(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class ProfileInfo(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
