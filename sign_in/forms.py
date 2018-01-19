from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class Register(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, help_text='Required')
    first_name = forms.CharField(max_length=50, required=True, help_text='Required')
    last_name = forms.CharField(max_length=50, required=True, help_text='Required')
    email = forms.EmailField(max_length=250, required=True, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
