from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, views
from rest_framework.response import Response

from apps.chat.models import Chat, Message, Media
from .serializers import ChatSerializer, MessageSerializer


class ChatListCreateView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/chat/v1/list-create/
    queryset = Chat.objects.filter(is_deleted=False)
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        return qs.filter(chat_members__member_id=user.id)


class MessageView(views.APIView):
    # http://127.0.0.1:8000/chat/v1/messages/
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('chat_id', openapi.IN_QUERY, description='Chat ID', type=openapi.TYPE_INTEGER),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'message': openapi.Schema(type=openapi.TYPE_STRING),
            }
        )
    )
    def post(self, request, *args, **kwargs):
        chat_id = request.GET.get('chat_id', None)
        message = request.data['message']
        user_id = request.user.id
        context = {
            "request": request
        }
        if chat_id:
            obj = Message.objects.create(chat_id=chat_id, sender_id=user_id, message=message)
            serializer = MessageSerializer(obj, context=context)
            return Response(serializer.data)
        return Response('ok')

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('chat_id', openapi.IN_QUERY, description='Chat ID', type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request, *args, **kwargs):
        chat_id = request.GET.get('chat_id', None)
        context = {
            'request': request
        }
        if chat_id:
            chat = Chat.objects.get(id=chat_id)
            if (request.user.id,) not in chat.chat_members.values_list('member_id'):
                return Response({"success": False, "message": "You have no any permissions for this chat"})
            messages = Message.objects.filter(chat_id=chat_id)
            serializer = MessageSerializer(messages, many=True, context=context)
            return Response(serializer.data)
        return Response([])




