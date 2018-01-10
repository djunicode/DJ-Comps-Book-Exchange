from django.conf.urls import url
from book_listing.views import (BookCreateView,
                                BookUpdateView,
                                BookDeleteView,
                                search,
                                )

app_name = "book_listing"

urlpatterns = [
    url(r'^$', search, name="search"),
    url(r'^create/$', BookCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', BookUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', BookDeleteView.as_view(), name='delete')
]
