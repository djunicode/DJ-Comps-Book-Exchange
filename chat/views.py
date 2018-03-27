from django.shortcuts import render
# from django.contrib.auth.models import User                                # Django Build in User Model
# from django.http.response import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from .models import Message
# from .serializers import MessageSerializer, UserSerializer
# from django.shortcuts import render, get_object_or_404
from book_listing.models import Book_List
from sign_in.models import Profile
# from django.views.generic import CreateView
# from django.urls import reverse_lazy, reverse


# Decorator to make the view csrf excempt.
def user_list(request):
    users = Profile.objects.all()
    return render(request, 'chat/users.html', {'users': users})


def message(request, book_id):
    sender = request.user
    b = Book_List.objects.get(id=book_id)
    rec = b.user
    messagessend = Message.objects.order_by('timestamp')
    messagesrec = Message.objects.filter(sender=rec, receiver=sender).order_by('timestamp')
    if request.method == 'GET':
        return render(request, 'chat/chat.html',
                      {'sender': sender, 'book': book_id, 'receiver': rec,
                       'messagessend': messagessend, 'mess': messagesrec})
    elif request.method == 'POST':
        mes = request.POST.get('message_cont')
        if sender.is_authenticated:
            p = Message(message=mes, sender=sender, receiver=rec)
            p.save()
        else:
            p1 = Message(message=mes, sender=rec, receiver=sender)
            p1.save()
        messagessend = Message.objects.order_by('timestamp')
        messagesrec = Message.objects.filter(sender=rec, receiver=sender).order_by('timestamp')
        return render(request, 'chat/chat.html', {'book_id': book_id, 'messagessend': messagessend,
                                                  'mess': messagesrec})


def messageview(request, user_id):
    sender = request.user
    user_det = Profile.objects.get(id=user_id)
    user_name = user_det.user
    receiver = user_det.user
    messagessend = Message.objects.order_by('timestamp')
    messagesrec = Message.objects.filter(sender=receiver, receiver=sender).order_by('timestamp')
    if request.method == 'GET':
        return render(request, 'chat/chat.html',
                      {'sender': sender, 'receiver': receiver,
                       'messagessend': messagessend, 'mess': messagesrec, 'username': user_name})
    elif request.method == 'POST':
        mes = request.POST.get('message_cont')
        if sender.is_authenticated:
            p = Message(message=mes, sender=sender, receiver=receiver)
            p.save()
        else:
            p1 = Message(message=mes, sender=receiver, receiver=sender)
            p1.save()
        messagessend = Message.objects.order_by('timestamp')
        messagesrec = Message.objects.filter(sender=receiver, receiver=sender)
        return render(request, 'chat/chat.html', {'messagessend': messagessend,
                                                  'mess': messagesrec, 'username': user_name})
