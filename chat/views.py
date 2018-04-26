from django.shortcuts import render
from .models import Message
from sign_in.models import Profile
from itertools import chain


# Decorator to make the view csrf excempt.
def user_list(request):
    users = Profile.objects.all()
    return render(request, 'chat/users.html', {'users': users})


def messageview(request, user_id, rec_id):
    sender = Profile.objects.get(user=user_id)
    receiver = Profile.objects.get(user=rec_id)
    messagessend = Message.objects.filter(sender=user_id, receiver=rec_id)
    messagesrec = Message.objects.filter(sender=rec_id, receiver=user_id)
    result_mess = sorted(chain(messagessend, messagesrec), key=lambda instance: instance.timestamp)
    if request.method == 'GET':
        return render(request, 'chat/chat.html',
                      {'sender': sender, 'receiver': receiver, 'messages': result_mess})

    elif request.method == 'POST':
        mes = request.POST.get('message_cont')
        if mes is not None:
            p = Message(message=mes, sender=sender.user, receiver=receiver.user)
            p.save()
        messagessend = Message.objects.filter(sender=user_id, receiver=rec_id)
        messagesrec = Message.objects.filter(sender=rec_id, receiver=user_id)
        result_mess = sorted(chain(messagessend, messagesrec), key=lambda instance: instance.timestamp)
        return render(request, 'chat/chat.html',
                      {'sender': sender, 'receiver': receiver, 'messages': result_mess})
