from django.urls import path, include



urlpatterns = [
    path('v1/', include('apps.post.api.v1.urls'))
]
