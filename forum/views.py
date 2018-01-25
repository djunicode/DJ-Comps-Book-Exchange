from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormUserNeededMixin, UserOwnerMixin
# Create your views here.


class PostList(ListView):
    template_name = 'forum/index.html'
    context_object_name = 'forum'

    def get_queryset(self):
        return Post.objects.all()


class PostCreate(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    template_name = "forum/create.html"
    form_class = PostForm
    model = Post
    login_url = "/admin/"
    success_url = reverse_lazy("forum:list")
    context_object_name = 'forum'


class PostUpdate(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Post.objects.all()
    form_class = PostForm
    model = Post
    template_name = "forum/update.html"
    context_object_name = 'forum'
    success_url = reverse_lazy("forum:list")


class PostDelete(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = Post
    template_name = "forum/delete.html"
    success_url = reverse_lazy("forum:list")
    context_object_name = 'forum'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render(request, 'forum/not_allowed.html', {"txt": "You are not allowed to delete this."})



def comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        return redirect('/forum/')
    else:
        form = CommentForm()
    return render(request, 'forum/comment_create.html', {'form': form})


class CommentDelete(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = Comment
    template_name = "forum/comm_delete.html"
    success_url = reverse_lazy("forum:list")


class CommentUpdate(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Comment.objects.all()
    form_class = CommentForm
    model = Comment
    template_name = "forum/comm_update.html"
    success_url = reverse_lazy("forum:list")
