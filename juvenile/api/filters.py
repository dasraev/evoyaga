from django.db.models import Q
from django_filters import rest_framework as filters

from juvenile import models


# Aniqlangan bolalar filter
class JuvenileFilter(filters.FilterSet):
    address = filters.CharFilter(method='search_address')
    address_region = filters.CharFilter(method='search_address_region')
    school_type = filters.CharFilter(method='search_school_type')
    birth_date = filters.DateFilter(method='search_birth_date')
    birth_region = filters.CharFilter(method='search_birth_region')
    birth_district = filters.CharFilter(method='search_birth_district')
    full_name = filters.CharFilter(method='search_by_full_name')

    class Meta:
        model = models.Juvenile
        fields = ['full_name', 'address', 'school_type', 'address_region']

    def search_address(self, queryset, name, value):
        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.filter(address__icontains=value).filter(markaz=user_markaz).filter(status="1")

    def search_address_region(self, queryset, name, value):
        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.filter(address_district__region_id__id__icontains=value).filter(
            markaz=user_markaz).filter(status="1")

    def search_birth_region(self, queryset, name, value):
        user_markaz = self.request.user.markaz

        personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_district__region_id=value)

        juveniles_ids = []

        queryset = models.Juvenile.objects.filter(juvenile_markaz__markaz=user_markaz)
        list_juveniles = list(queryset)
        incomplete_juveniles = []
        for juvenile in list_juveniles:
            personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not personal_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            address_info = models.AddressInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not address_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            education_info = models.EducationInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not education_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            parent_info = models.ParentInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not parent_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

        for incomplete_juvenile in incomplete_juveniles:
            personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=incomplete_juvenile.id).order_by(
                '-created_at').first()

            if personal_info:
                if personal_info.passport_type == '5':
                    incomplete_juveniles.remove(incomplete_juvenile)

        incomplete_juvenile_ids = []
        for item in incomplete_juveniles:
            incomplete_juvenile_ids.append(item.id)


        for item in personal_infos:
            juveniles_ids.append(item.juvenile_id)


        for juvenile_id in juveniles_ids:
            if juvenile_id in incomplete_juvenile_ids:
                juveniles_ids.remove(juvenile_id)
        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=1)


        filtered_juveniles = []
        for item in juveniles:
            if item not in filtered_juveniles:
                filtered_juveniles.append(item)

        juvenile_ids = []
        for item in filtered_juveniles:
            juvenile_ids.append(item.id)

        juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)


        return juveniles

    def search_birth_district(self, queryset, name, value):
        user_markaz = self.request.user.markaz

        personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_district_id=value)

        juveniles_ids = []

        queryset = models.Juvenile.objects.filter(juvenile_markaz__markaz=user_markaz)
        list_juveniles = list(queryset)
        incomplete_juveniles = []
        for juvenile in list_juveniles:
            personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not personal_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            address_info = models.AddressInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not address_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            education_info = models.EducationInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not education_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            parent_info = models.ParentInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not parent_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

        for incomplete_juvenile in incomplete_juveniles:
            personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=incomplete_juvenile.id).order_by(
                '-created_at').first()

            if personal_info:
                if personal_info.passport_type == '5':
                    incomplete_juveniles.remove(incomplete_juvenile)

        incomplete_juvenile_ids = []
        for item in incomplete_juveniles:
            incomplete_juvenile_ids.append(item.id)


        for item in personal_infos:
            juveniles_ids.append(item.juvenile_id)


        for juvenile_id in juveniles_ids:
            if juvenile_id in incomplete_juvenile_ids:
                juveniles_ids.remove(juvenile_id)
        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=1)


        filtered_juveniles = []
        for item in juveniles:
            if item not in filtered_juveniles:
                filtered_juveniles.append(item)

        juvenile_ids = []
        for item in filtered_juveniles:
            juvenile_ids.append(item.id)

        juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)


        return juveniles

    def search_school_type(self, queryset, name, value):
        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.filter(school_type__contains=value).filter(markaz=user_markaz).filter(status="1")

    def search_birth_date(self, queryset, name, value):
        user_markaz = self.request.user.markaz

        personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_date=value)

        juveniles_ids = []

        queryset = models.Juvenile.objects.filter(juvenile_markaz__markaz=user_markaz)
        list_juveniles = list(queryset)
        incomplete_juveniles = []
        for juvenile in list_juveniles:
            personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not personal_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            address_info = models.AddressInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not address_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            education_info = models.EducationInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not education_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            parent_info = models.ParentInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not parent_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

        for incomplete_juvenile in incomplete_juveniles:
            personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=incomplete_juvenile.id).order_by(
                '-created_at').first()

            if personal_info:
                if personal_info.passport_type == '5':
                    incomplete_juveniles.remove(incomplete_juvenile)

        incomplete_juvenile_ids = []
        for item in incomplete_juveniles:
            incomplete_juvenile_ids.append(item.id)


        for item in personal_infos:
            juveniles_ids.append(item.juvenile_id)


        for juvenile_id in juveniles_ids:
            if juvenile_id in incomplete_juvenile_ids:
                juveniles_ids.remove(juvenile_id)
        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=1)


        filtered_juveniles = []
        for item in juveniles:
            if item not in filtered_juveniles:
                filtered_juveniles.append(item)

        juvenile_ids = []
        for item in filtered_juveniles:
            juvenile_ids.append(item.id)

        juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)


        return juveniles

    def search_by_full_name(self, qs, name, value):
        user_markaz = self.request.user.markaz

        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]

        qs = models.PersonalInfoJuvenile.objects.all()
        juveniles_id = []

        queryset = models.Juvenile.objects.filter(juvenile_markaz__markaz=user_markaz)
        list_juveniles = list(queryset)
        incomplete_juveniles = []
        for juvenile in list_juveniles:
            personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not personal_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            address_info = models.AddressInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not address_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            education_info = models.EducationInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not education_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

            parent_info = models.ParentInfoJuvenile.objects.filter(juvenile_id=juvenile.id)
            if not parent_info:
                if juvenile not in incomplete_juveniles:
                    incomplete_juveniles.append(juvenile)

        for incomplete_juvenile in incomplete_juveniles:
            personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=incomplete_juvenile.id).order_by(
                '-created_at').first()

            if personal_info:
                if personal_info.passport_type == '5':
                    incomplete_juveniles.remove(incomplete_juvenile)

        incomplete_juvenile_ids = []
        for item in incomplete_juveniles:
            incomplete_juvenile_ids.append(item.id)

        for term in value.split():
            qs = qs.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term) | Q(father_name__icontains=term))
            for item in qs:
                juveniles_id.append(item.juvenile_id)

        for juvenile_id in juveniles_id:
            if juvenile_id in incomplete_juvenile_ids:
                juveniles_id.remove(juvenile_id)
        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_id).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=1)

        filtered_juveniles = []
        for item in juveniles:
            if item not in filtered_juveniles:
                filtered_juveniles.append(item)

        juvenile_ids = []
        for item in filtered_juveniles:
            juvenile_ids.append(item.id)

        juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)

        if user_code == 1:
            juveniles = models.Juvenile.objects.filter(pk__in=juveniles_id)

        return juveniles


