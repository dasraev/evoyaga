from datetime import datetime
from rest_framework import serializers

import info.models
from juvenile import models
from info import models as info_db
from rest_framework.response import Response
from django.db.models import Q,Count,Sum
from collections import Counter
from datetime import datetime,timedelta


def get_juvenile_markaz(date_from = None, date_to = None, markaz_id = None):
    last_year = int(format(datetime.now(), '%Y'))
    juvenile_markaz = models.Juvenile_Markaz.objects.filter(
        status__in=['2','3','4','5','6','7','8','9','10','11','12','13'] )
    if date_from and date_to:
        print(date_to,date_from)
        juvenile_markaz = juvenile_markaz.filter(accept_center_info__arrived_date__range=[date_from, date_to])
        print(juvenile_markaz.only('id').query)
    if date_from == None and date_to == None:
        juvenile_markaz = juvenile_markaz.filter(accept_center_info__arrived_date__year=last_year)
    if markaz_id:
        juvenile_markaz = juvenile_markaz.filter(markaz=markaz_id)
    return juvenile_markaz

# Dashboard card statistics
class DashboardCardStatisticsSerializer(serializers.ModelSerializer):
    accepted_center_childs = serializers.SerializerMethodField()
    boys = serializers.SerializerMethodField()
    girls = serializers.SerializerMethodField()
    graduated_itm = serializers.SerializerMethodField()
    employment_guaranteed = serializers.SerializerMethodField()
    not_identified = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = [
            "accepted_center_childs",
            "boys",
            "girls",
            "graduated_itm",
            "employment_guaranteed",
            "not_identified",
        ]

    def get_accepted_center_childs(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id=user_markaz).count()


        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz).count()


        return juvenile_markaz

    def get_boys(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)


        boys = juvenile_markaz.filter(juvenile__juvenile__gender='M').distinct().count()


        return boys

    def get_girls(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        girls = juvenile_markaz.filter(juvenile__juvenile__gender='F').distinct().count()


        return girls

    def get_graduated_itm(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id=user_markaz).filter(monitoring_info__monitoring_status=2).distinct().count()

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz).filter(monitoring_info__monitoring_status=2).distinct().count()


        return juvenile_markaz

    def get_employment_guaranteed(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')


        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)



        return juvenile_markaz.filter(status='6').count()

    def get_not_identified(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
                markaz=user_markaz).filter(created_at__range=[date_from, date_to]).count()
        else:
            unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
                markaz=user_markaz).filter(created_at__year=last_year).count()

        return unidentified_juvenile


# Dashboard Reason for bringing statistics
# Markazga olib kelish sababi


class ReasonBringingStatisticsSerializer(serializers.ModelSerializer):
    unsupervised_child = serializers.SerializerMethodField()
    neglected_child = serializers.SerializerMethodField()
    needs_state_public_support = serializers.SerializerMethodField()
    dangerous_social_situation = serializers.SerializerMethodField()
    missing_and_wanted = serializers.SerializerMethodField()
    difficult_upbringing = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = [
            "unsupervised_child",
            "neglected_child",
            "needs_state_public_support",
            "dangerous_social_situation",
            "missing_and_wanted",
            "difficult_upbringing",
        ]

    def get_unsupervised_child(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id=user_markaz)


        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)
        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order = 1).distinct().count()


    def get_neglected_child(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to,markaz_id=user_markaz)



        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order=2).distinct().count()


    def get_needs_state_public_support(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)



        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order=3).distinct().count()

    def get_dangerous_social_situation(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)



        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order=4).distinct().count()

    def get_missing_and_wanted(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)



        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order=6).distinct().count()

    def get_difficult_upbringing(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)



        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order=5).distinct().count()


