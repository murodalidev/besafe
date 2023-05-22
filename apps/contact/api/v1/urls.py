from django.urls import path
from .views import RelationshipView, ContactView, ContactDetailView


urlpatterns = [
    path('relationships/', RelationshipView.as_view()),
    path('list/', ContactView.as_view()),
    path('detail/<int:pk>/', ContactDetailView.as_view()),
]
