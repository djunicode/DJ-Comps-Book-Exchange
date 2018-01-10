import django_filters
from .models import Book_List


class Book_ListFilter(django_filters.FilterSet):
    class Meta():
        model = Book_List
        fields = ['sem', 'subject', 'publication']
