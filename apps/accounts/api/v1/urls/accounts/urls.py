from django.urls import path
from apps.accounts.api.v1.views import accounts


urlpatterns = [
    path('account/list/', accounts.AccountListView.as_view()),
    path('account/rud/<int:pk>/', accounts.AccountRUDView.as_view()),
    path('account/profile/', accounts.MyProfileView.as_view()),
    path('position-list/', accounts.PositionListView.as_view()),
    path('consultant-list/', accounts.ConsultantListView.as_view()),
    path('consultant-create/', accounts.ConsultantCreateView.as_view()),
]
