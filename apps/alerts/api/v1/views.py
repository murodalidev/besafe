import requests
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SendAlertTelegram(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type="object",
            properties={
                "location_link": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["location_link"],
            example={
                "location_link": "",
            }
        ),
        responses={
            200: openapi.Response(description='Success response'),
            400: openapi.Response(description='Bad request'),
        }
    )
    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        location_link = data.get('location_link', None)
        token = "6810106730:AAHF9i80bHqW0qVEik8tnBYMH6j7e81Vi7c"
        chat_id = "-1002109325310"
        message = f"Name: {user.full_name}\nPhone: {user.phone}\nLocation: {location_link}"
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        respond = requests.get(url)
        if respond.ok:
            return Response({"success": True, "detail": "Send alert to telegram group"})
        return Response({"success": False, "detail": str(respond.text)})