# Markazga qabul qilingan bolalar filter
class JuvenileAcceptedFilter(filters.FilterSet):
    full_name = filters.CharFilter(method='search_by_full_name')
    birth_date = filters.DateFilter(method='search_birth_date')
    birth_region = filters.CharFilter(method='search_birth_region')
    birth_district = filters.CharFilter(method='search_birth_district')

    def search_by_full_name(self, qs, name, value):
        user_markaz = self.request.user.markaz

        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]

        qs = models.PersonalInfoJuvenile.objects.all()
        juveniles_id = []
        for term in value.split():
            qs = qs.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term) | Q(father_name__icontains=term))
            for item in qs:
                juveniles_id.append(item.juvenile_id)

        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_id).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=2)
        if user_code == 1:
            juveniles = models.Juvenile.objects.filter(pk__in=juveniles_id)

        return juveniles

    class Meta:
        model = models.Juvenile
        fields = ['birth_date', 'birth_region', 'birth_district']

    def search_birth_region(self, queryset, name, value):
        user_markaz = self.request.user.markaz

        personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_district__region_id=value)

        juveniles_ids = []


        for item in personal_infos:
            juveniles_ids.append(item.juvenile_id)

        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=2)


        filtered_juveniles = []
        for item in juveniles:
            if item not in filtered_juveniles:
                filtered_juveniles.append(item)

        juvenile_ids = []
        for item in filtered_juveniles:
            juvenile_ids.append(item.id)

        juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)


        return juveniles

    def search_birth_district(self, queryset, name, value):
        user_markaz = self.request.user.markaz

        personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_district_id=value)

        juveniles_ids = []


        for item in personal_infos:
            juveniles_ids.append(item.juvenile_id)

        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=2)


        filtered_juveniles = []
        for item in juveniles:
            if item not in filtered_juveniles:
                filtered_juveniles.append(item)

        juvenile_ids = []
        for item in filtered_juveniles:
            juvenile_ids.append(item.id)

        juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)


        return juveniles

    def search_birth_date(self, queryset, name, value):
        user_markaz = self.request.user.markaz

        personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_date=value)

        juveniles_ids = []


        for item in personal_infos:
            juveniles_ids.append(item.juvenile_id)

        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=2)


        filtered_juveniles = []
        for item in juveniles:
            if item not in filtered_juveniles:
                filtered_juveniles.append(item)

        juvenile_ids = []
        for item in filtered_juveniles:
            juvenile_ids.append(item.id)

        juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)


        return juveniles