# Dashboard Educational institution for children admitted to the center statistics
# Markazga qabul qilingan bolalarning o‘qish muasassasi statistikasi
class EducationTypeStatisticsSerializer(serializers.ModelSerializer):
    kindergarten = serializers.SerializerMethodField()
    school = serializers.SerializerMethodField()
    vocational_school = serializers.SerializerMethodField()
    vocational_college = serializers.SerializerMethodField()
    litsey = serializers.SerializerMethodField()
    texnikum = serializers.SerializerMethodField()
    special_education = serializers.SerializerMethodField()
    otm = serializers.SerializerMethodField()
    working = serializers.SerializerMethodField()
    not_study_not_working = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = [
            "kindergarten",
            "school",
            "vocational_school",
            "vocational_college",
            "litsey",
            "texnikum",
            "special_education",
            "otm",
            "working",
            "not_study_not_working",
        ]

    def get_kindergarten(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)


        kindergarten = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=1).distinct().count()



        return kindergarten
    def get_school(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        school = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=2).distinct().count()

        return school

    def get_vocational_school(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        vocational_school = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=3).distinct().count()

        return vocational_school

    def get_vocational_college(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        vocational_college = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=4).distinct().count()

        return vocational_college

    def get_litsey(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        litsey = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=5).distinct().count()

        return litsey

    def get_texnikum(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        texnikum = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=6).distinct().count()


        return texnikum

    def get_special_education(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        special_education = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=7).distinct().count()

        return special_education

    def get_otm(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        otm = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=8).distinct().count()

        return otm


    def get_working(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        working = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=10).distinct().count()


        return working

    def get_not_study_not_working(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)

        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        not_study_not_working = juvenile_markaz.filter(Q(juvenile__educationinfojuvenile__school_type=9)|Q(juvenile__juvenile__passport_type=5)).distinct().count()

        return not_study_not_working


def get_distribution_type_statistics(request, date_from, date_to, field_type, field_value):
    user_markaz = request.user.markaz
    result = 0
    last_year = int(format(datetime.now(), '%Y'))

    if date_from and date_to:
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['3','4','5','6','7','8','9','11','12','13']).filter(markaz=user_markaz,accept_center_info__arrived_date__range=[date_from,date_to])

    else:
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['3','4','5','6','7','8','9','11','12','13']).filter(markaz=user_markaz,accept_center_info__arrived_date__year=last_year)



    if field_type == 'distribution_type':
        distribution_stat_num = juvenile_markaz.filter(distributed_info__distribution_type=field_value).distinct().count()
    elif field_type == 'type_guardianship':
        distribution_stat_num = juvenile_markaz.filter(distributed_info__type_guardianship=field_value).distinct().count()
    return distribution_stat_num



