from django.db.models import Q
from rest_framework import generics, permissions, status
from apps.blog.models import Category, Blog
from apps.blog.api.v1.serializers import CategorySerializer, BlogSerializer
from apps.blog.api.v1.filters import BlogFilter


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        qs = super().get_queryset()


class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.GET.get('category')
        title = self.request.GET.get('title')

        category_condition = Q()
        if category:
            category_condition = Q(category__exact=category)

        title_condition = Q()
        if title:
            title_condition = Q(title__icontains=title)
        qs = qs.filter(category_condition, title_condition)
        return qs


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


