from rest_framework import serializers

from apps.blog.models import Category, Blog, BlogImage


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

    class Meta:
        model = Blog
        fields = ['id', 'category', 'title', 'images', 'description', 'modified_date', 'created_date']

