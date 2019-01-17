from django.conf.urls import url
from . import views

app_name = 'chat'

urlpatterns = [

    url(r'^chats/', views.list_chatrooms, name='user-list'),      # GET request for user with id
    url(r'^new_chat/', views.new_chatroom, name='new_chat'),
    url(r'^chat/(?P<id>\d+)/$', views.start_chat, name='chat'),
    url(r'^chat_json/(?P<id>\d+)/$', views.chat_json_resp, name='chat_json'),
]
