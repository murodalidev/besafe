from django.urls import path
from apps.blog.api.v1.views import CategoryView, BlogView, BlogDetailView


urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('blog/', BlogView.as_view()),
    path('blog/<int:pk>/', BlogDetailView.as_view()),
]
