<<<<<<< HEAD
import django_filters
from django_filters import DateFilter,CharFilter

from . views import *

class orderFilter(django_filters.FilterSet):
    start = DateFilter(field_name='date_created',lookup_expr='gte')
    end = DateFilter(field_name='date_created',lookup_expr='lte')
    note = CharFilter(field_name='note',lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
=======
import django_filters
from django_filters import DateFilter,CharFilter

from . views import *

class orderFilter(django_filters.FilterSet):
    start = DateFilter(field_name='date_created',lookup_expr='gte')
    end = DateFilter(field_name='date_created',lookup_expr='lte')
    note = CharFilter(field_name='note',lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
>>>>>>> 7511be836ccd1300326d827fd7d821c5e95ba3b4
        exclude = ['customer','date_created']