# Kimlarga topshirildi statistikasi
# Distribution type statistikasi
class DistributionTypeStatisticsSerializer(serializers.ModelSerializer):
    to_parents = serializers.SerializerMethodField()
    to_rotm = serializers.SerializerMethodField()
    to_orphanages = serializers.SerializerMethodField()
    to_family_orphanages = serializers.SerializerMethodField()
    to_sos = serializers.SerializerMethodField()
    to_guardianship = serializers.SerializerMethodField()
    to_healthcare = serializers.SerializerMethodField()
    to_other_center = serializers.SerializerMethodField()
    to_other_country = serializers.SerializerMethodField()
    to_itm = serializers.SerializerMethodField()


    class Meta:
        model = models.Juvenile
        fields = [
            "to_parents",
            "to_rotm",
            "to_orphanages",
            "to_family_orphanages",
            "to_sos",
            "to_guardianship",
            "to_healthcare",
            "to_other_center",
            "to_other_country",
            "to_itm",

        ]

    def get_to_parents(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        to_parents = get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 1)
        to_others = get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 8)

        return to_parents + to_others

    def get_to_rotm(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        return get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 4)

    def get_to_orphanages(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        return get_distribution_type_statistics(request, date_from, date_to, 'type_guardianship', 5)

    def get_to_family_orphanages(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        return get_distribution_type_statistics(request, date_from, date_to, 'type_guardianship', 6)

    def get_to_sos(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        return get_distribution_type_statistics(request, date_from, date_to, 'type_guardianship', 7)

    def get_to_itm(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        return get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 3)



    def get_to_guardianship(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        vasiylik = get_distribution_type_statistics(request, date_from, date_to, 'type_guardianship', 1)
        homiylik = get_distribution_type_statistics(request, date_from, date_to, 'type_guardianship', 2)

        return vasiylik + homiylik

    def get_to_healthcare(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        return get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 5)

    def get_to_other_center(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        #

        #
        user_markaz = request.user.markaz
        last_year = int(format(datetime.now(), '%Y'))

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13']).filter(markaz_id=user_markaz,status='8',
                                                                                         accept_center_info__arrived_date__range=[date_from,
                                                                                                            date_to])


        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13']).filter(markaz_id=user_markaz,
                                                                                         status='8',
                                                                                         accept_center_info__arrived_date__year=last_year)
        return juvenile_markaz.count()



    def get_to_other_country(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        return get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 7)


# apparat distribution type statistics function
def get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, field_type, field_value):
    last_year = int(format(datetime.now(), '%Y'))

    if markaz_id:
        if markaz_id == '':
            markaz_id = None

        try:
            info_db.Markaz.objects.get(pk=markaz_id)
        except:
            raise serializers.ValidationError(
                {'message': 'markaz_id is not valid!'})
    if date_from and date_to and markaz_id:
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['3','4','5','6','7','8','9','11','12','13']).filter(markaz=markaz_id,accept_center_info__arrived_date__range=[date_from,date_to])


    elif date_from and date_to:
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13']).filter(accept_center_info__arrived_date__range=[date_from,
                                                                                                        date_to])


    elif markaz_id:
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13']).filter(markaz = markaz_id,accept_center_info__arrived_date__year=last_year)
    else:
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13']).filter(accept_center_info__arrived_date__year=last_year)

    if field_type == 'distribution_type':
        distribution_stat_num = juvenile_markaz.filter(distributed_info__distribution_type=field_value).distinct().count()
    elif field_type == 'type_guardianship':
        distribution_stat_num = juvenile_markaz.filter(distributed_info__type_guardianship=field_value).distinct().count()
    return distribution_stat_num



# Apparat Kimlarga topshirildi statistikasi
# Apparat Distribution type statistikasi
class ApparatDistributionTypeStatisticsSerializer(serializers.ModelSerializer):
    to_parents = serializers.SerializerMethodField()
    to_rotm = serializers.SerializerMethodField()
    to_orphanages = serializers.SerializerMethodField()
    to_family_orphanages = serializers.SerializerMethodField()
    to_sos = serializers.SerializerMethodField()
    to_guardianship = serializers.SerializerMethodField()
    to_healthcare = serializers.SerializerMethodField()
    to_other_center = serializers.SerializerMethodField()
    to_other_country = serializers.SerializerMethodField()
    to_itm = serializers.SerializerMethodField()
    class Meta:
        model = models.Juvenile
        fields = [
            "to_parents",
            "to_rotm",
            "to_orphanages",
            "to_family_orphanages",
            "to_sos",
            "to_guardianship",
            "to_healthcare",
            "to_other_center",
            "to_other_country",
            "to_itm"
        ]

    def get_to_parents(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        to_parents = get_apparat_distribution_type_statistics(
            markaz_id, date_from, date_to, 'distribution_type', 1)
        to_others = get_apparat_distribution_type_statistics(
            markaz_id, date_from, date_to, 'distribution_type', 8)

        return to_parents + to_others

    def get_to_rotm(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'distribution_type', 4)

    def get_to_orphanages(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'type_guardianship', 5)

    def get_to_family_orphanages(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'type_guardianship', 6)

    def get_to_sos(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'type_guardianship', 7)

    def get_to_guardianship(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        vasiylik = get_apparat_distribution_type_statistics(
            markaz_id, date_from, date_to, 'type_guardianship', 1)
        homiylik = get_apparat_distribution_type_statistics(
            markaz_id, date_from, date_to, 'type_guardianship', 2)

        return vasiylik + homiylik

    def get_to_healthcare(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'distribution_type', 5)

    def get_to_other_center(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        #

        #
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13']).filter(accept_center_info__arrived_date__range=[date_from,
                                                                                                            date_to],status='8')


        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13']).filter(accept_center_info__arrived_date__year=last_year,
                                                                                         status='8')
        return juvenile_markaz.distinct().count()


    def get_to_other_country(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'distribution_type', 7)
    def get_to_itm(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'distribution_type', 3)


