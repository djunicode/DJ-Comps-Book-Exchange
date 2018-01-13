from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^update/(?P<pk>\d+)/$', views.BookUpdateView.as_view(), name="update"),
    url(r'^delete/(?P<pk>\d+)/$', views.BookDeleteView.as_view(), name="delete"),
]
