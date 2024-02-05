from django.db.models import Q
from django_filters import rest_framework as filters

from juvenile import models
from django.db.models import Count
from django.shortcuts import get_object_or_404

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
        queryset = queryset.filter(juvenile__birth_district__region_id=value)
        return queryset

    def search_birth_district(self, queryset, name, value):
        queryset = queryset.filter(juvenile__birth_district_id=value)
        return queryset

    def search_school_type(self, queryset, name, value):
        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.filter(school_type__contains=value).filter(markaz=user_markaz).filter(status="1")

    def search_birth_date(self, queryset, name, value):

        queryset = queryset.filter(juvenile__birth_date=value)

        return queryset

    def search_by_full_name(self, qs, name, value):

        group_codes = self.request.user.groups.values_list('code', flat=True)

        for term in value.split():
            qs = qs.filter(Q(juvenile__first_name__icontains=term) | Q(juvenile__last_name__icontains=term) | Q(juvenile__father_name__icontains=term))

        return qs


# Markazga qabul qilingan bolalar filter
class JuvenileAcceptedFilter(filters.FilterSet):
    full_name = filters.CharFilter(method='search_by_full_name')
    birth_date = filters.DateFilter(method='search_birth_date')
    birth_region = filters.CharFilter(method='search_birth_region')
    birth_district = filters.CharFilter(method='search_birth_district')
    class Meta:
        model = models.Juvenile
        fields = ['birth_date', 'birth_region', 'birth_district']

    #####
    def search_by_full_name(self, qs, name, value):
        for term in value.split():
            qs = qs.filter(Q(juvenile__first_name__icontains=term) | Q(juvenile__last_name__icontains=term) | Q(juvenile__father_name__icontains=term))
        return qs
    def search_birth_region(self, queryset, name, value):
        queryset = queryset.filter(juvenile__birth_district__region_id=value)
        return queryset

    def search_birth_district(self, queryset, name, value):
        queryset = queryset.filter(juvenile__birth_district_id=value)
        return queryset
    def search_birth_date(self, queryset, name, value):

        queryset = queryset.filter(juvenile__birth_date=value)

        return queryset


    ######
    # def search_by_full_name(self, qs, name, value):
    #     user_markaz = self.request.user.markaz
    #
    #     group_codes = self.request.user.groups.values_list('code', flat=True)
    #     user_code = list(group_codes)[0]
    #
    #     qs = models.PersonalInfoJuvenile.objects.all()
    #     juveniles_id = []
    #     for term in value.split():
    #         qs = qs.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term) | Q(father_name__icontains=term))
    #         for item in qs:
    #             juveniles_id.append(item.juvenile_id)
    #
    #     juveniles = models.Juvenile.objects.filter(pk__in=juveniles_id).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=2)
    #     if user_code == 1:
    #         juveniles = models.Juvenile.objects.filter(pk__in=juveniles_id)
    #
    #     return juveniles.distinct()



    # def search_birth_region(self, queryset, name, value):
    #     user_markaz = self.request.user.markaz
    #
    #     personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_district__region_id=value)
    #
    #     juveniles_ids = []
    #
    #
    #     for item in personal_infos:
    #         juveniles_ids.append(item.juvenile_id)
    #
    #     juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=2)
    #
    #
    #     filtered_juveniles = []
    #     for item in juveniles:
    #         if item not in filtered_juveniles:
    #             filtered_juveniles.append(item)
    #
    #     juvenile_ids = []
    #     for item in filtered_juveniles:
    #         juvenile_ids.append(item.id)
    #
    #     juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)
    #
    #
    #     return juveniles

    # def search_birth_district(self, queryset, name, value):
    #     user_markaz = self.request.user.markaz
    #
    #     personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_district_id=value)
    #
    #     juveniles_ids = []
    #
    #
    #     for item in personal_infos:
    #         juveniles_ids.append(item.juvenile_id)
    #
    #     juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=2)
    #
    #
    #     filtered_juveniles = []
    #     for item in juveniles:
    #         if item not in filtered_juveniles:
    #             filtered_juveniles.append(item)
    #
    #     juvenile_ids = []
    #     for item in filtered_juveniles:
    #         juvenile_ids.append(item.id)
    #
    #     juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)
    #
    #
    #     return juveniles

    # def search_birth_date(self, queryset, name, value):
    #     user_markaz = self.request.user.markaz
    #
    #     personal_infos = models.PersonalInfoJuvenile.objects.filter(birth_date=value)
    #
    #     juveniles_ids = []
    #
    #
    #     for item in personal_infos:
    #         juveniles_ids.append(item.juvenile_id)
    #
    #     juveniles = models.Juvenile.objects.filter(pk__in=juveniles_ids).filter(juvenile_markaz__markaz=user_markaz).filter(juvenile_markaz__status=2)
    #
    #
    #     filtered_juveniles = []
    #     for item in juveniles:
    #         if item not in filtered_juveniles:
    #             filtered_juveniles.append(item)
    #
    #     juvenile_ids = []
    #     for item in filtered_juveniles:
    #         juvenile_ids.append(item.id)
    #
    #     juveniles = models.Juvenile.objects.filter(pk__in=juvenile_ids)
    #
    #
    #     return juveniles


