from django_filters import rest_framework as filters

from accounts import models


class UserFilter(filters.FilterSet):
    position = filters.CharFilter(method='filter_position')

    class Meta:
        model = models.CustomUser
        fields = ['markaz']

    def filter_position(self, queryset, name, value):
        return models.CustomUser.objects.filter(groups__code=value).filter(groups__code__gte=2)