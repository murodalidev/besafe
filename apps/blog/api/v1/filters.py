from django_filters import FilterSet, CharFilter
from apps.blog.models import Blog


class BlogFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')
    category = CharFilter(lookup_expr='exact')

    class Meta:
        model = Blog
        fields = ['title', 'category']
