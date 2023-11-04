import django_filters

from .models import Consultant


class ConsultantFilter(django_filters.FilterSet):
    position = django_filters.NumberFilter(field_name='position__id')

    class Meta:
        model = Consultant
        fields = ['position']
