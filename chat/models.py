from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse("chat:message-list")

    class Meta:
        ordering = ('timestamp',)
