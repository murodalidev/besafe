from django.urls import path
from .views import VerifyNumberView, AccountRegisterView, AccountLoginView, AccountListView, AccountRUDView

urlpatterns = [
    path('verify_number/', VerifyNumberView.as_view()),
    path('register/', AccountRegisterView.as_view()),
    path('login/', AccountLoginView.as_view()),

    path('account/list/', AccountListView.as_view()),
    path('account/rud/<int:pk>/', AccountRUDView.as_view()),

]