# Taqsimlangan bolalar filter
class JuvenileExpelledFilter(filters.FilterSet):
    full_name = filters.CharFilter(method='search_by_full_name')
    birth_date = filters.DateFilter(method='search_birth_date')
    birth_region = filters.CharFilter(method='search_birth_region')
    birth_district = filters.CharFilter(method='search_birth_district')

    def search_by_full_name(self, qs, name, value):
        user_markaz = self.request.user.markaz
        markaz_tuman = self.request.user.markaz_tuman

        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]

        qs = models.PersonalInfoJuvenile.objects.all()
        juveniles_id = []
        for term in value.split():
            qs = qs.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term) | Q(father_name__icontains=term))
            for item in qs:
                juveniles_id.append(item.juvenile_id)

        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_id).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=3)
        if markaz_tuman:
            juveniles = models.Juvenile.objects.filter(pk__in=juveniles_id).filter(
                juvenile_markaz__monitoring_markaz_tuman=markaz_tuman).filter(juvenile_markaz__status=3)
        if user_code == 1:
            juveniles = models.Juvenile.objects.filter(pk__in=juveniles_id)

        return juveniles

    def search_birth_region(self, queryset, name, value):
        user_markaz = self.request.user.markaz
        markaz_tuman = self.request.user.markaz_tuman

        personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_district__region_id=value)

        juveniles_ids = []


        for item in personal_infos:
            juveniles_ids.append(item.juvenile_id)

        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(
            juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=3)

        if markaz_tuman:
            juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__monitoring_markaz_tuman=markaz_tuman).filter(juvenile_markaz__status=3)


        filtered_juveniles = []
        for item in juveniles:
            if item not in filtered_juveniles:
                filtered_juveniles.append(item)

        juvenile_ids = []
        for item in filtered_juveniles:
            juvenile_ids.append(item.id)

        juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)


        return juveniles

    def search_birth_district(self, queryset, name, value):
        user_markaz = self.request.user.markaz
        markaz_tuman = self.request.user.markaz_tuman

        personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_district_id=value)

        juveniles_ids = []


        for item in personal_infos:
            juveniles_ids.append(item.juvenile_id)

        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=3)

        if markaz_tuman:
            juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__monitoring_markaz_tuman=markaz_tuman).filter(juvenile_markaz__status=3)


        filtered_juveniles = []
        for item in juveniles:
            if item not in filtered_juveniles:
                filtered_juveniles.append(item)

        juvenile_ids = []
        for item in filtered_juveniles:
            juvenile_ids.append(item.id)

        juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)


        return juveniles

    def search_birth_date(self, queryset, name, value):
        user_markaz = self.request.user.markaz
        markaz_tuman = self.request.user.markaz_tuman
        personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_date=value)

        juveniles_ids = []


        for item in personal_infos:
            juveniles_ids.append(item.juvenile_id)

        juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(
            juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=3)
        if markaz_tuman:
            juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__monitoring_markaz_tuman=markaz_tuman).filter(juvenile_markaz__status=3)


        filtered_juveniles = []
        for item in juveniles:
            if item not in filtered_juveniles:
                filtered_juveniles.append(item)

        juvenile_ids = []
        for item in filtered_juveniles:
            juvenile_ids.append(item.id)

        juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)


        return juveniles


