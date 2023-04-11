import django_filters
from .models import LedgerUpdate
class LedgerUpdateFilter(django_filters.FilterSet):
    authentication_code = django_filters.NumberFilter(field_name='authentication_code')

    class Meta:
        model = LedgerUpdate
        fields = ['authentication_code']
