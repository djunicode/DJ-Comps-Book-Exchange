from django.db import models
from django.contrib.auth.models import User


class DialogBox(models.Model):

    title = models.CharField(max_length=100)


class Message(models.Model):

    dialog = models.ForeignKey(DialogBox, on_delete=models.CASCADE)
    sender = models.ForeignKey(User)
    message = models.TextField(max_length=255)
    message_create_time = models.DateTimeField()

    def __unicode__(self):
        return self.message
