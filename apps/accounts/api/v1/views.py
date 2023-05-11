from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.accounts.api.v1.serializers import VerifyNumberSerializer,  RegisterSerializer, LoginSerializer, \
    AccountSerializer
from apps.accounts.models import Account
from apps.accounts.permissions import IsOwnerOrReadOnly


class VerifyNumberView(generics.GenericAPIView):
    # http://127.0.0.1:8000/auth/api/v1/verify_number/
    serializer_class = VerifyNumberSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        dict_data = dict(data)
        is_registered = dict_data.get('registered')
        if is_registered:
            try:
                user = Account.objects.get(phone=dict_data.get('phone'))
            except Account.DoesNotExist:
                raise ValueError({"detail": "Account object does not exist for this number"})
            except Account.MultipleObjectsReturned:
                raise ValueError({"detail": "Multiple account returned for this number"})
            else:
                refresh = RefreshToken.for_user(user)
                tokens = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)
                }
                return Response(tokens, status=status.HTTP_200_OK)

        return Response(dict_data, status=status.HTTP_200_OK)


class AccountRegisterView(generics.GenericAPIView):
    # http://127.0.0.1:8000/auth/api/v1/register/
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response({'success': True, 'data': user_data}, status=status.HTTP_201_CREATED)


class AccountLoginView(generics.GenericAPIView):
    # http://127.0.0.1:8000/auth/api/v1/login/
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return Response(tokens, status=status.HTTP_200_OK)


class AccountListView(generics.ListAPIView):
    # http://127.0.0.1:8000/auth/api/v1/account/list/
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


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
