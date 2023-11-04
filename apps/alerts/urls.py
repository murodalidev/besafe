from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('apps.alerts.api.v1.urls')),
]
