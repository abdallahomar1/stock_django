import django_filters
from . models import orders5, prodect
class ordersFilter(django_filters.FilterSet):
    names = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = orders5
        fields = ['names', 'id']
