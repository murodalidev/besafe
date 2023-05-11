from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('apps.accounts.api.v1.urls.accounts.urls')),
]