class ComeMore2TimesStatisticsSerializer(serializers.ModelSerializer):
    all_juveniles = serializers.SerializerMethodField()
    boys = serializers.SerializerMethodField()
    girls = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = [
            "all_juveniles",
            "boys",
            "girls",
        ]

    def get_all_juveniles(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
#.values('juvenile','markaz').annotate(markaz_count=Count('id')).filter(markaz_count=2)
        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id=user_markaz)


        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)



        return juvenile_markaz.values('juvenile','markaz').annotate(markaz_count=Count('id')).filter(markaz_count__gt=1).count()

    def get_boys(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)


        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        return juvenile_markaz.filter(juvenile__juvenile__gender='M').values('juvenile', 'markaz').annotate(markaz_count=Count('id')).filter(markaz_count__gt=1).count()

    def get_girls(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=user_markaz)


        else:
            juvenile_markaz = get_juvenile_markaz(markaz_id=user_markaz)

        return juvenile_markaz.filter(juvenile__juvenile__gender='F').values('juvenile', 'markaz').annotate(
            markaz_count=Count('id')).filter(markaz_count__gt=1).count()


class InCenterNowStatisticsSerializer(serializers.ModelSerializer):
    all_juveniles = serializers.SerializerMethodField()
    boys = serializers.SerializerMethodField()
    girls = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = [
            "all_juveniles",
            "boys",
            "girls",
        ]

    def get_all_juveniles(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:

            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,status__in=['2','10'],accept_center_info__arrived_date__range=[date_from, date_to])


        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz, status__in=['2','10'],
                                                                    accept_center_info__arrived_date__year=last_year)


        return juvenile_markaz.distinct().count()

    def get_boys(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz, status__in=['2','10'],
                                                                    accept_center_info__arrived_date__range=[date_from, date_to])
            return juvenile_markaz.filter(juvenile__juvenile__gender='M').distinct().count()

        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz, status__in=['2','10'],
                                                                    accept_center_info__arrived_date__year=last_year)
            return juvenile_markaz.filter(juvenile__juvenile__gender='M').distinct().count()

    def get_girls(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz, status__in=['2','10'],
                                                                    accept_center_info__arrived_date__range=[date_from, date_to])
            return juvenile_markaz.filter(juvenile__juvenile__gender='F').distinct().count()

        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz, status__in=['2','10'],
                                                                    accept_center_info__arrived_date__year=last_year)
            return juvenile_markaz.filter(juvenile__juvenile__gender='F').distinct().count()


