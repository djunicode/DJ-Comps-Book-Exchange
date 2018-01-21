from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        exclude = ["date_created"]


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        exclude = ["date_created", "post"]
