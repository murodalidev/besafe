from django.urls import path
from .views import SendAlertTelegram, SendAnonymousTelegram


urlpatterns = [
    path('send-telegram/', SendAlertTelegram.as_view()),
    path('send-telegram-anonymous/', SendAnonymousTelegram.as_view()),
]
