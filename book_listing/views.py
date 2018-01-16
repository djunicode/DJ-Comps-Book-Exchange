from django.shortcuts import render
from .models import Book_List
from .filters import BookFilter
from django.urls import reverse_lazy
from .forms import Book_ListForm
from django.views.generic import (UpdateView, DeleteView, CreateView)


def search(request):
    book_list = Book_List.objects.all()
    book_filtered = BookFilter(request.GET, queryset=book_list)
    return render(request, 'book_listing/search.html', {'book_filtered': book_filtered})


class BookUpdateView(UpdateView):
    queryset = Book_List.objects.all()
    form_class = Book_ListForm
    model = Book_List
    template_name = "book_listing/update_view.html"


class BookDeleteView(DeleteView):
    model = Book_List
    template_name = "book_listing/delete_view.html"
    success_url = reverse_lazy("books:search")


class BookCreate(CreateView):
    model = Book_List
    fields = ['uploaded_by', 'author', 'title', 'description', 'book_image', 'publication', 'semester', 'subject']


def lender_details(request):
    user = request.user
    return render(request, 'book_listing/details.html', {"user": user})
