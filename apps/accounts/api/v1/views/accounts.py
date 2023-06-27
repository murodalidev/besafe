from rest_framework import generics, status, views
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.accounts.api.v1.serializers import AccountSerializer, PositionSerializer, ConsultantListSerializer, \
    ConsultantCreateSerializer
from apps.accounts.models import Account, Position, Consultant
from apps.accounts.filters import ConsultantFilter
from apps.accounts.permissions import IsOwnerOrReadOnly


class AccountListView(generics.ListAPIView):
    # http://127.0.0.1:8000/accounts/api/v1/account/list/
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AccountRUDView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/accounts/api/v1/account/rud/{account_id}/
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


class MyProfileView(views.APIView):
    # http://127.0.0.1:8000/accounts/api/v1/account/profile/
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)


class PositionListView(generics.ListAPIView):
    # http://127.0.0.1:8000/accounts/api/v1/position-list/
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    pagination_class = None


class ConsultantListView(generics.ListAPIView):
    # http://127.0.0.1:8000/accounts/api/v1/consultant-list/
    queryset = Consultant.objects.filter(is_verified=True)
    serializer_class = ConsultantListSerializer
    pagination_class = None
    filterset_class = ConsultantFilter


class ConsultantCreateView(generics.CreateAPIView):
    # http://127.0.0.1:8000/accounts/api/v1/consultant-create/
    queryset = Consultant.objects.all()
    serializer_class = ConsultantCreateSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'position': openapi.Schema(
                    type=openapi.TYPE_INTEGER
                ),
                'bio': openapi.Schema(
                    type=openapi.TYPE_STRING
                ),
            },
            required=['position', 'bio']
        )
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
