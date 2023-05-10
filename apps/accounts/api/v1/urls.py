from django.urls import path
from .views import AccountRegisterView, AccountLoginView

urlpatterns = [
    path('register/', AccountRegisterView.as_view()),
    path('login/', AccountLoginView.as_view()),

]
