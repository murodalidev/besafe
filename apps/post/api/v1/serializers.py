from rest_framework import serializers

from apps.post.models import Post, PostImage, Comment
from apps.accounts.api.v1.serializers import AccountSerializer


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']


class PostSerializers(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    images = PostImageSerializer(required=False)
    class Meta:
        model = Post
        fields = ['id', 'author', 'description', 'images', 'modified_date', 'created_date']

    def create(self, validated_data):
        description = validated_data.pop('description')
        images = validated_data.pop('images')
        request = self.context['request']
        user_id = request.user.id
        obj = Post.objects.create(author_id=user_id, description=description)
        return obj

