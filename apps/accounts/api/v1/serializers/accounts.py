from rest_framework import serializers

from apps.accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'phone', 'first_name', 'last_name', 'avatar', 'is_superuser', 'is_staff', 'is_active',
                  'is_verified', 'created_date', 'modified_date']
        read_only_fields = ['is_superuser', 'is_staff', 'is_active', 'is_verified', 'created_date', 'modified_date']
