from rest_framework import serializers

from apps.post.models import Post, PostImage, Comment
from apps.accounts.api.v1.serializers import AccountSerializer


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image', 'is_main']


class PostSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    images = PostImageSerializer(required=False, many=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'images', 'description', 'modified_date', 'created_date']

    def create(self, validated_data):
        description = validated_data.pop('description')
        images = validated_data.pop('images', [])
        request = self.context['request']
        user_id = request.user.id
        obj = Post.objects.create(author_id=user_id, description=description)
        for image in images:
            PostImage.objects.create(post_id=obj.id, image=image['image'])
        return obj



class MiniCommentSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'parent_comment', 'top_level_comment_id', 'message', 'created_date']


class CommentSerializer(serializers.ModelSerializer):

    author = AccountSerializer(read_only=True)
    children = serializers.SerializerMethodField(read_only=True)

    def get_children(self, obj):
        children = Comment.objects.filter(top_level_comment_id=obj.id).exclude(id=obj.top_level_comment_id)
        serializer = MiniCommentSerializer(children, many=True)
        return serializer.data

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'parent_comment', 'top_level_comment_id', 'message', 'children', 'created_date']
        read_only_fields = ['top_level_comment_id', 'created_date']


    def create(self, validated_data):
        parent_comment = validated_data.get('parent_comment')
        message = validated_data.get('message')
        request = self.context['request']
        post_id = self.context['post_id']
        user_id = request.user.id
        obj = Comment.objects.create(author_id=user_id, post_id=post_id, parent_comment=parent_comment, message=message)
        return obj

