import django_filters
from apps.blog.models import Blog


class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    category = django_filters.NumberFilter(field_name='category__id')

    class Meta:
        model = Blog
        fields = ['title', 'category']
