from django.shortcuts import render, redirect
from .models import ChatRoom, Message
from django.contrib.auth.models import User
from itertools import chain
from .filters import UserFilter
from django.http import HttpResponse, JsonResponse
from django.core import serializers


def new_chatroom(request):
    user_list = User.objects.all()
    user_filtered = UserFilter(request.GET, queryset=user_list)
    if request.GET:
        user_filtered = UserFilter(request.GET, queryset=user_list)
    if request.user.is_authenticated():
        if request.POST:
            sender = request.user
            receiver = request.POST.get("user")
            print(receiver)
            user_receiver = User.objects.all().filter(username=receiver)
            chat_rooms_1 = ChatRoom.objects.all().filter(sender=sender, receiver=user_receiver)
            chat_rooms_2 = ChatRoom.objects.all().filter(sender=user_receiver, receiver=sender)
            if (len(user_receiver) != 0):
                if (len(chat_rooms_1) == 0 and len(chat_rooms_2) == 0):
                    chat_room = ChatRoom.objects.create(
                        sender=sender,
                        receiver=user_receiver[0]
                    )
                    chat_room.save()
                    return redirect("chat:user-list")
                else:
                    return render(request, 'chat/users.html', {'user_filtered': user_filtered,
                                                               'no_user': "Chat already exists"})
            else:
                return render(request, 'chat/users.html', {'user_filtered': user_filtered, 'no_user': "No such user"})
        else:
            return render(request, 'chat/users.html', {'user_filtered': user_filtered, 'no_user': ""})
    else:
        return redirect("login")


def list_chatrooms(request):
    if request.user.is_authenticated():
            chat_rooms_sender = ChatRoom.objects.all().filter(sender=request.user)
            chat_rooms_receiver = ChatRoom.objects.all().filter(receiver=request.user)
            return render(request, 'chat/chat_rooms.html', {'chat_rooms_sender': chat_rooms_sender,
                                                            'chat_rooms_receiver': chat_rooms_receiver})
    else:
        return redirect("login")


def start_chat(request, id):
    if request.user.is_authenticated():
        chat_room = ChatRoom.objects.all().filter(id=id)
        if chat_room[0].sender == request.user:
            receiver = chat_room[0].receiver
        else:
            receiver = chat_room[0].sender
        if request.POST and request.is_ajax():
            message = request.POST.get("message")
            print(message)
            if message != "" and len(chat_room) != 0:
                m = Message.objects.create(
                    conversation=chat_room[0],
                    message=message,
                    sender1=request.user,
                    receiver1=receiver
                )
                m.save()
                return redirect("/chat/chat/" + id)
            else:
                return render(request, 'chat/chat.html', {'chat_detail': chat_room[0],
                                                          'no_message': 'Please type something!', 'chat_id': id})
        else:
            m = Message.objects.all().filter(conversation=chat_room[0])
            return render(request, 'chat/chat.html', {'chat_detail': chat_room[0],
                                                      'no_message': '', 'messages': m, 'chat_id': id})
    else:
        return redirect('login')


def chat_json_resp(request, id):
    if request.user.is_authenticated():
        chat_room = ChatRoom.objects.all().filter(id=id)
        m = Message.objects.all().filter(conversation=chat_room[0])
        data = []
        k = 0
        for i in m:
            data.append({
                "conversation": i.conversation.id,
                "user_in": request.user.username,
                "sender": i.sender1.username,
                "receiver": i.receiver1.username,
                "message": i.message,
                "time": i.timestamp
            })
            k += 1
        return JsonResponse(data, content_type='application/json', safe=False)
    else:
        return redirect("login")
