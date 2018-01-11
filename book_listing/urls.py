from django.conf.urls import url
from book_listing.views import (BookUpdateView,
                                BookDeleteView,
                                search,
                                )

app_name = "book_listing"

urlpatterns = [
    url(r'^search/$', search, name="search"),
    url(r'^update/(?P<pk>\d+)/$', BookUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', BookDeleteView.as_view(), name='delete')
]
