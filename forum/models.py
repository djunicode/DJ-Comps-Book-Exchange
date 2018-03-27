from django.db import models
from django.utils import timezone
# from django.urls import reverse
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey("auth.User")
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ["-date_created"]


class Comment(models.Model):
    post = models.ForeignKey("forum.Post", related_name="comments")
    user = models.ForeignKey("auth.User")
    comment = models.CharField(max_length=256)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment

    class Meta():
        ordering = ["-date_created"]
