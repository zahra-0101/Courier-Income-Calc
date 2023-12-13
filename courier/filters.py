import django_filters
from .models import WeeklySalary
from django.forms.widgets import DateInput


class WeeklySalaryFilter(django_filters.FilterSet):
    courier_id = django_filters.NumberFilter(
        field_name='courier__id',
        label='Courier ID'
    )
    from_date = django_filters.DateFilter(
        field_name='week_start_date', lookup_expr='gte',
        widget=DateInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )
    to_date = django_filters.DateFilter(
        field_name='week_start_date', lookup_expr='lte',
        widget=DateInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )

    class Meta:
        model = WeeklySalary
        fields = []
