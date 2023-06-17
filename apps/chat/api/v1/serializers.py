from rest_framework import serializers

from apps.chat.models import Chat, Message, Media
from apps.accounts.api.v1.serializers import AccountSerializer


class ChatSerializer(serializers.ModelSerializer):
    sender = AccountSerializer()
    receiver = AccountSerializer()
    class Meta:
        model = Chat
        fields = ['id', 'sender', 'receiver', 'created_date']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'file']


class MessageSerializer(serializers.ModelSerializer):
    medias = MediaSerializer(required=False, many=True)
    is_mine = serializers.SerializerMethodField(read_only=True)

    def get_is_mine(self, obj):
        request = self.context['request']
        user_id = request.user.id
        return user_id == obj.room.sender_id

    class Meta:
        model = Message
        fields = ['id', 'room', 'message', 'medias', 'is_mine', 'created_date']




