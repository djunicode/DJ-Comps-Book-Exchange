import django_filters
from .models import Book_List


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book_List
        fields = ['title', 'author', 'semester', 'subject', 'publication']
