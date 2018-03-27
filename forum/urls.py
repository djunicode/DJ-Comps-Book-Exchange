from django.conf.urls import url
from .views import (PostCreate,
                    PostUpdate,
                    PostDelete,
                    comment_to_post,
                    CommentDelete,
                    CommentUpdate,
                    search_post,
                    )

urlpatterns = [
    url(r'^$', search_post, name="list"),  # PostList.as_view()
    url(r'^create/$', PostCreate.as_view(), name="create"),
    url(r'^update/(?P<pk>\d+)/$', PostUpdate.as_view(), name="update"),
    url(r'^delete/(?P<pk>\d+)/$', PostDelete.as_view(), name="delete"),
    url(r'^comment/(?P<pk>\d+)/$', comment_to_post, name="comment"),
    url(r'^comment/delete/(?P<pk>\d+)/$', CommentDelete.as_view(), name="comment_delete"),
    url(r'^comment/update/(?P<pk>\d+)/$', CommentUpdate.as_view(), name="comment_update"),
]
