from django.db import models
from django.contrib.auth.models import User


class Book_List(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    book_image = models.FileField(null=True)
