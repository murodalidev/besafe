from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenBlacklistView

from apps.accounts.api.v1.views import auth


urlpatterns = [
    path('get_sms_code/', auth.GetSMSCodeView.as_view()),
    path('verify_sms_code/', auth.VerifySMSCodeView.as_view()),
    path('register/', auth.RegisterView.as_view()),
    path('login/', auth.LoginView.as_view()),

    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist')

]
