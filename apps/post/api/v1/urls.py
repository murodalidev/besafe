from django.urls import path, include

from apps.post.api.v1.views import PostListCreateView, MyPostListCreateView, CommentListCreateView


urlpatterns = [
    path('list-create/', PostListCreateView.as_view()),
    path('my/list-create/', PostListCreateView.as_view()),
    path('<int:post_id>/comment/list-create/', CommentListCreateView.as_view()),
]
