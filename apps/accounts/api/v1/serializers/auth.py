import os
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import ValidationError

from apps.accounts.models import Account


class GetSMSCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(min_length=12)

    def validate(self, attrs):
        phone = attrs.get('phone')
        attrs['registered'] = False
        user = authenticate(username=phone, password=os.environ.get('ACCOUNT_DEFAULT_PASSWORD'))
        if user:
            attrs['registered'] = True
        return attrs


class VerifySMSCodeSerializer(serializers.Serializer):
    phone = serializers.CharField(min_length=12)
    verification_code = serializers.CharField(min_length=4, max_length=4, write_only=True)



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('phone', 'first_name', 'last_name', 'birth_date', 'avatar')
        extra_fields = {
            'avatar': {'required': False}
        }

    def create(self, validated_data):
        password = os.environ.get('ACCOUNT_DEFAULT_PASSWORD')
        validated_data['password'] = password
        validated_data['is_verified'] = True
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(min_length=12)
    verification_code = serializers.CharField(min_length=4, max_length=4, write_only=True)

    class Meta:
        fields = ('phone', 'verification_code')

    def validate(self, attrs):
        phone = attrs.get('phone')
        verification_code = attrs.get('verification_code', None)
        if verification_code != os.environ.get('VERIFICATION_CODE'):
            raise ValidationError({"verification_code": _("Verification code did not match")})
        user = authenticate(username=phone, password=os.environ.get('ACCOUNT_DEFAULT_PASSWORD'))
        if not user:
            raise AuthenticationFailed({'detail': "Incorrect number"})
        if not user.is_active:
            raise AuthenticationFailed({'detail': 'Account disabled'})
        if not user.is_verified:
            raise AuthenticationFailed({'detail': 'Account is not verified'})
        return user