# Apparat Dashboard card statistics
class ApparatDashboardCardStatisticsSerializer(serializers.ModelSerializer):
    accepted_center_childs_per_region = serializers.SerializerMethodField()
    accepted_center_childs = serializers.SerializerMethodField()
    boys = serializers.SerializerMethodField()
    girls = serializers.SerializerMethodField()
    graduated_itm = serializers.SerializerMethodField()
    employment_guaranteed = serializers.SerializerMethodField()
    not_identified = serializers.SerializerMethodField()


    class Meta:
        model = models.Juvenile
        fields = [
            "accepted_center_childs_per_region",
            "accepted_center_childs",
            "boys",
            "girls",
            "graduated_itm",
            "employment_guaranteed",
            "not_identified",
        ]

    def get_accepted_center_childs_per_region(self,obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')
        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})


        if date_from and date_to and markaz_id:
            data={}
            regions = info.models.Region.objects.all()
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)
            for region in regions:
                data[region.name] = juvenile_markaz.filter(markaz__region = region).count()


        elif date_from and date_to:

            data = {}
            regions = info.models.Region.objects.all()
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            for region in regions:
                data[region.name] = juvenile_markaz.filter(markaz__region=region).count()
        elif markaz_id:
            data = {}
            regions = info.models.Region.objects.all()
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            for region in regions:
                data[region.name] = juvenile_markaz.filter(markaz__region=region).count()
        else:
            data = {}
            regions = info.models.Region.objects.all()
            juvenile_markaz = get_juvenile_markaz()
            for region in regions:
                data[region.name] = juvenile_markaz.filter(markaz__region=region).count()
        return data
    def get_accepted_center_childs(self, obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')
        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:

            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id).count()



        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to).count()

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id).count()


        else:
            juvenile_markaz = get_juvenile_markaz().count()

        return juvenile_markaz

    def get_boys(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError(
                    {'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)


        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        boys = juvenile_markaz.filter(juvenile__juvenile__gender='M').distinct().count()

        return boys

    def get_girls(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError(
                    {'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

        else:
            juvenile_markaz = get_juvenile_markaz()

        girls = juvenile_markaz.filter(juvenile__juvenile__gender='F').distinct().count()

        return girls

    def get_graduated_itm(self, obj):
        request = self.context.get('request')
        markaz_id = request.GET.get('markaz_id')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id).filter(
                monitoring_info__monitoring_status=2).distinct().count()

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to).filter(
                monitoring_info__monitoring_status=2).distinct().count()
        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id).filter(
                monitoring_info__monitoring_status=2).distinct().count()
        else:
            juvenile_markaz = get_juvenile_markaz().filter(
                monitoring_info__monitoring_status=2).distinct().count()
        return juvenile_markaz

    def get_employment_guaranteed(self, obj):
        request = self.context.get('request')
        markaz_id = request.GET.get('markaz_id')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
        else:
            juvenile_markaz = get_juvenile_markaz()


        return juvenile_markaz.filter(status='6').count()



    def get_not_identified(self, obj):
        request = self.context.get('request')
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
                markaz=markaz_id).filter(created_at__range=[date_from, date_to]).count()
        elif date_from and date_to:
            unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
                created_at__range=[date_from, date_to]).count()

        elif markaz_id:
            unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
                markaz=markaz_id).filter(created_at__year=last_year).count()
        else:
            unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(created_at__year=last_year).count()

        return unidentified_juvenile


# Apparat Dashboard Reason for bringing statistics
# Apparat Markazga olib kelish sababi statistikasi

# class ApparatReasonBringingStatisticsSerializer2(serializers.ModelSerializer):
# =======

