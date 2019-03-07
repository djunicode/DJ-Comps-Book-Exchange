from django.contrib import admin
from forum.models import Post, Comment, Upvote

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Upvote)
