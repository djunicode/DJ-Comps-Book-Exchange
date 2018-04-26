from django import forms
from .models import Profile
from django.contrib.auth.models import User


class Register(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        help_texts = {'username': None, 'password': None, 'email': None}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email address already registered.')
        return email


class ProfileInfo(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
