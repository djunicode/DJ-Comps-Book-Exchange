from django.conf.urls import url
from . import views

app_name = 'chat'

urlpatterns = [

    url('message/(?P<user_id>\d+)', views.messageview, name='message'),
    url('users/', views.user_list, name='user-list'),      # GET request for user with id

]
