from django.conf.urls import url
from . import views

app_name = "book_listing"

urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^details/$', views.lender_details, name='details'),
    url(r'^add/$', views.BookCreate.as_view(), name='book-add'),
    url(r'^update/(?P<pk>\d+)/$', views.BookUpdateView.as_view(), name="update"),
    url(r'^delete/(?P<pk>\d+)/$', views.BookDeleteView.as_view(), name="delete"),
]
