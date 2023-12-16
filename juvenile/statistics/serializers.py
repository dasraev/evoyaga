from datetime import datetime
from rest_framework import serializers

import info.models
from juvenile import models
from info import models as info_db
from rest_framework.response import Response
from django.db.models import Q
from collections import Counter


def get_juvenile_markaz(date_from = None, date_to = None, markaz_id = None):
    last_year = int(format(datetime.now(), '%Y'))

    juvenile_markaz = models.Juvenile_Markaz.objects.filter(
        juvenile__educationinfojuvenile__isnull=False,
        juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
        juvenile__parentinfojuvenile__isnull=False).distinct()
    juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(juvenile__juvenile__passport_type='5').distinct()
    if date_from and date_to:
        juvenile_markaz = juvenile_markaz.filter(created_at__range=[date_from, date_to])
        juvenile_markaz_foreign = juvenile_markaz_foreign.filter(created_at__range=[date_from, date_to])
    if date_from == None and date_to == None:
        juvenile_markaz = juvenile_markaz.filter(created_at__year=last_year)
        juvenile_markaz_foreign = juvenile_markaz_foreign.filter(created_at__year=last_year)
    if markaz_id:
        juvenile_markaz = juvenile_markaz.filter(markaz=markaz_id)
        juvenile_markaz_foreign = juvenile_markaz_foreign.filter(markaz=markaz_id)
    # else:
    #     juvenile_markaz = juvenile_markaz.filter(created_at__year=last_year)
    #     juvenile_markaz_foreign = juvenile_markaz_foreign.filter(created_at__year=last_year)

    return juvenile_markaz | juvenile_markaz_foreign
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
        print(980,user_markaz.id)

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = (models.Juvenile_Markaz.objects.filter(markaz=user_markaz).
                                            filter(juvenile__educationinfojuvenile__isnull=False,juvenile__addressinfojuvenile__isnull=False,
                                            juvenile__juvenile__isnull=False,juvenile__parentinfojuvenile__isnull=False).
                                            filter(created_at__range=[date_from, date_to]).distinct().count())
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type = '5').filter(created_at__range=[date_from, date_to]).distinct().count()
            juvenile_markaz += juvenile_markaz_foreign
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=user_markaz,).filter(created_at__range=[date_from, date_to]).count()
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(created_at__range=[date_from, date_to]).count()
            # juvenile_markaz += unidentified_juvenile

        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz).filter(juvenile__educationinfojuvenile__isnull=False,
                                           juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                           juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct().count()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type = '5').filter(created_at__year = last_year).distinct().count()
            print(121,juvenile_markaz)
            print(221,juvenile_markaz_foreign)
            juvenile_markaz += juvenile_markaz_foreign
            print(109,juvenile_markaz)
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(created_at__year=last_year).count()
            # juvenile_markaz += unidentified_juvenile

        return juvenile_markaz

    def get_boys(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz,juvenile__educationinfojuvenile__isnull=False,
                                           juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                           juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type = '5').filter(created_at__range=[date_from, date_to]).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(gender='M').filter(created_at__range=[date_from, date_to]).count()
            # result += unidentified_juvenile
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz,juvenile__educationinfojuvenile__isnull=False,
                                           juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                           juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type = '5').filter(created_at__year = last_year).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(gender='M').filter(created_at__year=last_year).count()
            # result += unidentified_juvenile

        for item in juvenile_markaz:
            boy = models.PersonalInfoJuvenile.objects.filter(juvenile=item.juvenile).filter(gender='M').count()
            result += boy

        return result

    def get_girls(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz,juvenile__educationinfojuvenile__isnull=False,
                                           juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                           juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type = '5').filter(created_at__range=[date_from, date_to]).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(gender='M').filter(created_at__range=[date_from, date_to]).count()
            # result += unidentified_juvenile
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz,juvenile__educationinfojuvenile__isnull=False,
                                           juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                           juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type = '5').filter(created_at__year = last_year).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(gender='M').filter(created_at__year=last_year).count()
            # result += unidentified_juvenile

        for item in juvenile_markaz:
            girl = models.PersonalInfoJuvenile.objects.filter(juvenile=item.juvenile).filter(gender='F').count()
            result += girl

        return result

    def get_graduated_itm(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(created_at__range=[date_from, date_to]).filter(
                monitoring_info__monitoring_status=2).filter(markaz=user_markaz,juvenile__educationinfojuvenile__isnull=False,
                                           juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                           juvenile__parentinfojuvenile__isnull=False).distinct().count()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type = '5',monitoring_info__monitoring_status=2).filter(created_at__range = [date_from,date_to]).distinct().count()
            juvenile_markaz +=juvenile_markaz_foreign
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(created_at__year=last_year).filter(
                monitoring_info__monitoring_status=2).filter(markaz=user_markaz,juvenile__educationinfojuvenile__isnull=False,
                                           juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                           juvenile__parentinfojuvenile__isnull=False).distinct().count()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type = '5',monitoring_info__monitoring_status=2).filter(created_at__year = last_year).distinct().count()
            juvenile_markaz += juvenile_markaz_foreign


        return juvenile_markaz

    def get_employment_guaranteed(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz,juvenile__educationinfojuvenile__isnull=False,
                                           juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                           juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type = '5').filter(created_at__range = [date_from,date_to]).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz,juvenile__educationinfojuvenile__isnull=False,
                                           juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                           juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type = '5').filter(created_at__year = last_year).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        for item in juvenile_markaz:
            if item.employment_info:
                if item.employment_info.employment_file:
                    result += 1

        return result

    def get_not_identified(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

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
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                unsupervised_child = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=1).count()
                result += unsupervised_child
        return result

    def get_neglected_child(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                neglected_child = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=2).count()
                result += neglected_child
        return result

    def get_needs_state_public_support(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                needs_state_public_support = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=3).count()
                result += needs_state_public_support
        return result

    def get_dangerous_social_situation(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                dangerous_social_situation = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=4).count()
                result += dangerous_social_situation
        return result

    def get_missing_and_wanted(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                missing_and_wanted = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=6).count()
                result += missing_and_wanted
        return result

    def get_difficult_upbringing(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                difficult_upbringing = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=5).count()
                result += difficult_upbringing
        return result


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

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        kindergarten = models.EducationInfoJuvenile.objects.filter(
                juvenile__id__in=juvenile_ids,school_type=1).count()


        return kindergarten
    def get_school(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        school = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=2).count()

        return school

    def get_vocational_school(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        vocational_school = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in = juvenile_ids).filter(school_type=3).count()

        return vocational_school

    def get_vocational_college(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        vocational_college = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in = juvenile_ids).filter(school_type=4).count()


        return vocational_college

    def get_litsey(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        litsey = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=5).count()


        return litsey

    def get_texnikum(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        texnikum = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=6).count()


        return texnikum

    def get_special_education(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        print('Pod',juvenile_markaz)
        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        special_education = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=7).count()


        return special_education

    def get_otm(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        print(9008,juvenile_markaz)
        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        otm = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=8).count()


        return otm


    def get_working(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        working = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in = juvenile_ids).filter(school_type=10).count()


        return working

    def get_not_study_not_working(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        not_study_not_working = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in = juvenile_ids).filter(school_type=9).count()


        return not_study_not_working


