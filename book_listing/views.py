from django.shortcuts import render
from book_listing.models import Book_List
from book_listing.forms import Book_ListForm
from .filters import Book_ListFilter
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


def search(request):
    book_list = Book_List.objects.all()
    book_filter = Book_ListFilter(request.GET, queryset=book_list)
    return render(request, 'book_listing/search.html', {'filter': book_filter})


class BookCreateView(CreateView):
    form_class = Book_ListForm
    template_name = "book_listing/create_view.html"
    login_url = '/admin/'
    model = Book_List
    redirect_field_name = 'redirect_to'


class BookUpdateView(UpdateView):
    queryset = Book_List.objects.all()
    form_class = Book_ListForm
    model = Book_List
    template_name = "book_listing/update_view.html"


class BookDeleteView(DeleteView):
    model = Book_List
    template_name = "book_listing/delete_view.html"
    success_url = reverse_lazy("books:search")