#
# class ApparatReasonBringingStatisticsSerializer(serializers.ModelSerializer):
#     unsupervised_child = serializers.IntegerField()
#     neglected_child = serializers.IntegerField()
#     needs_state_public_support = serializers.IntegerField()
#     dangerous_social_situation = serializers.IntegerField()
#     missing_and_wanted = serializers.IntegerField()
#     difficult_upbringing = serializers.IntegerField()
#
#     class Meta:
#         model = models.Juvenile
#         fields = [
#             "unsupervised_child",
#             "neglected_child",
#             "needs_state_public_support",
#             "dangerous_social_situation",
#             "missing_and_wanted",
#             "difficult_upbringing",
#         ]
#
#     def get_queryset(self, request):
#         last_year = int(format(datetime.now(), '%Y'))
#         date_from = request.GET.get('date_from')
#         date_to = request.GET.get('date_to')
#     time_date_to = datetime.strptime(date_to,'%Y-%m-%d').date()
#     date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
#         markaz_id = request.GET.get('markaz_id')
#
#         if markaz_id == '':
#             markaz_id = None
#
#         queryset = models.Juvenile_Markaz.objects.filter(created_at__year=last_year)
#
#         if date_from and date_to:
#             queryset = queryset.filter(created_at__range=[date_from, date_to])
#
#         if markaz_id:
#             try:
#                 info_db.Markaz.objects.get(pk=markaz_id)
#                 queryset = queryset.filter(markaz=markaz_id)
#
#             except info_db.Markaz.DoesNotExist:
#                 raise serializers.ValidationError({'message': 'markaz_id is not valid!'})
#
#         return queryset
#
#     def get_unsupervised_child(sel):
#         return models.JuvenileAcceptCenterInfo.objects.filter().filter(sub_reason_bringing_child__parent=1).count()
#
#     def get_neglected_child(self, obj):
#         return obj.juvenile_markaz.filter(
#             accept_center_info__sub_reason_bringing_child__parent=2).count()
#
#     def get_needs_state_public_support(self, obj):
#         return obj.juvenile_markaz.filter(
#             accept_center_info__sub_reason_bringing_child__parent=3).count()
#
#     def get_dangerous_social_situation(self, obj):
#         return obj.juvenile_markaz.filter(
#             accept_center_info__sub_reason_bringing_child__parent=4).count()
#
#     def get_missing_and_wanted(self, obj):
#         return obj.juvenile_markaz.filter(
#             accept_center_info__sub_reason_bringing_child__parent=6).count()
#
#     def get_difficult_upbringing(self, obj):
#         return obj.juvenile_markaz.filter(
#             accept_center_info__sub_reason_bringing_child__parent=5).count()


class ApparatReasonBringingStatisticsSerializer(serializers.ModelSerializer):
    unsupervised_child = serializers.SerializerMethodField()
    neglected_child = serializers.SerializerMethodField()
    needs_state_public_support = serializers.SerializerMethodField()
    dangerous_social_situation = serializers.SerializerMethodField()
    missing_and_wanted = serializers.SerializerMethodField()
    difficult_upbringing = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = [
            "unsupervised_child",
            "neglected_child",
            "needs_state_public_support",
            "dangerous_social_situation",
            "missing_and_wanted",
            "difficult_upbringing",
        ]

    def get_unsupervised_child(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError(
                    {'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)


        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order = 1).distinct().count()


    def get_neglected_child(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)


        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order=2).distinct().count()

    def get_needs_state_public_support(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)


        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order=3).distinct().count()

    def get_dangerous_social_situation(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)


        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order=4).distinct().count()

    def get_missing_and_wanted(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)


        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order=6).distinct().count()

    def get_difficult_upbringing(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)


        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        return juvenile_markaz.filter(accept_center_info__sub_reason_bringing_child__parent__order=5).distinct().count()


# Apparat in center now statistics serializer
class ApparatInCenterNowStatisticsSerializer(serializers.ModelSerializer):
    all_juveniles = serializers.SerializerMethodField()
    boys = serializers.SerializerMethodField()
    girls = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = [
            "all_juveniles",
            "boys",
            "girls",
        ]

    def get_all_juveniles(self, obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],markaz = markaz_id,accept_center_info__arrived_date__range=[date_from,date_to])

        elif date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],
                                                                    accept_center_info__arrived_date__range=[date_from, date_to])


        elif markaz_id:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'], markaz=markaz_id,
                                                                    accept_center_info__arrived_date__year=last_year)


        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],
                                                                    accept_center_info__arrived_date__year=last_year)
        return juvenile_markaz.count()
    def get_boys(self, obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'], markaz=markaz_id,
                                                                    accept_center_info__arrived_date__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],
                                                                    accept_center_info__arrived_date__range=[date_from, date_to])


        elif markaz_id:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'], markaz=markaz_id,
                                                                    accept_center_info__arrived_date__year=last_year)


        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],
                                                                    accept_center_info__arrived_date__year=last_year)

        return juvenile_markaz.filter(juvenile__juvenile__gender='M').distinct().count()

    def get_girls(self, obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'], markaz=markaz_id,
                                                                    accept_center_info__arrived_date__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],
                                                                    accept_center_info__arrived_date__range=[date_from, date_to])


        elif markaz_id:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'], markaz=markaz_id,
                                                                    accept_center_info__arrived_date__year=last_year)


        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],
                                                                    accept_center_info__arrived_date__year=last_year)

        return juvenile_markaz.filter(juvenile__juvenile__gender='F').distinct().count()


