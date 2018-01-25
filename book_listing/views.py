from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book_List
from .filters import BookFilter
from django.urls import reverse_lazy
from .forms import Book_ListForm
from django.views.generic import (UpdateView, DeleteView, CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormUserNeededMixin, UserOwnerMixin


def search(request):
    book_list = Book_List.objects.all()
    book_filtered = BookFilter(request.GET, queryset=book_list)
    return render(request, 'book_listing/search.html', {'book_filtered': book_filtered})


class BookUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Book_List.objects.all()
    form_class = Book_ListForm
    model = Book_List
    template_name = "book_listing/update_view.html"


class BookDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = Book_List
    context_object_name = "item"
    template_name = "book_listing/delete_view.html"
    success_url = reverse_lazy("books:search")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, 'book_listing/not_allowed.html', {"txt": "You are not allowed to delete this."})


class BookCreate(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    model = Book_List
    form_class = Book_ListForm
    success_url = reverse_lazy("books:search")
