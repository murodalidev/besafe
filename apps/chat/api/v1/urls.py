from django.urls import path

from .views import ChatListCreateView, MessageView

urlpatterns = [
    path('list-create/', ChatListCreateView.as_view()),
    path('messages/', MessageView.as_view()),
]
