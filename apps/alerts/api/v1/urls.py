from django.urls import path
from .views import SendAlertTelegram


urlpatterns = [
    path('send-telegram/', SendAlertTelegram.as_view())
]
