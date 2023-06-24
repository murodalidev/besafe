from rest_framework import generics
from apps.blog.models import Category, Blog
from apps.blog.api.v1.serializers import CategorySerializer, BlogSerializer
from apps.blog.filters import BlogFilter


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_class = BlogFilter


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


