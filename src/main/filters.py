import django_filters

from .models import Listing


class ListingFilter(django_filters.FilterSet):

    class Meta:
        model = Listing
        fields = {'transmisson': ['exact'], 'Brand': [
            'exact'], 'model': ['icontains'], 'Mileage': ['lt']}