from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message, ChatRoom
from django.contrib.auth.models import User
import json
from pytz import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["id"]
        self.room_group_name = "chat_%s" % self.room_name
        self.users = await self.get_users(self.room_name)
        self.sender = self.users[0]
        self.receiver = self.users[1]

        print(self.sender + " - " + self.receiver)
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = text_data_json["sender"]
        receiver = text_data_json["receiver"]

        if message != "":
            add_chat = await self.add_chat(self.room_name, message, sender, receiver)
            print(add_chat)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": sender,
                "receiver": receiver,
            },
        )

    # Receive message from room group
    async def chat_message(self, event):
        chat_hist_data = await self.get_chats(self.room_name)

        await self.send(text_data=json.dumps({"data": chat_hist_data}))

    # Getting User List
    @database_sync_to_async
    def get_users(self, id):
        id = int(id)
        c = ChatRoom.objects.filter(id=id)[0]
        users = [c.sender.username, c.receiver.username]

        return users

    # Getting Chats
    @database_sync_to_async
    def get_chats(self, id):
        id = int(id)
        c = ChatRoom.objects.filter(id=id)[0]
        m = Message.objects.filter(conversation=c)

        chat_hist_data = []
        for i in m:
            IST = timezone("Asia/Kolkata")
            i.timestamp = i.timestamp.astimezone(IST)
            timestamp = (
                str(i.timestamp.day)
                + "/"
                + str(i.timestamp.month)
                + "/"
                + str(i.timestamp.year)
                + " "
                + str(i.timestamp.hour)
                + ":"
                + str(i.timestamp.minute)
            )
            chat_hist_data.append(
                {
                    "conversation": i.conversation.id,
                    "sender": i.sender1.username,
                    "receiver": i.receiver1.username,
                    "message": i.message,
                    "timestamp": timestamp,
                }
            )
        # print(chat_hist_data)

        return chat_hist_data

    @database_sync_to_async
    def add_chat(self, id, message, user1, user2):
        sender = User.objects.filter(username=user1)[0]
        receiver = User.objects.filter(username=user2)[0]
        c = ChatRoom.objects.filter(id=id)[0]

        m = Message.objects.create(
            conversation=c, message=message, sender1=sender, receiver1=receiver
        )

        m.save()

        return "Done"
