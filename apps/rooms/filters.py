import django_filters

from apps.rooms.models import Room


class TimeFilter(django_filters.FilterSet):
    start_time = django_filters.DateTimeFilter()
    end_time = django_filters.DateTimeFilter()
    seats = django_filters.NumberFilter(field_name="seats", lookup_expr="exact")

    class Meta:
        model = Room
        fields = ["bookings__start_time", "bookings__end_time", "seats"]
