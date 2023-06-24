from rest_framework import serializers

from apps.chat.models import Chat, ChatMember, Message, Media
from apps.accounts.api.v1.serializers import AccountSerializer


class MiniChatMemberSerializer(serializers.ModelSerializer):
    member = AccountSerializer(required=False)
    class Meta:
        model = ChatMember
        fields = ['id', 'member']


class ChatSerializer(serializers.ModelSerializer):
    chat_members = MiniChatMemberSerializer(many=True, required=False)
    chat_name = serializers.SerializerMethodField(read_only=True)

    def get_chat_name(self, obj):
        if obj.type == 0:
            request = self.context['request']
            user_id = request.user.id
            member = ChatMember.objects.filter(chat_id=obj.id).exclude(member_id=user_id).first()
            return member.member.full_name
        return obj.name
    class Meta:
        model = Chat
        fields = ['id', 'name', 'chat_name', 'type', 'chat_members', 'created_date']


class MiniChatSerializer(serializers.ModelSerializer):
    chat_name = serializers.SerializerMethodField(read_only=True)

    def get_chat_name(self, obj):
        if obj.type == 0:
            request = self.context['request']
            user_id = request.user.id
            member = ChatMember.objects.filter(chat_id=obj.id).exclude(member_id=user_id).first()
            return member.member.full_name
        return obj.name

    class Meta:
        model = Chat
        fields = ['id', 'chat_name', 'type', 'created_date']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'file']


class MessageSerializer(serializers.ModelSerializer):
    chat = MiniChatSerializer(required=False)
    medias = MediaSerializer(required=False, many=True)
    is_mine = serializers.SerializerMethodField(read_only=True)
    sender = AccountSerializer(read_only=True)

    def get_is_mine(self, obj):
        request = self.context['request']
        user_id = request.user.id
        return user_id == obj.sender_id

    class Meta:
        model = Message
        fields = ['id', 'sender', 'chat', 'message', 'medias', 'is_mine', 'created_date']


