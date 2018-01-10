from . import views
from django.conf.urls import url

app_name = 'book_listing'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^book/add/$', views.BookCreate.as_view(), name='book-add'),
]