# Taqsimlangan bolalar filter
class JuvenileExpelledFilter(filters.FilterSet):
    full_name = filters.CharFilter(method='search_by_full_name')
    birth_date = filters.DateFilter(method='search_birth_date')
    birth_region = filters.CharFilter(method='search_birth_region')
    birth_district = filters.CharFilter(method='search_birth_district')



    ######

    ######
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
    markaz_id = filters.CharFilter(method='search_by_markaz')


    class Meta:
        model = models.Juvenile_Markaz
        fields = []
        # fields = ['address_region']

    def search_by_full_name(self, queryset, name, value):
        print(99098)
        user_markaz = self.request.user.markaz
        markaz_tuman = self.request.user.markaz_tuman

        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]

        if user_code == 4:
            if self.request.GET.get('status') and int(self.request.GET.get('status')) == 14:
                return models.UnidentifiedJuvenile.objects.none()
            for term in value.split():
                queryset = queryset.filter(Q(juvenile__juvenile__first_name__icontains = term) |
                                            Q(juvenile__juvenile__last_name__icontains = term) |
                                            Q(juvenile__juvenile__father_name__icontains = term)).filter(monitoring_markaz_tuman=markaz_tuman)

        elif user_code == 1:
            print('VAA',value)
            for term in value.split():
                if self.request.GET.get('status') and int(self.request.GET.get('status')) == 14:
                    queryset = queryset.filter(Q(first_name__icontains = term) |
                                                Q(last_name__icontains = term) |
                                                Q(father_name__icontains = term))
                else:
                    queryset = queryset.filter(Q(juvenile__juvenile__first_name__icontains = term) |
                                                Q(juvenile__juvenile__last_name__icontains = term) |
                                                Q(juvenile__juvenile__father_name__icontains = term))
        else:

            for term in value.split():
                if self.request.GET.get('status') and int(self.request.GET.get('status')) == 14:
                    queryset = queryset.filter(Q(first_name__icontains = term) |
                                                Q(last_name__icontains = term) |
                                                Q(father_name__icontains = term)).filter(markaz=user_markaz)

                else:
                    queryset = queryset.filter(Q(juvenile__juvenile__first_name__icontains = term) |
                                            Q(juvenile__juvenile__last_name__icontains = term) |
                                            Q(juvenile__juvenile__father_name__icontains = term)).filter(markaz=user_markaz)
        return queryset

    def search_address_region(self, queryset, name, value):
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]

        user_markaz = self.request.user.markaz
        markaz_tuman = self.request.user.markaz_tuman

        if user_code == 1:
            if self.request.GET.get('status') and int(self.request.GET.get('status')) == 14:
                # return models.UnidentifiedJuvenile.objects.all()
                return queryset
            juveniles = queryset.filter(juvenile__addressinfojuvenile__address_mahalla__district_id__region_id__id = value)
        elif user_code == 4:
            if self.request.GET.get('status') and int(self.request.GET.get('status')) == 14:
                # return models.UnidentifiedJuvenile.objects.none()
                return queryset
            print(9007)
            juveniles = queryset.filter(juvenile__addressinfojuvenile__address_mahalla__district_id__region_id__id = value).filter(monitoring_markaz_tuman=markaz_tuman)
        else:
            if self.request.GET.get('status') and int(self.request.GET.get('status')) == 14:
                # return models.UnidentifiedJuvenile.objects.filter(markaz=user_markaz)
                return queryset

            juveniles = queryset.filter(juvenile__addressinfojuvenile__address_mahalla__district_id__region_id__id = value).filter(markaz = user_markaz)

        return juveniles

    def filter_by_status(self, queryset, name, value):
        print('90008',value)
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]

        user_markaz = self.request.user.markaz
        markaz_tuman = self.request.user.markaz_tuman

        if user_code == 1:

            if int(value) > 16:
                psychology_conditions = models.PsychologyCondition.objects.all().order_by('-created_at')
                return queryset.filter(distributed_info__psychology_condition_id = psychology_conditions[int(value)-17])

            if int(value) == 14:
                return models.UnidentifiedJuvenile.objects.all()

            if int(value) == 15:
                come_2_times_juveniles_values =  queryset.values('juvenile', 'markaz').annotate(
                markaz_count=Count('id')).filter(markaz_count__gte = 2).distinct()
                come_2_times_juveniles = queryset.filter(
                    juvenile__in=come_2_times_juveniles_values.values('juvenile'),
                    markaz__in=come_2_times_juveniles_values.values('markaz'))
                return come_2_times_juveniles

            if int(value) == 16:
                return queryset.filter(status__in=['1','2','10'])

            return queryset.filter(status=value)


        elif user_code == 4:
            markaz_tuman = self.request.user.markaz_tuman

            if int(value) > 16:
                psychology_conditions = models.PsychologyCondition.objects.all().order_by('-created_at')
                return queryset.filter(distributed_info__psychology_condition_id = psychology_conditions[int(value)-17])

            if int(value) == 14:
                return models.UnidentifiedJuvenile.objects.none()

            if int(value) == 15:
                come_2_times_juveniles_values = queryset.values('juvenile', 'markaz').annotate(
                    markaz_count=Count('id')).filter(markaz_count__gte=2,monitoring_markaz_tuman=markaz_tuman).distinct()
                come_2_times_juveniles = queryset.filter(
                    juvenile__in=come_2_times_juveniles_values.values('juvenile'),
                    markaz__in=come_2_times_juveniles_values.values('markaz') )
                return come_2_times_juveniles

            if int(value) == 16:
                return queryset.filter(monitoring_markaz_tuman=markaz_tuman).filter(status__in=['1','2','10']).distinct()
            return queryset.filter(status=value).filter(monitoring_markaz_tuman=markaz_tuman)



        else:
            if int(value) > 16:
                psychology_conditions = models.PsychologyCondition.objects.all().order_by('-created_at')
                return queryset.filter(distributed_info__psychology_condition_id = psychology_conditions[int(value)-17])

            if int(value) == 14:
                return models.UnidentifiedJuvenile.objects.filter(markaz=user_markaz)
            if int(value) == 15:
                come_2_times_juveniles_values = queryset.values('juvenile', 'markaz').annotate(
                    markaz_count=Count('id')).filter(markaz_count__gte=2,markaz=user_markaz).distinct()

                come_2_times_juveniles = queryset.filter(
                    juvenile__in=come_2_times_juveniles_values.values('juvenile'),
                    markaz__in=come_2_times_juveniles_values.values('markaz') )
                return come_2_times_juveniles

            if int(value) == 16:
                return queryset.filter(markaz=user_markaz,status__in=['1', '2', '10']).distinct()

            return queryset.filter(status=value).filter(markaz=user_markaz)

    def search_education_type(self, queryset, name, value):

        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]

        user_markaz = self.request.user.markaz
        markaz_tuman = self.request.user.markaz_tuman

        if user_code == 4:
            if self.request.GET.get('status') and int(self.request.GET.get('status')) == 14:
                # return models.UnidentifiedJuvenile.objects.none()
                return queryset

            juveniles = queryset.filter(juvenile__educationinfojuvenile__school_type=value).filter(monitoring_markaz_tuman=markaz_tuman)


        elif user_code == 1:
            if self.request.GET.get('status') and int(self.request.GET.get('status')) == 14:
                # return models.UnidentifiedJuvenile.objects.all()
                return queryset

            juveniles = queryset.filter(juvenile__educationinfojuvenile__school_type=value)


        else:
            if self.request.GET.get('status') and int(self.request.GET.get('status')) == 14:
                # return models.UnidentifiedJuvenile.objects.filter(markaz=user_markaz)
                return queryset

            juveniles = queryset.filter(juvenile__educationinfojuvenile__school_type=value).filter(
                markaz=user_markaz)

        return juveniles

    def search_by_markaz(self, queryset, name, value):
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]
        print("JORABEK")
        if user_code == 1:
            if self.request.GET.get('status') and int(self.request.GET.get('status')) == 14:
                # return models.UnidentifiedJuvenile.objects.all()
                return queryset
            return queryset.filter(markaz = value)




