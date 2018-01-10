from .models import BookList
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView


class IndexView(generic.ListView):
    template_name = 'book_listing/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return BookList.objects.all()


class BookCreate(CreateView):
    model = BookList
    fields = ['author', 'title', 'description', 'book_image', 'publication', 'semester', 'subject']
