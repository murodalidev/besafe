from django.urls import path
from apps.accounts.api.v1.views import auth


urlpatterns = [
    path('get_sms_code/', auth.GetSMSCodeView.as_view()),
    path('verify_sms_code/', auth.VerifySMSCodeView.as_view()),
    path('register/', auth.RegisterView.as_view()),
    path('login/', auth.LoginView.as_view()),

]
