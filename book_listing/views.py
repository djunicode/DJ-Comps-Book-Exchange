from django.shortcuts import render
from book_listing.models import Book_List
from book_listing.forms import Book_ListForm
from .filters import Book_ListFilter
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


def search(request):
    book_list = Book_List.objects.all()
    book_filtered = Book_ListFilter(request.GET, queryset=book_list)
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
