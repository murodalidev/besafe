# from django.shortcuts import get_object_or_404
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework import generics, permissions, status, views
# from rest_framework.response import Response
#
# from apps.chat.models import Room, Message, Media
# from .serializers import RoomSerializer, MessageSerializer
#
#
# class MessageView(views.APIView):
#     # http://127.0.0.1:8000/chat/v1/
#
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         # Add custom context data
#         print(context)
#         # context['extra_info'] = 'Additional information'
#         return context
#
#     def post(self, request, *args, **kwargs):
#         sender_id = request.data['sender']['id']
#         receiver_id = request.data['receiver']['id']
#         obj, created = Room.objects.get_or_create(sender_id=sender_id, receiver_id=receiver_id)
#         if created:
#             print(created)
#         print(obj)
#         return Response('ok')
#
#     @swagger_auto_schema(
#         manual_parameters=[
#             openapi.Parameter('sender_id', openapi.IN_QUERY, description='Sender ID', type=openapi.TYPE_INTEGER),
#             openapi.Parameter('receiver_id', openapi.IN_QUERY, description='Receiver ID', type=openapi.TYPE_INTEGER),
#         ]
#     )
#     def get(self, request, *args, **kwargs):
#         sender_id = request.GET.get('sender_id')
#         receiver_id = request.GET.get('receiver_id')
#         context = {
#             'request': request
#         }
#         room, created = Room.objects.get_or_create(sender_id=sender_id, receiver_id=receiver_id, is_deleted=False)
#         messages = Message.objects.filter(room_id=room.id)
#         serializer = MessageSerializer(messages, many=True, context=context)
#         return Response(serializer.data)
#
#
#
#
