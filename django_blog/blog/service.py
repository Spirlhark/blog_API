import django_filters
from django_filters import rest_framework as filters

from .models import Post


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PostFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__title', lookup_expr='in')

    class Meta:
        model = Post
        fields = ['category', ]
