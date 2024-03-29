from django.urls import path
from apps.accounts.api.v1.views import auth, accounts


urlpatterns = [
    # auth
    path('get_sms_code/', auth.GetSMSCodeView.as_view()),
    path('verify_sms_code/', auth.VerifySMSCodeView.as_view()),
    path('register/', auth.RegisterView.as_view()),
    path('login/', auth.LoginView.as_view()),

    # accounts
    path('account/list/', accounts.AccountListView.as_view()),
    path('account/rud/<int:pk>/', accounts.AccountRUDView.as_view()),

]
