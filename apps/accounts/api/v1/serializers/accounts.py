from rest_framework import serializers

from apps.accounts.models import Account, Position, Consultant


class AccountSerializer(serializers.ModelSerializer):
    consultant_status = serializers.SerializerMethodField(read_only=True)

    def get_consultant_status(self, obj):
        try:
            obj.consultant
        except Consultant.DoesNotExist:
            return 0
        if obj.consultant.is_verified:
            return 2
        return 1


    class Meta:
        model = Account
        fields = ['id', 'phone', 'first_name', 'last_name', 'avatar', 'is_superuser', 'is_staff', 'is_active',
                  'is_verified', 'consultant_status', 'created_date', 'modified_date']
        read_only_fields = ['is_superuser', 'is_staff', 'is_active', 'is_verified', 'created_date', 'modified_date']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name')


class ConsultantListSerializer(serializers.ModelSerializer):
    position = PositionSerializer(required=False)
    user = AccountSerializer(read_only=True)

    class Meta:
        model = Consultant
        fields = ('id', 'user', 'position', 'bio')


class ConsultantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ('id', 'user', 'position', 'bio')
        extra_kwargs = {
            "user": {"required": False},
        }

    def create(self, validated_data):
        position = validated_data.pop('position', None)
        bio = validated_data.pop('bio', None)
        request = self.context['request']
        user_id = request.user.id
        instance = Consultant.objects.create(user_id=user_id, position_id=position.id, bio=bio)
        return instance


