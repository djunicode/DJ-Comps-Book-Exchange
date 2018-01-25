from django import forms
from book_listing.models import Book_List


class Book_ListForm(forms.ModelForm):
    class Meta():
        model = Book_List
        exclude = ['user', 'date_created']