# Apparat come more 2 times statistics
class ApparatComeMore2TimesStatisticsSerializer(serializers.ModelSerializer):
    all_juveniles = serializers.SerializerMethodField()
    boys = serializers.SerializerMethodField()
    girls = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = [
            "all_juveniles",
            "boys",
            "girls",
        ]

    def get_all_juveniles(self, obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        return juvenile_markaz.values('juvenile','markaz').annotate(markaz_count=Count('id')).filter(markaz_count__gt=1).count()

    def get_boys(self, obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError(
                    {'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        return juvenile_markaz.filter(juvenile__juvenile__gender='M').values('juvenile', 'markaz').annotate(markaz_count=Count('id')).filter(markaz_count__gt=1).count()

    def get_girls(self, obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        return juvenile_markaz.filter(juvenile__juvenile__gender='F').values('juvenile', 'markaz').annotate(
            markaz_count=Count('id')).filter(markaz_count__gt=1).count()


# Apparat Dashboard Educational institution for children admitted to the center statistics
# Apparat Markazga qabul qilingan bolalarning o‘qish muasassasi statistikasi

class ApparatReasonBringingStatisticsSerializer2(serializers.ModelSerializer):
    fields_mapping = {
        "unsupervised_child": 1,
        "neglected_child": 2,
        "needs_state_public_support": 3,
        "dangerous_social_situation": 4,
        "missing_and_wanted": 6,
        "difficult_upbringing": 5,
    }

    class Meta:
        model = models.Juvenile
        fields = ['unsupervised_child', "neglected_child", "needs_state_public_support",
                  "dangerous_social_situation", "missing_and_wanted", "difficult_upbringing"]

    def get_field_count(self, obj, field_name, request):
        result = 0
        last_year = int(format(datetime.now(), '%Y'))
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError(
                    {'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=markaz_id).filter(accept_center_info__arrived_date__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                accept_center_info__arrived_date__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=markaz_id).filter(accept_center_info__arrived_date__year=last_year)

        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                accept_center_info__arrived_date__year=last_year)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                field_parent = self.fields_mapping.get(field_name)
                if field_parent is not None:
                    count = models.JuvenileAcceptCenterInfo.objects.filter(
                        pk=accept_center_info).filter(sub_reason_bringing_child__parent=field_parent).count()
                    result += count
        return result

    def get_unsupervised_child(self, obj):
        return self.get_field_count(obj, "unsupervised_child", self.context.get('request'))

    def get_neglected_child(self, obj):
        return self.get_field_count(obj, "neglected_child", self.context.get('request'))

    def get_needs_state_public_support(self, obj):
        return self.get_field_count(obj, "needs_state_public_support", self.context.get('request'))

    def get_dangerous_social_situation(self, obj):
        return self.get_field_count(obj, "dangerous_social_situation", self.context.get('request'))

    def get_missing_and_wanted(self, obj):
        return self.get_field_count(obj, "missing_and_wanted", self.context.get('request'))

    def get_difficult_upbringing(self, obj):
        return self.get_field_count(obj, "difficult_upbringing", self.context.get('request'))


class ApparatEducationTypeStatisticsSerializer(serializers.ModelSerializer):
    kindergarten = serializers.SerializerMethodField()
    school = serializers.SerializerMethodField()
    vocational_school = serializers.SerializerMethodField()
    vocational_college = serializers.SerializerMethodField()
    litsey = serializers.SerializerMethodField()
    texnikum = serializers.SerializerMethodField()
    special_education = serializers.SerializerMethodField()
    otm = serializers.SerializerMethodField()
    working = serializers.SerializerMethodField()
    not_study_not_working = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = [
            "kindergarten",
            "school",
            "vocational_school",
            "vocational_college",
            "litsey",
            "texnikum",
            "special_education",
            "otm",
            "working",
            "not_study_not_working",
        ]

    def get_kindergarten(self, obj):
        request = self.context.get('request')


        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError(
                    {'message': 'markaz_id is not valid!'})


        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

        else:
            juvenile_markaz = get_juvenile_markaz()

        kindergarten = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=1).distinct().count()

        return kindergarten
    def get_school(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError(
                    {'message': 'markaz_id is not valid!'})
        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

        else:
            juvenile_markaz = get_juvenile_markaz()

        school = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=2).distinct().count()

        return school
    def get_vocational_school(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

        else:
            juvenile_markaz = get_juvenile_markaz()

        vocational_school = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=3).distinct().count()

        return vocational_school
    def get_vocational_college(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None
        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

        else:
            juvenile_markaz = get_juvenile_markaz()

        vocational_college = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=4).distinct().count()

        return vocational_college
    def get_litsey(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError(
                    {'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

        else:
            juvenile_markaz = get_juvenile_markaz()

        litsey = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=5).distinct().count()

        return litsey
    def get_texnikum(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

        else:
            juvenile_markaz = get_juvenile_markaz()

        texnikum = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=6).distinct().count()

        return texnikum
    def get_special_education(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

        else:
            juvenile_markaz = get_juvenile_markaz()

        special_education = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=7).distinct().count()

        return special_education

    def get_otm(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

        else:
            juvenile_markaz = get_juvenile_markaz()

        otm = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=8).distinct().count()

        return otm
    def get_working(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

        else:
            juvenile_markaz = get_juvenile_markaz()

        working = juvenile_markaz.filter(juvenile__educationinfojuvenile__school_type=10).distinct().count()

        return working
    def get_not_study_not_working(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to, markaz_id=markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

        else:
            juvenile_markaz = get_juvenile_markaz()

        not_study_not_working = juvenile_markaz.filter(
            Q(juvenile__educationinfojuvenile__school_type=9)|Q(juvenile__juvenile__passport_type=5)).distinct().count()

        return not_study_not_working


class ApparatMapStatisticsSerializer(serializers.ModelSerializer):
    accepted_center_childs_per_region = serializers.SerializerMethodField()
    class Meta:
        model = models.Juvenile
        fields = [
            "accepted_center_childs_per_region",
        ]

    def get_accepted_center_childs_per_region(self,obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
        markaz_id = request.GET.get('markaz_id')
        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})


        if date_from and date_to and markaz_id:
            data={}
            regions = info.models.Region.objects.all()
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)
            for region in regions:
                data[region.name] = juvenile_markaz.filter(markaz__region = region).count()


        elif date_from and date_to:

            data = {}
            regions = info.models.Region.objects.all()
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            for region in regions:
                data[region.name] = juvenile_markaz.filter(markaz__region=region).count()
        elif markaz_id:
            data = {}
            regions = info.models.Region.objects.all()
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            for region in regions:
                data[region.name] = juvenile_markaz.filter(markaz__region=region).count()
        else:
            data = {}
            regions = info.models.Region.objects.all()
            juvenile_markaz = get_juvenile_markaz()
            for region in regions:
                data[region.name] = juvenile_markaz.filter(markaz__region=region).count()
        return data