# Umimiy hisobotlat filter
class JuvenileReportFilter(filters.FilterSet):
    status = filters.CharFilter(method='filter_by_status')
    full_name = filters.CharFilter(method='search_by_full_name')
    address_region = filters.CharFilter(method='search_address_region')
    school_type = filters.CharFilter(method='search_education_type')

    class Meta:
        model = models.Juvenile_Markaz
        fields = ['address_region']

    def search_by_full_name(self, qs, name, value):
        user_markaz = self.request.user.markaz
        markaz_tuman = self.request.user.markaz_tuman

        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]


        qs = models.PersonalInfoJuvenile.objects.all()
        juveniles_id = []
        for term in value.split():
            qs = qs.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term) | Q(father_name__icontains=term))
            for item in qs:
                juveniles_id.append(item.juvenile_id)

        juveniles = models.Juvenile_Markaz.objects.filter(juvenile_id__in=juveniles_id).filter(markaz=user_markaz)
        if user_code == 4:
            juveniles = models.Juvenile_Markaz.objects.filter(juvenile_id__in=juveniles_id).filter(monitoring_markaz_tuman=markaz_tuman)

        if user_code == 1:
            juveniles = models.Juvenile_Markaz.objects.filter(juvenile_id__in=juveniles_id)

        return juveniles

    def search_address_region(self, queryset, name, value):
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]

        user_markaz = self.request.user.markaz
        markaz_tuman = self.request.user.markaz_tuman
        juvenile_ids = []
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            markaz=user_markaz)

        if user_code == 4:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(monitoring_markaz_tuman=markaz_tuman)

        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile_id)

        address_infos = models.AddressInfoJuvenile.objects.filter(address_mahalla__district_id__region_id__id__icontains=value).filter(
            juvenile__id__in=juvenile_ids)

        
        with_address_juvenile_ids = []
        for address_info in address_infos:
            with_address_juvenile_ids.append(address_info.juvenile_id)

        if user_code == 1:
            juveniles_id = []
            address_infos = models.AddressInfoJuvenile.objects.filter(
                address_mahalla__district_id__region_id__id__icontains=value)

            for item in address_infos:
                juveniles_id.append(item.juvenile_id)

            juveniles = models.Juvenile_Markaz.objects.filter(juvenile_id__in=juveniles_id)
            return juveniles

        if user_code == 4:
            return models.Juvenile_Markaz.objects.filter(juvenile_id__in=with_address_juvenile_ids).filter(
                monitoring_markaz_tuman=markaz_tuman)

        return models.Juvenile_Markaz.objects.filter(juvenile_id__in=with_address_juvenile_ids)

    def filter_by_status(self, queryset, name, value):
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]

        if user_code == 1:
            return models.Juvenile_Markaz.objects.filter(status=value)

        if user_code == 4:
            markaz_tuman = self.request.user.markaz_tuman
            return models.Juvenile_Markaz.objects.filter(status=value).filter(monitoring_markaz_tuman=markaz_tuman)

        user_markaz = self.request.user.markaz
        return models.Juvenile_Markaz.objects.filter(status=value).filter(markaz=user_markaz)

    def search_education_type(self, queryset, name, value):
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]

        user_markaz = self.request.user.markaz
        markaz_tuman = self.request.user.markaz_tuman
        juvenile_ids = []
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            markaz=user_markaz)

        if user_code == 4:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(monitoring_markaz_tuman=markaz_tuman)

        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile_id)

        school_types = models.EducationInfoJuvenile.objects.filter(school_type=value).filter(
            juvenile__id__in=juvenile_ids)

        education_juvenile_ids = []
        for school_type in school_types:
            education_juvenile_ids.append(school_type.juvenile_id)

        if user_code == 1:
            juveniles_id = []
            education_infos = models.EducationInfoJuvenile.objects.filter(school_type=value)

            for item in education_infos:
                juveniles_id.append(item.juvenile_id)

            juveniles = models.Juvenile_Markaz.objects.filter(juvenile_id__in=juveniles_id)
            return juveniles


        if user_code == 4:
            return models.Juvenile_Markaz.objects.filter(juvenile_id__in=education_juvenile_ids).filter(
                monitoring_markaz_tuman=markaz_tuman)

        return models.Juvenile_Markaz.objects.filter(juvenile_id__in=education_juvenile_ids)
