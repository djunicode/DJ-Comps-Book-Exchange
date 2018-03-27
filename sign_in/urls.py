from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<usernm>\w+)/$', views.profile_detail, name='profile-detail'),
    url(r'^log_in/$', views.log_in, name='log_in'),
]
