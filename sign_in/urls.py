from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
urlpatterns = [
	url(r'^$',views.home),
	url(r'^login/$', login, {'template_name': 'signup/login.html'}),
	url(r'^logout/$', logout, {'template_name': 'signup/logout.html'}),
	url(r'^register/$', views.register, name='register'),
]