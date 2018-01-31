from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        exclude = ["user", "date_created"]


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        exclude = ["user", "date_created", "post"]
