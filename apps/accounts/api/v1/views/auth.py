from django.utils.translation import gettext_lazy as _
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from apps.accounts.api.v1.serializers import GetSMSCodeSerializer, VerifySMSCodeSerializer, RegisterSerializer, \
    LoginSerializer, AccountSerializer
from apps.accounts.models import Account
from apps.utils.verify_phone import get_sms_code, verify_sms_code



class GetSMSCodeView(generics.GenericAPIView):
    # http://127.0.0.1:8000/auth/api/v1/get_sms_code/
    serializer_class = GetSMSCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        dict_data = dict(data)
        phone = dict_data.get('phone')
        sms_code = get_sms_code(phone)
        if sms_code:
            return Response({"success": True, "detail": _("SMS code sent to phone number")})
        return Response({"success": False, "detail": _("SMS code sent failed please try again")})


class VerifySMSCodeView(generics.GenericAPIView):
    # http://127.0.0.1:8000/auth/api/v1/verify_sms_code/
    serializer_class = VerifySMSCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        dict_data = dict(data)
        phone = dict_data.get('phone')
        verification_code = dict_data.get('verification_code')
        verify = verify_sms_code(phone, verification_code)
        if not verify:
            return Response({"success": False, "detail": _("Verification code did not match")})
        try:
            user = Account.objects.get(phone=phone)
        except Account.DoesNotExist:
            new_user = Account.objects.create(phone=phone, is_verified=True)
            refresh = RefreshToken.for_user(new_user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            data = {
                "success": True,
                "created": True,
                "tokens": tokens
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except Account.MultipleObjectsReturned:
            return Response({"success": False, "detail": _("Multiple account returned for this number")},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            data = {
                "success": True,
                "tokens": tokens
            }
            return Response(data, status=status.HTTP_200_OK)


class RegisterView(generics.GenericAPIView):
    # http://127.0.0.1:8000/auth/api/v1/register/
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response({'success': True, 'data': user_data}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
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