def get_distribution_type_statistics(request, date_from, date_to, field_type, field_value):
    user_markaz = request.user.markaz
    result = 0
    last_year = int(format(datetime.now(), '%Y'))

    if date_from and date_to:
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            markaz=user_markaz,juvenile__educationinfojuvenile__isnull=False,juvenile__addressinfojuvenile__isnull=False,
                                            juvenile__juvenile__isnull=False,juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()
        juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type='5').filter(
            created_at__range=[date_from, date_to]).distinct()
        juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
    else:
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            markaz=user_markaz,juvenile__educationinfojuvenile__isnull=False,juvenile__addressinfojuvenile__isnull=False,
                                            juvenile__juvenile__isnull=False,juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()
        juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,juvenile__juvenile__passport_type='5').filter(
            created_at__year = last_year).distinct()
        juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)


    for item in juvenile_markaz:
        if item.distributed_info:
            distributed_info = item.distributed_info.id
            if field_type == 'distribution_type':
                statistic_num = models.JuvenileDistributedInfo.objects.filter(
                    pk=distributed_info).filter(
                    distribution_type=field_value).count()
                print('WER',statistic_num)
            elif field_type == 'type_guardianship':
                statistic_num = models.JuvenileDistributedInfo.objects.filter(
                    pk=distributed_info).filter(
                    type_guardianship=field_value).count()
            result += statistic_num
    return result


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

        to_parents = get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 1)
        to_others = get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 8)

        return to_parents + to_others

    def get_to_rotm(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        return get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 4)

    def get_to_orphanages(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        return get_distribution_type_statistics(request, date_from, date_to, 'type_guardianship', 5)

    def get_to_family_orphanages(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        return get_distribution_type_statistics(request, date_from, date_to, 'type_guardianship', 6)

    def get_to_sos(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        return get_distribution_type_statistics(request, date_from, date_to, 'type_guardianship', 7)

    def get_to_itm(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        return get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 3)



    def get_to_guardianship(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        vasiylik = get_distribution_type_statistics(request, date_from, date_to, 'type_guardianship', 1)
        homiylik = get_distribution_type_statistics(request, date_from, date_to, 'type_guardianship', 2)

        return vasiylik + homiylik

    def get_to_healthcare(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        return get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 5)

    def get_to_other_center(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        #

        #
        user_markaz = request.user.markaz
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False,
                juvenile__juvenile__isnull=False, juvenile__parentinfojuvenile__isnull=False,status='8').filter(
                created_at__range=[date_from, date_to]).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,status='8',
                                                                            juvenile__juvenile__passport_type='5').filter(
                created_at__range=[date_from, date_to]).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False,
                juvenile__juvenile__isnull=False, juvenile__parentinfojuvenile__isnull=False,status='8').filter(
                created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,status='8',
                                                                            juvenile__juvenile__passport_type='5').filter(
                created_at__year=last_year).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        print('KJK',juvenile_markaz.count())
        return juvenile_markaz.count()

        # for item in juvenile_markaz:
        #     if item.distributed_info:
        #         distributed_info = item.distributed_info.id
        #         if field_type == 'distribution_type':
        #             statistic_num = models.JuvenileDistributedInfo.objects.filter(
        #                 pk=distributed_info).filter(
        #                 distribution_type=field_value).count()
        #             print('WER', statistic_num)
        #         elif field_type == 'type_guardianship':
        #             statistic_num = models.JuvenileDistributedInfo.objects.filter(
        #                 pk=distributed_info).filter(
        #                 type_guardianship=field_value).count()
        #         result += statistic_num
        # return result

        # return get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 6)

    def get_to_other_country(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        return get_distribution_type_statistics(request, date_from, date_to, 'distribution_type', 7)


# apparat distribution type statistics function
def get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, field_type, field_value):
    result = 0
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
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            markaz=markaz_id).filter(created_at__range=[date_from, date_to])

    elif date_from and date_to:
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            created_at__range=[date_from, date_to])
    elif markaz_id:
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            markaz=markaz_id).filter(
            created_at__year=last_year)
    else:
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            created_at__year=last_year)

    for item in juvenile_markaz:
        if item.distributed_info:
            distributed_info = item.distributed_info.id
            if field_type == 'distribution_type':
                statistic_num = models.JuvenileDistributedInfo.objects.filter(
                    pk=distributed_info).filter(
                    distribution_type=field_value).count()
            elif field_type == 'type_guardianship':
                statistic_num = models.JuvenileDistributedInfo.objects.filter(
                    pk=distributed_info).filter(
                    type_guardianship=field_value).count()
            result += statistic_num
    return result


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
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'distribution_type', 4)

    def get_to_orphanages(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'type_guardianship', 5)

    def get_to_family_orphanages(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'type_guardianship', 6)

    def get_to_sos(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'type_guardianship', 7)

    def get_to_guardianship(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'distribution_type', 5)

    def get_to_other_center(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        #

        #
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        if date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False,
                juvenile__juvenile__isnull=False, juvenile__parentinfojuvenile__isnull=False,status='8').filter(
                created_at__range=[date_from, date_to]).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(status='8',
                                                                            juvenile__juvenile__passport_type='5').filter(
                created_at__range=[date_from, date_to]).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False,
                juvenile__juvenile__isnull=False, juvenile__parentinfojuvenile__isnull=False,status='8').filter(
                created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(status='8',
                                                                            juvenile__juvenile__passport_type='5').filter(
                created_at__year=last_year).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
        return juvenile_markaz.count()
    # def get_to_other_center(self, obj):
    #     request = self.context.get('request')
    #
    #     date_from = request.GET.get('date_from')
    #     date_to = request.GET.get('date_to')
    #     markaz_id = request.GET.get('markaz_id')
    #
    #     return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'distribution_type', 6)

    def get_to_other_country(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        markaz_id = request.GET.get('markaz_id')

        return get_apparat_distribution_type_statistics(markaz_id, date_from, date_to, 'distribution_type', 7)
    def get_to_itm(self, obj):
        request = self.context.get('request')

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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

        if date_from and date_to:
            juvenile_ids = []
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

            # for item in juvenile_markaz:
            #     juvenile_ids.append(item.juvenile_id)
            # juveniles = models.Juvenile.objects.filter(
            #     id__in=juvenile_ids).filter(accepted_center_number__gte=2).count()
            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1
        else:
            juvenile_ids = []
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _,count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1

            # juveniles = models.Juvenile.objects.filter(
            #     id__in=juvenile_ids).filter(accepted_center_number__gte=2).count()

        return come_more_times_juveniles

    def get_boys(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_ids = []
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to],juvenile__juvenile__gender='M').distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to],juvenile__juvenile__gender='M').distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1

            # for item in juvenile_markaz:
            #     juvenile_ids.append(item.juvenile_id)
            # boys = models.PersonalInfoJuvenile.objects.filter(
            #     gender='M').filter(juvenile__id__in=juvenile_ids).filter(
            #     juvenile__accepted_center_number__gte=2).count()

        else:
            juvenile_ids = []
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year,juvenile__juvenile__gender='M').distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year,juvenile__juvenile__gender='M').distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1
            # for item in juvenile_markaz:
            #     juvenile_ids.append(item.juvenile_id)
            # boys = models.PersonalInfoJuvenile.objects.filter(
            #     gender='M').filter(juvenile__id__in=juvenile_ids).filter(
            #     juvenile__accepted_center_number__gte=2).count()

        return come_more_times_juveniles

    def get_girls(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_ids = []
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to],juvenile__juvenile__gender='F').distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to],juvenile__juvenile__gender='F').distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
            # for item in juvenile_markaz:
            #     juvenile_ids.append(item.juvenile_id)
            # girls = models.PersonalInfoJuvenile.objects.filter(
            #     gender='F').filter(juvenile__id__in=juvenile_ids).filter(
            #     juvenile__accepted_center_number__gte=2).count()
            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1
        else:
            juvenile_ids = []
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=user_markaz, juvenile__educationinfojuvenile__isnull=False,
                juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year,juvenile__juvenile__gender='F').distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year,juvenile__juvenile__gender='F').distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
            # for item in juvenile_markaz:
            #     juvenile_ids.append(item.juvenile_id)
            # girls = models.PersonalInfoJuvenile.objects.filter(
            #     gender='F').filter(juvenile__id__in=juvenile_ids).filter(
            #     juvenile__accepted_center_number__gte=2).count()
            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1

        return come_more_times_juveniles


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

        if date_from and date_to:
            juvenile_ids = []

            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                                                       juvenile__educationinfojuvenile__isnull=False,
                                                       juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                                       juvenile__parentinfojuvenile__isnull=False).filter(status__in=['1','2']).filter(
                                                       created_at__range=[date_from, date_to]).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to],status__in=['1','2']).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            juveniles = models.Juvenile.objects.filter(id__in=juvenile_ids).count()
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(created_at__range=[date_from, date_to]).count()
            #
            # all_juveniles = juveniles + unidentified_juvenile
            all_juveniles = juveniles
        else:
            juvenile_ids = []
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                                                       juvenile__educationinfojuvenile__isnull=False,
                                                       juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                                       juvenile__parentinfojuvenile__isnull=False).filter(status__in=['1','2']).filter(
                                                       created_at__year=last_year).distinct()
            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year,status__in=['1','2']).distinct()
            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            juveniles = models.Juvenile.objects.filter(id__in=juvenile_ids).count()

            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(created_at__year=last_year).count()

            # all_juveniles = juveniles + unidentified_juvenile
            all_juveniles = juveniles

        return all_juveniles

    def get_boys(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_ids = []
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                   juvenile__educationinfojuvenile__isnull=False,
                   juvenile__addressinfojuvenile__isnull=False, juvenile__juvenile__isnull=False,
                   juvenile__parentinfojuvenile__isnull=False).filter(status__in=['1', '2']).filter(
                created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to],
                                                              status__in=['1', '2']).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            boys = models.PersonalInfoJuvenile.objects.filter(
                gender='M').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_boys = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(
            #     gender='M').filter(
            #     created_at__range=[date_from, date_to]).count()

            # all_boys = boys + unidentified_boys
            all_boys = boys
        else:
            juvenile_ids = []
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                                                       juvenile__educationinfojuvenile__isnull=False,
                                                       juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
                                                       juvenile__parentinfojuvenile__isnull=False).filter(status__in=['1','2']).filter(
                                                       created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year,status__in=['1','2']).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            boys = models.PersonalInfoJuvenile.objects.filter(
                gender='M').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_boys = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(
            #     gender='M').filter(
            #     created_at__year=last_year).count()

            # all_boys = boys + unidentified_boys
            all_boys = boys
        return all_boys

    def get_girls(self, obj):
        request = self.context.get('request')
        user_markaz = request.user.markaz

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to:
            juvenile_ids = []
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                                                                    juvenile__educationinfojuvenile__isnull=False,
                                                                    juvenile__addressinfojuvenile__isnull=False,
                                                                    juvenile__juvenile__isnull=False,
                                                                    juvenile__parentinfojuvenile__isnull=False).filter(
                status__in=['1', '2']).filter(
                created_at__range=[date_from, date_to]).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__range=[date_from, date_to],
                                                              status__in=['1', '2']).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            girls = models.PersonalInfoJuvenile.objects.filter(
                gender='F').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_girls = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(
            #     gender='F').filter(
            #     created_at__range=[date_from, date_to]).count()

            # all_girls = girls + unidentified_girls
            all_girls = girls
        else:
            juvenile_ids = []
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz,
                                                                    juvenile__educationinfojuvenile__isnull=False,
                                                                    juvenile__addressinfojuvenile__isnull=False,
                                                                    juvenile__juvenile__isnull=False,
                                                                    juvenile__parentinfojuvenile__isnull=False).filter(
                status__in=['1', '2']).filter(
                created_at__year=last_year).distinct()

            juvenile_markaz_foreign = models.Juvenile_Markaz.objects.filter(markaz = user_markaz,
                juvenile__juvenile__passport_type='5').filter(created_at__year=last_year, status__in=['1', '2']).distinct()

            juvenile_markaz = juvenile_markaz.union(juvenile_markaz_foreign)

            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            girls = models.PersonalInfoJuvenile.objects.filter(
                gender='F').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_girls = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=user_markaz).filter(
            #     gender='F').filter(
            #     created_at__year=last_year).count()

            # all_girls = girls + unidentified_girls
            all_girls = girls
        return all_girls


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
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id,juvenile__educationinfojuvenile__isnull=False,
            #                    juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
            #                    juvenile__parentinfojuvenile__isnull=False).filter(created_at__range=[date_from, date_to]).count()
            #
            # juvenile_markaz_foreign = (models.Juvenile_Markaz.objects.filter(markaz=markaz_id,
            #                                                                 juvenile__juvenile__passport_type='5').
            #                                                                 filter(created_at__range=[date_from, date_to])).count()
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id).count()


            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to]).count()
            # juvenile_markaz += unidentified_juvenile
        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to).count()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(created_at__range=[date_from, date_to],
            #                                                         juvenile__educationinfojuvenile__isnull=False,
            #                                                         juvenile__addressinfojuvenile__isnull=False,
            #                                                         juvenile__juvenile__isnull=False,
            #                                                         juvenile__parentinfojuvenile__isnull=False
            #                                                         ).count()
            # juvenile_markaz_foreign = (models.Juvenile_Markaz.objects.filter(juvenile__juvenile__passport_type='5').
            #                                                                 filter(created_at__range=[date_from, date_to])).count()
            # juvenile_markaz += juvenile_markaz_foreign
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     created_at__range=[date_from, date_to]).count()
            # juvenile_markaz += unidentified_juvenile
        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id).count()

            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id,juvenile__educationinfojuvenile__isnull=False,
            #                    juvenile__addressinfojuvenile__isnull=False,juvenile__juvenile__isnull=False,
            #                    juvenile__parentinfojuvenile__isnull=False).filter(created_at__year=last_year).count()
            # juvenile_markaz_foreign = (models.Juvenile_Markaz.objects.filter(markaz = markaz_id,juvenile__juvenile__passport_type='5').
            #                            filter(created_at__range=[date_from, date_to])).count()
            # juvenile_markaz += juvenile_markaz_foreign

            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=markaz_id).filter(created_at__year=last_year).count()
            # juvenile_markaz += unidentified_juvenile
        else:
            juvenile_markaz = get_juvenile_markaz().count()
            print(9090,juvenile_markaz)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(created_at__year=last_year,
            #                                                         juvenile__educationinfojuvenile__isnull=False,
            #                                                         juvenile__addressinfojuvenile__isnull=False,
            #                                                         juvenile__juvenile__isnull=False,
            #                                                         juvenile__parentinfojuvenile__isnull=False
            #                                                         ).count()
            # juvenile_markaz_foreign = (models.Juvenile_Markaz.objects.filter(juvenile__juvenile__passport_type='5').
            #                            filter(created_at__year=last_year)).count()
            # juvenile_markaz += juvenile_markaz_foreign
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(created_at__year=last_year).count()
            # juvenile_markaz += unidentified_juvenile
        return juvenile_markaz

    def get_boys(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=markaz_id).filter(gender='M').filter(created_at__range=[date_from, date_to]).count()
            # result += unidentified_juvenile
        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)

            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(created_at__range=[date_from, date_to])
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(gender='M').filter(
            #     created_at__range=[date_from, date_to]).count()
            # result += unidentified_juvenile
        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__year=last_year)
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=markaz_id).filter(gender='M').filter(created_at__year=last_year).count()
            # result += unidentified_juvenile
        else:
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(created_at__year=last_year)
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(gender='M').filter(
            #     created_at__year=last_year).count()
            # result += unidentified_juvenile

        for item in juvenile_markaz:
            boy = models.PersonalInfoJuvenile.objects.filter(juvenile=item.juvenile).filter(gender='M').count()
            result += boy

        return result

    def get_girls(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=markaz_id).filter(gender='F').filter(created_at__range=[date_from, date_to]).count()
            # result += unidentified_juvenile
        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(gender='F').filter(
            #     created_at__range=[date_from, date_to]).count()
            # result += unidentified_juvenile
        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(
            #     created_at__year=last_year)
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz=markaz_id).filter(gender='F').filter(created_at__year=last_year).count()
            # result += unidentified_juvenile
        else:
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(gender='F').filter(
            #     created_at__year=last_year).count()
            # result += unidentified_juvenile
        for item in juvenile_markaz:
            girl = models.PersonalInfoJuvenile.objects.filter(
                juvenile=item.juvenile).filter(gender='F').count()
            result += girl

        return result

    def get_graduated_itm(self, obj):
        request = self.context.get('request')
        markaz_id = request.GET.get('markaz_id')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id).filter(
                monitoring_info__monitoring_status=2).count()

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to).filter(
                monitoring_info__monitoring_status=2).count()
        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id).filter(
                monitoring_info__monitoring_status=2).count()
        else:
            juvenile_markaz = get_juvenile_markaz().filter(
                monitoring_info__monitoring_status=2).count()
        return juvenile_markaz

    def get_employment_guaranteed(self, obj):
        request = self.context.get('request')
        markaz_id = request.GET.get('markaz_id')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
        else:
            juvenile_markaz = get_juvenile_markaz()

        for item in juvenile_markaz:
            if item.employment_info:
                if item.employment_info.employment_file:
                    result += 1
        return result

    def get_not_identified(self, obj):
        request = self.context.get('request')
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(
            #     created_at__year=last_year)

        else:
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                unsupervised_child = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=1).count()
                result += unsupervised_child
        return result

    def get_neglected_child(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(
            #     created_at__year=last_year)

        else:
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                neglected_child = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=2).count()
                result += neglected_child
        return result

    def get_needs_state_public_support(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(
            #     created_at__year=last_year)

        else:
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                needs_state_public_support = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=3).count()
                result += needs_state_public_support
        return result

    def get_dangerous_social_situation(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id = markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(
            #     created_at__year=last_year)

        else:
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                dangerous_social_situation = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=4).count()
                result += dangerous_social_situation
        return result

    def get_missing_and_wanted(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

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
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(
            #     created_at__year=last_year)

        else:
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                missing_and_wanted = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=6).count()
                result += missing_and_wanted
        return result

    def get_difficult_upbringing(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(
            #     created_at__year=last_year)

        else:
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)

        for item in juvenile_markaz:
            if item.accept_center_info:
                accept_center_info = item.accept_center_info.id
                difficult_upbringing = models.JuvenileAcceptCenterInfo.objects.filter(
                    pk=accept_center_info).filter(sub_reason_bringing_child__parent=5).count()
                result += difficult_upbringing
        return result


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
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id).filter(status__in=['1','2'])
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=markaz_id).filter(
            #     status__in=['1','2']).filter(created_at__range=[date_from, date_to])
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            juveniles = models.Juvenile.objects.filter(id__in=juvenile_ids).count()

            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz_id=markaz_id).filter(created_at__range=[date_from, date_to]).count()

            # all_juveniles = juveniles + unidentified_juvenile
            all_juveniles = juveniles

        elif date_from and date_to:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(date_from,date_to).filter(status__in=['1','2'])
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            juveniles = models.Juvenile.objects.filter(
                id__in=juvenile_ids).count()
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     created_at__range=[date_from, date_to]).count()

            # all_juveniles = juveniles + unidentified_juvenile
            all_juveniles = juveniles

        elif markaz_id:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id).filter(status__in=['1','2'])
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            juveniles = models.Juvenile.objects.filter(id__in=juvenile_ids).count()
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz_id=markaz_id).filter(created_at__year=last_year).count()

            # all_juveniles = juveniles + unidentified_juvenile
            all_juveniles = juveniles

        else:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz().filter(status__in=['1','2'])
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(status__in=['1','2']).filter(created_at__year=last_year)

            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            juveniles = models.Juvenile.objects.filter(id__in=juvenile_ids).count()
            # unidentified_juvenile = models.UnidentifiedJuvenile.objects.filter(
            #     markaz_id=markaz_id).filter(created_at__year=last_year).count()

            # all_juveniles = juveniles + unidentified_juvenile
            all_juveniles = juveniles

        return all_juveniles

    def get_boys(self, obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id=markaz_id).filter(status__in=['1', '2'])

            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            boys = models.PersonalInfoJuvenile.objects.filter(
                gender='M').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_boys = models.UnidentifiedJuvenile.objects.filter(
            #     markaz_id=markaz_id).filter(
            #     gender='M').filter(
            #     created_at__range=[date_from, date_to]).count()

            # all_boys = boys + unidentified_boys
            all_boys = boys

        elif date_from and date_to:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(date_from,date_to).filter(status__in=['1', '2'])

            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            boys = models.PersonalInfoJuvenile.objects.filter(
                gender='M').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_boys = models.UnidentifiedJuvenile.objects.filter(gender='M').filter(
            #     created_at__range=[date_from, date_to]).count()

            # all_boys = boys + unidentified_boys
            all_boys = boys

        elif markaz_id:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id).filter(status__in=['1', '2'])

            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(status__in=['1','2']).filter(created_at__year=last_year)
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            boys = models.PersonalInfoJuvenile.objects.filter(
                gender='M').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_boys = models.UnidentifiedJuvenile.objects.filter(
            #     markaz_id=markaz_id).filter(
            #     gender='M').filter(
            #     created_at__year=last_year).count()

            # all_boys = boys + unidentified_boys
            all_boys = boys

        else:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz().filter(status__in=['1', '2'])
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            boys = models.PersonalInfoJuvenile.objects.filter(
                gender='M').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_boys = models.UnidentifiedJuvenile.objects.filter(
            #     gender='M').filter(
            #     created_at__year=last_year).count()

            # all_boys = boys + unidentified_boys
            all_boys = boys

        return all_boys

    def get_girls(self, obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id=markaz_id).filter(status__in=['1', '2'])

            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            girls = models.PersonalInfoJuvenile.objects.filter(
                gender='F').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_boys = models.UnidentifiedJuvenile.objects.filter(
            #     markaz_id=markaz_id).filter(
            #     gender='M').filter(
            #     created_at__range=[date_from, date_to]).count()

            # all_boys = boys + unidentified_boys
            all_girls = girls

        elif date_from and date_to:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(date_from,date_to).filter(status__in=['1', '2'])

            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            girls = models.PersonalInfoJuvenile.objects.filter(
                gender='F').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_boys = models.UnidentifiedJuvenile.objects.filter(gender='M').filter(
            #     created_at__range=[date_from, date_to]).count()

            # all_boys = boys + unidentified_boys
            all_girls = girls

        elif markaz_id:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id).filter(status__in=['1', '2'])

            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(status__in=['1','2']).filter(created_at__year=last_year)
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            girls = models.PersonalInfoJuvenile.objects.filter(
                gender='F').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_boys = models.UnidentifiedJuvenile.objects.filter(
            #     markaz_id=markaz_id).filter(
            #     gender='M').filter(
            #     created_at__year=last_year).count()

            # all_boys = boys + unidentified_boys
            all_girls = girls

        else:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz().filter(status__in=['1', '2'])
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            girls = models.PersonalInfoJuvenile.objects.filter(
                gender='F').filter(juvenile__id__in=juvenile_ids).count()

            # unidentified_boys = models.UnidentifiedJuvenile.objects.filter(
            #     gender='M').filter(
            #     created_at__year=last_year).count()

            # all_boys = boys + unidentified_boys
            all_girls = girls

        return all_girls


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
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1

        elif date_from and date_to:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1
        elif markaz_id:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__year=last_year)
            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1


        else:
            print("12SHIT")
            juvenile_ids = []
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(created_at__year=last_year)
            juvenile_markaz = get_juvenile_markaz()

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1
        return come_more_times_juveniles

    def get_boys(self, obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)
            juvenile_markaz = juvenile_markaz.filter(juvenile__juvenile__gender='M')

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1

        elif date_from and date_to:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            juvenile_markaz = juvenile_markaz.filter(juvenile__juvenile__gender='M')

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1

        elif markaz_id:
            juvenile_ids = []
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__year=last_year)
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

            juvenile_markaz = juvenile_markaz.filter(juvenile__juvenile__gender='M')

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1
        else:
            juvenile_ids = []
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(created_at__year=last_year)
            juvenile_markaz = get_juvenile_markaz()
            juvenile_markaz = juvenile_markaz.filter(juvenile__juvenile__gender='M')

            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)


            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1

        return come_more_times_juveniles

    def get_girls(self, obj):
        request = self.context.get('request')

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)
            juvenile_markaz = juvenile_markaz.filter(juvenile__juvenile__gender='F')

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1

        elif date_from and date_to:
            juvenile_ids = []
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            juvenile_markaz = juvenile_markaz.filter(juvenile__juvenile__gender='F')

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1

        elif markaz_id:
            juvenile_ids = []
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__year=last_year)
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            juvenile_markaz = juvenile_markaz.filter(juvenile__juvenile__gender='F')

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1
        else:
            juvenile_ids = []
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)
            juvenile_markaz = juvenile_markaz.filter(juvenile__juvenile__gender='F')

            come_more_times_juveniles = 0
            for item in juvenile_markaz:
                juvenile_ids.append(item.juvenile_id)
            counter = Counter(juvenile_ids)
            for _, count in counter.items():
                if count > 1:
                    come_more_times_juveniles += 1

        return come_more_times_juveniles


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
                markaz=markaz_id).filter(created_at__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                created_at__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                markaz=markaz_id).filter(created_at__year=last_year)

        else:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                created_at__year=last_year)

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

        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError(
                    {'message': 'markaz_id is not valid!'})
        juvenile_ids = []
        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to,markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(
            #     created_at__year=last_year)

        else:
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)
            juvenile_markaz = get_juvenile_markaz()

        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)

        kindergarten = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=1).count()

        return kindergarten

    def get_school(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(
            #     created_at__year=last_year)

        else:
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)
        juvenile_ids = []

        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        school = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=2).count()

        return school

    def get_vocational_school(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(
            #     created_at__year=last_year)

        else:
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        vocational_school = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=3).count()


        return vocational_school

    def get_vocational_college(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(created_at__range=[date_from, date_to])

        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from,date_to)

            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__range=[date_from, date_to])

        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)

            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     markaz=markaz_id).filter(
            #     created_at__year=last_year)

        else:
            juvenile_markaz = get_juvenile_markaz()
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            #     created_at__year=last_year)

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        vocational_college = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=4).count()

        return vocational_college

    def get_litsey(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)


        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        litsey = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=5).count()


        return litsey

    def get_texnikum(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        texnikum = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=6).count()

        return texnikum

    def get_special_education(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to,markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)


        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        special_education = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in=juvenile_ids).filter(school_type=7).count()

        return special_education

    def get_otm(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        otm = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in = juvenile_ids).filter(school_type=8).count()

        return otm

    def get_working(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
        markaz_id = request.GET.get('markaz_id')

        if markaz_id == '':
            markaz_id = None

        if markaz_id:
            try:
                info_db.Markaz.objects.get(pk=markaz_id)
            except:
                raise serializers.ValidationError({'message': 'markaz_id is not valid!'})

        if date_from and date_to and markaz_id:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to,markaz_id)


        elif date_from and date_to:
            juvenile_markaz = get_juvenile_markaz(date_from, date_to)


        elif markaz_id:
            juvenile_markaz = get_juvenile_markaz(markaz_id=markaz_id)


        else:
            juvenile_markaz = get_juvenile_markaz()

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        working = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in = juvenile_ids).filter(school_type=10).count()

        return working

    def get_not_study_not_working(self, obj):
        request = self.context.get('request')
        result = 0
        last_year = int(format(datetime.now(), '%Y'))

        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')
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

        juvenile_ids = []
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile.id)
        not_study_not_working = models.EducationInfoJuvenile.objects.filter(
            juvenile__id__in = juvenile_ids).filter(school_type=9).count()

        return not_study_not_working
