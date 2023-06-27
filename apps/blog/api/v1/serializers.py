from rest_framework import serializers

from apps.blog.models import Category, Blog, BlogImage
from apps.accounts.api.v1.serializers import AccountSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class MiniBlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = ['id', 'image', 'is_main']


class BlogSerializer(serializers.ModelSerializer):
    images = MiniBlogImageSerializer(many=True, required=False)
    category = CategorySerializer(required=False)
    author = AccountSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'author', 'type', 'category', 'title', 'images', 'description', 'modified_date', 'created_date']

