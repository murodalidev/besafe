from rest_framework import generics, permissions

from apps.contact.models import Relationship, Contact
from .serializers import RelationshipSerializer, ContactSerializer
from ...permissions import IsOwnerOrReadOnly


class RelationshipView(generics.ListAPIView):
    # http://127.0.0.1:8000/contact/relationships/
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    pagination_class = None

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('-id')


class ContactView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/contact/list/
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        user_id = self.request.user.id
        name = self.request.GET.get('name')
        if name:
            return qs.filter(name__icontains=name)
        return qs.filter(author_id=user_id)


class ContactDetailView(generics.RetrieveDestroyAPIView):
    # http://127.0.0.1:8000/contact/{contact_id}/
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
