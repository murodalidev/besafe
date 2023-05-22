from rest_framework import serializers

from apps.contact.models import Relationship, Contact
from apps.accounts.api.v1.serializers import AccountSerializer


class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = ['id', 'title', 'is_other']


class ContactSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    other_relationship = serializers.CharField(required=False, write_only=True)
    class Meta:
        model = Contact
        fields = ['id', 'author', 'relationship', 'other_relationship', 'name', 'phone', 'created_date']

    def create(self, validated_data):
        request = self.context['request']
        author_id = request.user.id
        other_relationship = validated_data.pop('other_relationship', None)
        if other_relationship:
            validated_data['relationship'] = other_relationship.capitalize()
        obj = Contact.objects.create(author_id=author_id, **validated_data)
        return obj

