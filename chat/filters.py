import django_filters
from django.contrib.auth.models import User
from django import forms


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains', label='Whom you want to message?',
                                         widget=forms.TextInput(attrs={'name': 'receiver'}))

    class Meta:
        model = User
        fields = ['username']
