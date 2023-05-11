from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.accounts.api.v1.serializers import AccountSerializer
from apps.accounts.models import Account
from apps.accounts.permissions import IsOwnerOrReadOnly


class AccountListView(generics.ListAPIView):
    # http://127.0.0.1:8000/auth/api/v1/account/list/
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AccountRUDView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/auth/api/v1/account/rud/{account_id}/
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"success": True, "detail": "Account successfully deactivated"}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.is_verified = False
        instance.save()
