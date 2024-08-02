import mimetypes
import os
import base64

from hurry.filesize import alternative, size
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from django.db.models import F

from info import enums
from juvenile import models
from info.api.serializers import SubReasonBringingChildByParentListSerializer
from info import models as info_db
from django.utils import timezone

def is_have_all_info(juvenile_id):
    try:
        ps_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=juvenile_id).first()
    except:
        ps_info = None

    try:
        add_info = models.AddressInfoJuvenile.objects.filter(juvenile_id=juvenile_id).first()
    except:
        add_info = None

    try:
        edu_info = models.EducationInfoJuvenile.objects.filter(juvenile_id=juvenile_id).first()
    except:
        edu_info = None

    try:
        pt_info = models.ParentInfoJuvenile.objects.filter(juvenile_id=juvenile_id).first()
    except:
        pt_info = None


    if ps_info and add_info and edu_info and pt_info:
        return True
    return False


# Markazga qabul qilish
class JuvenileAcceptCenterInfoDetailSerializer(serializers.ModelSerializer):
    sub_reason_bringing_child = SubReasonBringingChildByParentListSerializer()

    class Meta:
        model = models.JuvenileAcceptCenterInfo
        fields = (
            "determined_location",
            "arrived_date",
            "arrived_reason",
            "prophylactic_list",
            'arrived_reason_file',
            'medical_list',
            'have_been_in_rotm_reason',
            'have_been_in_itm_reason',
            'sub_reason_bringing_child'
        )


class JuvenileAcceptCenterInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileAcceptCenterInfo
        fields = (
            'determined_location',
            'arrived_date',
            'arrived_reason',
            'prophylactic_list',
            'arrived_reason_file',
            'medical_list',
            'have_been_in_rotm_reason',
            'have_been_in_itm_reason',
            'sub_reason_bringing_child'
        )


class JuvenileAcceptCenterInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileAcceptCenterInfo
        fields = (
            'determined_location',
            'arrived_date',
            'arrived_reason',
            'prophylactic_list',
            'arrived_reason_file',
            'medical_list',
            'have_been_in_rotm_reason',
            'have_been_in_itm_reason',
            'sub_reason_bringing_child'
        )


# Taqsimlash
class JuvenileDistributedInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileDistributedInfo
        fields = (
            "distribution_type",
            'markaz',
            "basis_distribution",
            "health_condition",
            "skills_hobbies",
            "organization_psyhologs_name",
            'level_kinkdship',
            'type_guardianship',
            'itm_direction',
            'itm_district',
            'itm_name',
            'rotm_type',
            'basis_sending_file',
            'center_opinion_file',
            'psyhology_condition',
            'organization_directors_name',
            'organization_coach_name',
            'is_training',
            'training_file',
            'foreign_to_whom_given',
            'psychology_condition'

        )


class JuvenileDistributedInfoDetailSerializer(serializers.ModelSerializer):
    basis_sending_file = serializers.SerializerMethodField()
    center_opinion_file = serializers.SerializerMethodField()

    class Meta:
        model = models.JuvenileDistributedInfo
        fields = (
            'distribution_type',
            'markaz',
            'basis_distribution',
            'health_condition',
            'skills_hobbies',
            'organization_psyhologs_name',
            'level_kinkdship',
            'type_guardianship',
            'itm_direction',
            'itm_district',
            'itm_name',
            'rotm_type',
            'basis_sending_file',
            'center_opinion_file',
            'psyhology_condition',
            'organization_directors_name',
            'organization_coach_name',
            'is_training',
            'training_file',
            'foreign_to_whom_given',
        )

    def get_basis_sending_file(self, obj):
        if obj.basis_sending_file != '':
            request = self.context.get('request')
            file_name = os.path.basename(obj.basis_sending_file.name)
            file_size = size(obj.basis_sending_file.size, system=alternative)
            file_type = mimetypes.guess_type(os.path.basename(obj.basis_sending_file.name))[0]
            file_path = request.build_absolute_uri(obj.basis_sending_file.url)
            file = {
                "path": file_path,
                "name": file_name,
                "size": file_size,
                "content_type": file_type,
            }
            return file

    def get_center_opinion_file_file(self, obj):
        if obj.center_opinion_file != '':
            request = self.context.get('request')
            file_name = os.path.basename(obj.center_opinion_file.name)
            file_size = size(obj.center_opinion_file.size, system=alternative)
            file_type = mimetypes.guess_type(
                os.path.basename(obj.center_opinion_file.name))[0]
            file_path = request.build_absolute_uri(obj.center_opinion_file.url)
            file = {
                "path": file_path,
                "name": file_name,
                "size": file_size,
                "content_type": file_type,
            }
            return file


class JuvenileDistributedInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileDistributedInfo
        fields = (
            "distribution_type",
            'markaz',
            "basis_distribution",
            "health_condition",
            "skills_hobbies",
            "organization_psyhologs_name",
            'level_kinkdship',
            'type_guardianship',
            'itm_direction',
            'itm_district',
            'itm_name',
            'rotm_type',
            'basis_sending_file',
            'center_opinion_file',
            'psyhology_condition',
            'organization_directors_name',
            'organization_coach_name',
            'is_training',
            'training_file',
            'foreign_to_whom_given',
        )


# Monitoring
class JuvenileMonitoringInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileMonitoringInfo
        fields = (
            'monitoring_status',
            'deed_and_pictures',
            'school_type',
            'speciality',
            'class_group',
            'class_leader',
            'address',
            'mastery',
            'character',
            'is_action_been_taken',
            'file_action_been_taken',
        )


class JuvenileMonitoringInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileMonitoringInfo
        fields = (
            'monitoring_status',
            'deed_and_pictures',
            'school_type',
            'speciality',
            'class_group',
            'class_leader',
            'address',
            'mastery',
            'character',
            'is_action_been_taken',
            'file_action_been_taken',
        )


class MonitoringInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileMonitoringInfo
        fields = (
            'monitoring_status',
            'deed_and_pictures',
            'school_type',
            'speciality',
            'class_group',
            'class_leader',
            'address',
            'mastery',
            'character',
            'is_action_been_taken',
            'file_action_been_taken',
        )


# Bandlik
class JuvenileEmploymentInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileEmploymentInfo
        fields = (
            'not_applied_reason',
            'employment_education_type',
            'school_name',
            'employment_speciality',
            'accepted_school',
            'neighborhood_coach',
            'employment_inspector',
            'education_direction',
            'school_applied_file',
            'military_conscripted_file',
            'employment_file',
            'is_applied_document',
            'is_accepted_to_school',
            'is_military',
        )


class JuvenileEmploymentInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileEmploymentInfo
        fields = (
            'not_applied_reason',
            'employment_education_type',
            'school_name',
            'employment_speciality',
            'accepted_school',
            'neighborhood_coach',
            'employment_inspector',
            'education_direction',
            'school_applied_file',
            'military_conscripted_file',
            'employment_file',
            'is_applied_document',
            'is_accepted_to_school',
            'is_military',
        )


class EmploymentInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JuvenileEmploymentInfo
        fields = (
            'not_applied_reason',
            'employment_education_type',
            'school_name',
            'employment_speciality',
            'accepted_school',
            'neighborhood_coach',
            'employment_inspector',
            'education_direction',
            'school_applied_file',
            'military_conscripted_file',
            'employment_file',
            'is_applied_document',
            'is_accepted_to_school',
            'is_military',
        )


# Personal info serializer
class PersonalInfoJuvenileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PersonalInfoJuvenile
        fields = (
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'birth_district',
            'pinfl',
            'gender',
            'photo',
            'passport_type',
            'passport_seria',
            'reference_type',
            'foreign_country'
        )


class PersonalInfoJuvenileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PersonalInfoJuvenile
        fields = (
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'birth_district',
            'pinfl',
            'gender',
            'photo',
            'passport_type',
            'passport_seria',
            'reference_type',
            'foreign_country'
        )


class PersonalInfoJuvenileListSerializer(serializers.ModelSerializer):
    birth_district = serializers.SerializerMethodField()
    birth_region = serializers.SerializerMethodField()

    class Meta:
        model = models.PersonalInfoJuvenile
        fields = (
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'birth_district',
            'pinfl',
            'gender',
            'photo',
            'passport_type',
            'passport_seria',
            'reference_type',
            'foreign_country',
            "birth_region"
        )

    def get_birth_district(self, obj):
        if obj.birth_district is not None:
            district_id = obj.birth_district_id
            district_name = obj.birth_district.name

            region = {
                "id": district_id,
                "name": district_name,
            }
            return region
        return None

    def get_birth_region(self, obj):
        if obj.birth_district is not None:
            region_id = obj.birth_district.region_id.id
            region_name = obj.birth_district.region_id.name

            region = {
                "id": region_id,
                "name": region_name,
            }
            return region
        return None


class PersonalInfoJuvenileDetailSerializer(serializers.ModelSerializer):
    birth_region = serializers.SerializerMethodField()
    birth_district = serializers.SlugRelatedField(slug_field='name', read_only=True)
    passport_type = serializers.SerializerMethodField()

    class Meta:
        model = models.PersonalInfoJuvenile
        fields = (
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'birth_district',
            'pinfl',
            'gender',
            'photo',
            'passport_type',
            'passport_seria',
            'reference_type',
            'foreign_country',
            "birth_region"
        )

    def get_birth_region(self, obj):
        return obj.birth_district.region_id.name

    def get_passport_type(self, obj):
        passport_type = int(obj.passport_type) - 1
        return enums.PASSPORT_TYPE_CHOICE[passport_type][1]


# Address info Juvenile serializer
class AddressInfoJuvenileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressInfoJuvenile
        fields = (
            'address_mahalla',
            'address',
        )


class AddressInfoJuvenileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressInfoJuvenile
        fields = (
            'address_mahalla',
            'address',
        )


# Education info Juvenile serializer
class EducationInfoJuvenileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EducationInfoJuvenile
        fields = (
            'school_type',
            'kindergarten',
            'school',
            'university',
            'special_education',
            'litsey',
            'vocational_school',
            'college',
            'texnikum',
        )


class EducationInfoJuvenileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EducationInfoJuvenile
        fields = (
            'school_type',
            'kindergarten',
            'school',
            'university',
            'special_education',
            'litsey',
            'vocational_school',
            'college',
            'texnikum',
        )


# Parent info juvenile serializer
class ParentInfoJuvenileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ParentInfoJuvenile
        fields = (
            'marital_status',
        )


class ParentInfoJuvenileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ParentInfoJuvenile
        fields = (
            'marital_status',
        )


# SearchJuvenile Serializer
class SearchJuvenileSerializer(serializers.ModelSerializer):
    personal_info = PersonalInfoJuvenileDetailSerializer()

    class Meta:
        model = models.Juvenile
        fields = (
            'personal_info',
        )


# UnidentifiedJuvenile Serializer
class UnidentifiedJuvenileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UnidentifiedJuvenile
        fields = (
            "first_name",
            "last_name",
            "father_name",
            "birth_date",
            "birth_district",
            "gender",
            "photo",
        )


class UnidentifiedJuvenileListSerializer(serializers.ModelSerializer):
    birth_district = serializers.SerializerMethodField()
    birth_region = serializers.SerializerMethodField()
    is_identified = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    class Meta:
        model = models.UnidentifiedJuvenile()
        fields = (
            'id',
            "first_name",
            "last_name",
            "father_name",
            "birth_date",
            "birth_district",
            'birth_region',
            "gender",
            "photo",
            'is_identified'
        )

    def get_is_identified(self, obj):
        return False

    def get_birth_district(self, obj):
        if obj.birth_district is not None:
            district_id = obj.birth_district_id
            district_name = obj.birth_district.name

            region = {
                "id": district_id,
                "name": district_name,
            }
            return region
        return None

    def get_birth_region(self, obj):
        if obj.birth_district is not None:
            region_id = obj.birth_district.region_id.id
            region_name = obj.birth_district.region_id.name

            region = {
                "id": region_id,
                "name": region_name,
            }
            return region
        return None

    def get_photo(self, obj):
        request = self.context.get("request")
        if obj.photo is not None:
            return request.build_absolute_uri(obj.photo.url)
        return None


class JuvenileListPersonalInfoSerializer(serializers.ModelSerializer):
    personal_info = serializers.SerializerMethodField()
    address_info = serializers.SerializerMethodField()
    education_info = serializers.SerializerMethodField()
    parent_info = serializers.SerializerMethodField()
    is_identified = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = (
            'id',
            'personal_info',
            'address_info',
            'education_info',
            'parent_info',
            'is_identified'
        )

    def get_is_identified(self, obj):
        return True

    def get_birth_district(self, obj):
        if obj.personal_info.birth_district is not None:
            district_id = obj.personal_info.birth_district.id
            district_name = obj.personal_info.birth_district.name
            district = {
                "id": district_id,
                "name": district_name,
            }
            return district
        return None

    def get_birth_region(self, obj):
        if obj.personal_info.birth_district is not None:
            region_id = obj.personal_info.birth_district.region_id.id
            region_name = obj.personal_info.birth_district.region_id.name

            region = {
                "id": region_id,
                "name": region_name,
            }
            return region
        return None

    def get_first_name(self, obj):
        personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if personal_info:
            return personal_info.first_name
        return None

    def get_last_name(self, obj):
        personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if personal_info:
            return personal_info.last_name
        return None

    def get_father_name(self, obj):
        personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if personal_info:
            return personal_info.father_name
        return None

    def get_birth_date(self, obj):
        personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if personal_info:
            return personal_info.birth_date
        return None

    def get_pinfl(self, obj):
        personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if personal_info:
            return personal_info.pinfl
        return None

    def get_personal_info(self, obj):
        request = self.context.get("request")
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=obj.id).order_by(
            '-created_at').first()
        if last_personal_info:
            pasport_type = enums.PASSPORT_TYPE_CHOICE[int(
                last_personal_info.passport_type) - 1]
            data = {
                "id": last_personal_info.id,
                "first_name": last_personal_info.first_name,
                "last_name": last_personal_info.last_name,
                "father_name": last_personal_info.father_name,
                "birth_date": last_personal_info.birth_date,
                "birth_district": None,
                "birth_region": None,
                "pinfl": last_personal_info.pinfl,
                "gender": last_personal_info.gender,
                "photo": None,
                "passport_type": {
                    "id": pasport_type[0],
                    "name": pasport_type[1],
                },
                "passport_seria": last_personal_info.passport_seria,
                "reference_type": None,
                "foreign_country": None,
                "is_been_in_center": None
            }
            if last_personal_info.photo:
                data['photo'] = request.build_absolute_uri(
                    last_personal_info.photo.url)
            if last_personal_info.reference_type:
                data['reference_type'] = request.build_absolute_uri(
                    last_personal_info.reference_type.url)
            if last_personal_info.foreign_country:
                data['foreign_country'] = {
                    "id": last_personal_info.foreign_country.id,
                    "name": last_personal_info.foreign_country.name
                }
            if last_personal_info.birth_district:
                birth_region = info_db.Region.objects.get(
                    pk=last_personal_info.birth_district.region_id.id)
                data['birth_region'] = {
                    "id": birth_region.id,
                    "name": birth_region.name
                }
                data['birth_district'] = {
                    "id": last_personal_info.birth_district.id,
                    "name": last_personal_info.birth_district.name,
                }
            else:
                birth_region = None
            data['is_been_in_center'] = is_have_all_info(obj.id)
            return data
        return None

    def get_address_info(self, obj):
        last_address_info = models.AddressInfoJuvenile.objects.filter(juvenile_id=obj.id).order_by(
            '-created_at').first()
        if last_address_info:
            address_district = info_db.District.objects.get(pk=last_address_info.address_mahalla.district_id_id)
            address_region = info_db.Region.objects.get(pk=address_district.region_id_id)
            data = {
                "id": last_address_info.id,
                "address_region": {
                    "id": address_region.id,
                    "name": address_region.name
                },
                "address_district": {
                    "id": address_district.id,
                    "name": address_district.name
                },
                "address_mahalla": {
                    "id": last_address_info.address_mahalla.id,
                    "name": last_address_info.address_mahalla.name
                },
                "address": last_address_info.address,
            }
            return data
        return None

    def get_education_info(self, obj):
        last_education_info = models.EducationInfoJuvenile.objects.filter(juvenile_id=obj.id).order_by(
            '-created_at').first()

        if last_education_info:
            school_type = enums.SCHOOL_TYPE_CHOICE[int(last_education_info.school_type) - 1]
            data = {
                "id": last_education_info.id,
                "school_type": {
                    "id": school_type[0],
                    "text": school_type[1]
                },
                "kindergarten": None,
                "school": None,
                "university": None,
                "special_education": None,
                "litsey": None,
                "vocational_school": None,
                "college": None,
                "texnikum": None,
            }
            if last_education_info.kindergarten:
                kg_region = info_db.Region.objects.get(pk=last_education_info.kindergarten.district_id.region_id.id)
                data['kindergarten'] = {
                    "id": last_education_info.kindergarten.id,
                    "name": last_education_info.kindergarten.name,
                    "region": {
                        "id": kg_region.id,
                        "name": kg_region.name
                    },
                    "district": {
                        "id": last_education_info.kindergarten.district_id.id,
                        "name": last_education_info.kindergarten.district_id.name,
                    }
                }
            if last_education_info.school:
                school_region = info_db.Region.objects.get(pk=last_education_info.school.district_id.region_id.id)
                data['school'] = {
                    "id": last_education_info.school.id,
                    "name": last_education_info.school.name,
                    "region": {
                        "id": school_region.id,
                        "name": school_region.name
                    },
                    "district": {
                        "id": last_education_info.school.district_id.id,
                        "name": last_education_info.school.district_id.name,
                    }
                }

            if last_education_info.university:
                data['university'] = {
                    "id": last_education_info.university.id,
                    "name": last_education_info.university.name,
                    "region": {
                        "id": last_education_info.university.region_id.id,
                        "name": last_education_info.university.region_id.name
                    }
                }

            if last_education_info.special_education:
                data['special_education'] = {
                    "id": last_education_info.special_education.id,
                    "name": last_education_info.special_education.name,
                    "region": {
                        "id": last_education_info.special_education.region_id.id,
                        "name": last_education_info.special_education.region_id.name
                    }
                }

            if last_education_info.litsey:
                data['litsey'] = {
                    "id": last_education_info.litsey.id,
                    "name": last_education_info.litsey.name,
                    "region": {
                        "id": last_education_info.litsey.region_id.id,
                        "name": last_education_info.litsey.region_id.name
                    }
                }

            if last_education_info.vocational_school:
                data['vocational_school'] = {
                    "id": last_education_info.vocational_school.id,
                    "name": last_education_info.vocational_school.name,
                    "region": {
                        "id": last_education_info.vocational_school.region_id.id,
                        "name": last_education_info.vocational_school.region_id.name
                    }
                }
            if last_education_info.college:
                data['college'] = {
                    "id": last_education_info.college.id,
                    "name": last_education_info.college.name,
                    "region": {
                        "id": last_education_info.college.region_id.id,
                        "name": last_education_info.college.region_id.name
                    }
                }
            if last_education_info.texnikum:
                data['texnikum'] = {
                    "id": last_education_info.texnikum.id,
                    "name": last_education_info.texnikum.name,
                    "region": {
                        "id": last_education_info.texnikum.region_id.id,
                        "name": last_education_info.texnikum.region_id.name
                    }
                }

            return data
        return None

    def get_parent_info(self, obj):
        last_parent_info = models.ParentInfoJuvenile.objects.filter(juvenile_id=obj.id).order_by(
            '-created_at').first()
        if last_parent_info:
            marital_status = enums.MARITAL_STATUS_TYPE_CHOICE[int(last_parent_info.marital_status) - 1]
            data = {
                "id": last_parent_info.id,
                "marital_status": {
                    "id": marital_status[0],
                    "name": marital_status[1]
                },
                "parents": [],
            }
            parents = models.JuvenileParent.objects.filter(relationship__parent_info_juvenile=last_parent_info)
            for parent in parents:
                parent = {
                    "id": parent.id,
                    "first_name": parent.first_name,
                    "last_name": parent.last_name,
                    "birth_date": parent.birth_date,
                    "pinfl": parent.pinfl,
                    "employment": parent.employment,
                    "is_abroad": parent.is_abroad,
                    "is_wanted": parent.is_wanted,
                }
                data['parents'].append(parent)
            return data
        return None


class JuvenileDetailPersonalInfoSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="personal_info.first_name")
    last_name = serializers.CharField(source="personal_info.last_name")
    father_name = serializers.CharField(source="personal_info.father_name")
    birth_date = serializers.DateField(source="personal_info.birth_date")
    pinfl = serializers.CharField(source="personal_info.pinfl")
    gender = serializers.CharField(source="personal_info.gender")
    photo = serializers.FileField(source="personal_info.photo")
    passport_type = serializers.IntegerField(source="personal_info.passport_type")
    passport_seria = serializers.CharField(source="personal_info.passport_seria")
    reference_type = serializers.FileField(source="personal_info.reference_type")
    foreign_country = serializers.CharField(source="personal_info.foreign_country")
    birth_district = serializers.SerializerMethodField()
    birth_region = serializers.SerializerMethodField()
    is_identified = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = (
            'id',
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'birth_district',
            'pinfl',
            'gender',
            'photo',
            'passport_type',
            'passport_seria',
            'reference_type',
            'foreign_country',
            'birth_region',
            'is_identified'
        )

    def get_birth_district(self, obj):
        if obj.personal_info.birth_district is not None:
            district_id = obj.personal_info.birth_district.id
            district_name = obj.personal_info.birth_district.name
            district = {
                "id": district_id,
                "name": district_name,
            }
            return district
        return None

    def get_birth_region(self, obj):
        if obj.personal_info.birth_district is not None:
            region_id = obj.personal_info.birth_district.region_id.id
            region_name = obj.personal_info.birth_district.region_id.name

            region = {
                "id": region_id,
                "name": region_name,
            }
            return region
        return None

    def get_is_identified(self, obj):
        return True


class JuvenileMarkazListSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    father_name = serializers.SerializerMethodField()
    birth_date = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    time_arrival_center = serializers.SerializerMethodField()
    time_departure_center = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile_Markaz
        fields = (
            "id",
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'time_arrival_center',
            'time_departure_center',
            'status',
        )

    def get_first_name(self, obj):
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj.juvenile.id).order_by(
            '-created_at').first()
        if last_personal_info:
            return last_personal_info.first_name
        return None

    def get_last_name(self, obj):
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj.juvenile.id).order_by(
            '-created_at').first()
        if last_personal_info:
            return last_personal_info.last_name
        return None

    def get_father_name(self, obj):
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj.juvenile.id).order_by(
            '-created_at').first()
        if last_personal_info:
            return last_personal_info.father_name
        return None

    def get_birth_date(self, obj):
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj.juvenile_id).order_by('-created_at').first()
        if last_personal_info:
            return last_personal_info.birth_date
        return None

    def get_status(self, obj):
        status = enums.JUVENILE_STATUS_CHOICES[int(
                obj.status) - 1]
        data = {
            "id": status[0],
            "text": status[1]
        }
        return data
    def get_time_arrival_center(self, obj):
        if obj.accept_center_info:
            return obj.accept_center_info.arrived_date.date()
        return obj.time_arrival_center.date()

    def get_time_departure_center(self, obj):
        if obj.time_departure_center:
            return obj.time_departure_center.date()

        if obj.distributed_info:
            return obj.distributed_info.created_at.date()
        return None


class JuvenileListSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    father_name = serializers.SerializerMethodField()
    birth_date = serializers.SerializerMethodField()
    birth_district = serializers.SerializerMethodField()
    birth_region = serializers.SerializerMethodField()
    passport_documents = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    time_arrival_to_center = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile
        fields = (
            "id",
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'passport_documents',
            'status',
            'accepted_center_number',
            'birth_region',
            'birth_district',
            'time_arrival_to_center',
        )

    def get_first_name(self, obj):
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if last_personal_info:
            return last_personal_info.first_name
        return None

    def get_last_name(self, obj):
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if last_personal_info:
            return last_personal_info.last_name
        return None

    def get_father_name(self, obj):
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if last_personal_info:
            return last_personal_info.father_name
        return None

    def get_birth_date(self, obj):
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if last_personal_info:
            return last_personal_info.birth_date
        return None

    def get_passport_documents(self, obj):
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if last_personal_info:
            data = {
                'passport_type': last_personal_info.passport_type,
                'pinfl': last_personal_info.pinfl,
                'passport_seria': last_personal_info.passport_seria
            }
            return data
        return None

    def get_birth_district(self, obj):
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if last_personal_info.birth_district:

            return {
                "id": last_personal_info.birth_district.id,
                "name": last_personal_info.birth_district.name
            }
        return None

    def get_birth_region(self, obj):
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile=obj).order_by('-created_at').first()
        if last_personal_info.birth_district:
            return {
                "id": last_personal_info.birth_district.region_id.id,
                "name": last_personal_info.birth_district.region_id.name
            }
        return None

    def get_time_arrival_to_center(self, obj):
        obj.juvenile_markaz.all()

    def get_status(self, obj):
        request = self.context.get("request")
        is_superuser = request.user.is_superuser
        group_codes = request.user.groups.values_list('code', flat=True)
        user_code = None
        if not is_superuser:
            user_code = list(group_codes)[0]
        
        if user_code == 1:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(juvenile_id=obj.id).order_by('-created_at').first()
            status = enums.JUVENILE_STATUS_CHOICES[int(
                juvenile_markaz.status) - 1]
        else:
            if request.user.markaz:
                juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                    markaz=request.user.markaz).filter(juvenile_id=obj.id).order_by('-created_at').first()

                if juvenile_markaz:
                    status = enums.JUVENILE_STATUS_CHOICES[int(juvenile_markaz.status) - 1]
                else:
                    status = None
            else:
                juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                    monitoring_markaz_tuman=request.user.markaz_tuman).filter(juvenile_id=obj.id).order_by('-created_at').first()

                if juvenile_markaz:
                    status = enums.JUVENILE_STATUS_CHOICES[int(juvenile_markaz.status) - 1]
                else:
                    status = None


        if status:
            data = {
                "id": status[0],
                "text": status[1]
            }
        else:
            data = None
        return data
    

class JuvenileMarkazInfosDetailSerializer(serializers.ModelSerializer):
    personal_info = serializers.SerializerMethodField()
    address_info = serializers.SerializerMethodField()
    education_info = serializers.SerializerMethodField()
    parent_info = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    accept_center_info = serializers.SerializerMethodField()
    distribute_info = serializers.SerializerMethodField()
    monitoring_info = serializers.SerializerMethodField()
    employment_info = serializers.SerializerMethodField()
    class Meta:
        model = models.Juvenile_Markaz
        fields = (
            'id',
            'personal_info',
            'address_info',
            'education_info',
            'parent_info',
            'status',
            'accept_center_info',
            'distribute_info',
            'monitoring_info',
            'employment_info',
        )


    def get_personal_info(self, obj):
        request = self.context.get("request")
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=obj.juvenile.id).order_by(
            '-created_at').first()
        if last_personal_info:
            pasport_type = enums.PASSPORT_TYPE_CHOICE[int(last_personal_info.passport_type) - 1]
            data = {
                "id": last_personal_info.id,
                "first_name": last_personal_info.first_name,
                "last_name": last_personal_info.last_name,
                "father_name": last_personal_info.father_name,
                "birth_date": last_personal_info.birth_date,
                "birth_district": None,
                "birth_region": None,
                "pinfl": last_personal_info.pinfl,
                "gender": last_personal_info.gender,
                "photo": None,
                "passport_type": {
                    "id": pasport_type[0],
                    "name": pasport_type[1],
                },
                "passport_seria": last_personal_info.passport_seria,
                "reference_type": None,
                "foreign_country": None,
                "is_been_in_center": None
            }
            if last_personal_info.photo.url:
                data['photo'] = request.build_absolute_uri(last_personal_info.photo.url)
            if last_personal_info.reference_type:
                data['reference_type'] = request.build_absolute_uri(last_personal_info.reference_type.url)
            if last_personal_info.foreign_country:
                data['foreign_country'] = {
                    "id": last_personal_info.foreign_country.id,
                    "name": last_personal_info.foreign_country.name
                }
            if last_personal_info.birth_district:
                birth_region = info_db.Region.objects.get(
                    pk=last_personal_info.birth_district.region_id.id)
                data['birth_region'] = {
                    "id": birth_region.id,
                    "name": birth_region.name
                }
                data['birth_district'] = {
                    "id": last_personal_info.birth_district.id,
                    "name": last_personal_info.birth_district.name,
                }
            else:
                birth_region = None
            data['is_been_in_center'] = is_have_all_info(obj.id)
            return data
        return None

    def get_address_info(self, obj):
        last_address_info = models.AddressInfoJuvenile.objects.filter(juvenile_id=obj.juvenile.id).order_by(
            '-created_at').first()
        if last_address_info:
            address_district = info_db.District.objects.get(pk=last_address_info.address_mahalla.district_id_id)
            address_region = info_db.Region.objects.get(pk=address_district.region_id_id)
            data = {
                "id": last_address_info.id,
                "address_region": {
                    "id": address_region.id,
                    "name": address_region.name
                },
                "address_district": {
                    "id": address_district.id,
                    "name": address_district.name
                },
                "address_mahalla": {
                    "id": last_address_info.address_mahalla.id,
                    "name": last_address_info.address_mahalla.name
                },
                "address": last_address_info.address,
            }
            return data
        return None

    def get_education_info(self, obj):
        last_education_info = models.EducationInfoJuvenile.objects.filter(juvenile_id=obj.juvenile.id).order_by(
            '-created_at').first()

        if last_education_info:
            school_type = enums.SCHOOL_TYPE_CHOICE[int(last_education_info.school_type) - 1]
            data = {
                "id": last_education_info.id,
                "school_type": {
                    "id": school_type[0],
                    "text": school_type[1]
                },
                "kindergarten": None,
                "school": None,
                "university": None,
                "special_education": None,
                "litsey": None,
                "vocational_school": None,
                "college": None,
                "texnikum": None,
            }
            if last_education_info.kindergarten:
                kg_region = info_db.Region.objects.get(pk=last_education_info.kindergarten.district_id.region_id.id)
                data['kindergarten'] = {
                    "id": last_education_info.kindergarten.id,
                    "name": last_education_info.kindergarten.name,
                    "region": {
                        "id": kg_region.id,
                        "name": kg_region.name
                    },
                    "district": {
                        "id": last_education_info.kindergarten.district_id.id,
                        "name": last_education_info.kindergarten.district_id.name,
                    }
                }
            if last_education_info.school:
                school_region = info_db.Region.objects.get(pk=last_education_info.school.district_id.region_id.id)
                data['school'] = {
                    "id": last_education_info.school.id,
                    "name": last_education_info.school.name,
                    "region": {
                        "id": school_region.id,
                        "name": school_region.name
                    },
                    "district": {
                        "id": last_education_info.school.district_id.id,
                        "name": last_education_info.school.district_id.name,
                    }
                }
            if last_education_info.university:
                data['university'] = {
                    "id": last_education_info.university.id,
                    "name": last_education_info.university.name,
                    "region": {
                        "id": last_education_info.university.region_id.id,
                        "name": last_education_info.university.region_id.name
                    }
                }
            if last_education_info.special_education:
                data['special_education'] = {
                    "id": last_education_info.special_education.id,
                    "name": last_education_info.special_education.name,
                    "region": {
                        "id": last_education_info.special_education.region_id.id,
                        "name": last_education_info.special_education.region_id.name
                    }
                }
            if last_education_info.litsey:
                data['litsey'] = {
                    "id": last_education_info.litsey.id,
                    "name": last_education_info.litsey.name,
                    "region": {
                        "id": last_education_info.litsey.region_id.id,
                        "name": last_education_info.litsey.region_id.name
                    }
                }

            if last_education_info.vocational_school:
                data['vocational_school'] = {
                    "id": last_education_info.vocational_school.id,
                    "name": last_education_info.vocational_school.name,
                    "region": {
                        "id": last_education_info.vocational_school.region_id.id,
                        "name": last_education_info.vocational_school.region_id.name
                    }
                }
            if last_education_info.college:
                data['college'] = {
                    "id": last_education_info.college.id,
                    "name": last_education_info.college.name,
                    "region": {
                        "id": last_education_info.college.region_id.id,
                        "name": last_education_info.college.region_id.name
                    }
                }
            if last_education_info.texnikum:
                data['college'] = {
                    "id": last_education_info.texnikum.id,
                    "name": last_education_info.texnikum.name,
                    "region": {
                        "id": last_education_info.texnikum.region_id.id,
                        "name": last_education_info.texnikum.region_id.name
                    }
                }
            return data
        return None

    def get_parent_info(self, obj):
        last_parent_info = models.ParentInfoJuvenile.objects.filter(juvenile_id=obj.juvenile.id).order_by(
            '-created_at').first()
        if last_parent_info:
            marital_status = enums.MARITAL_STATUS_TYPE_CHOICE[int(last_parent_info.marital_status) - 1]
            data = {
                "id": last_parent_info.id,
                "marital_status": {
                    "id": marital_status[0],
                    "name": marital_status[1]
                },
                "parents": [],
            }
            parents = models.JuvenileParent.objects.filter(relationship__parent_info_juvenile=last_parent_info)
            for parent in parents:
                relationship = models.Relationship.objects.filter(parent_info_juvenile__juvenile_id=obj.juvenile.id).filter(
                    parent_id=parent.id).first()
                parent_type = enums.PARENT_TYPE_CHOICE[int(relationship.parent_type) - 1]
                parent = {
                    "id": parent.id,
                    "first_name": parent.first_name,
                    "last_name": parent.last_name,
                    "father_name": parent.father_name,
                    "birth_date": parent.birth_date,
                    "pinfl": parent.pinfl,
                    "employment": parent.employment,
                    "is_abroad": parent.is_abroad,
                    "is_wanted": parent.is_wanted,
                    "parent_type": parent_type[1]
                }
                data['parents'].append(parent)
            return data
        return None

    def get_accept_center_info(self, obj):
        request = self.context.get("request")
        center_info = obj.accept_center_info
        if center_info:
            determined_location = enums.DETERMINED_LOCATION_CHOICE[int(center_info.determined_location) - 1]
            arrived_reason = enums.ARRIVED_REASON_CHOICE[int(center_info.arrived_reason) - 1]

            data = {
                "reason_bringing_child": center_info.sub_reason_bringing_child.parent.title,
                "sub_reason_bringing_child": center_info.sub_reason_bringing_child.title,
                "determined_location": {
                    "id": determined_location[0],
                    "text": determined_location[1]
                },
                "arrived_date": center_info.arrived_date,
                "arrived_reason": {
                    "id": arrived_reason[0],
                    "text": arrived_reason[1]
                },
                "arrived_reason_file": None,
                "prophylactic_list": center_info.prophylactic_list,
                "center_come_number": obj.juvenile.accepted_center_number,
                "is_have_medical_list": False,
                "medical_list": [],
                "have_been_in_rotm_reason": None,
                "have_been_in_itm_reason": None,
                "inspector": {
                    "first_name": center_info.inspector.first_name,
                    "last_name": center_info.inspector.last_name,
                    "father_name": center_info.inspector.father_name,
                    "service_area": {
                        "region": center_info.inspector.district.region_id.name,
                        "district": center_info.inspector.district.name
                    },
                    "filled_date": center_info.created_at
                },
            }
            medical_list = models.JuvenileMedicalList.objects.filter(accept_center_info_id=center_info.id)

            for item in medical_list:
                medical_data = {
                    "id": item.medical_list.id,
                    "name": item.medical_list.title,
                }
                data['medical_list'].append(medical_data)
                if data['medical_list']:
                    data['is_have_medical_list'] = True
            if center_info.have_been_in_rotm_reason:
                have_been_in_rotm_reason = enums.HAVE_BEEN_IN_ROTM_REASON_CHOICE[
                    int(center_info.have_been_in_rotm_reason) - 1]
                data['have_been_in_rotm_reason'] = {
                                                       "id": have_been_in_rotm_reason[0],
                                                       "text": have_been_in_rotm_reason[1]
                                                   },
            if center_info.have_been_in_itm_reason:
                have_been_in_itm_reason = enums.HAVE_BEEN_IN_ITM_REASON_CHOICE[
                    int(center_info.have_been_in_itm_reason) - 1]
                data['have_been_in_itm_reason'] = {
                                                      "id": have_been_in_itm_reason[0],
                                                      "text": have_been_in_itm_reason[1]
                                                  },
            if center_info.arrived_reason_file:
                data['arrived_reason_file'] = request.build_absolute_uri(center_info.arrived_reason_file.url)
            return data
        else:
            return None

    def get_distribute_info(self, obj):
        request = self.context.get("request")
        distribute_info = obj.distributed_info

        if distribute_info:
            distribution_type = enums.DISTRIBUTION_TYPE_CHOICE[int(distribute_info.distribution_type) - 1]
            basis_distribution = enums.BASIS_DISTRIBUTION_CHOICE[int(distribute_info.basis_distribution) - 1]

            data = {
                "distribution_type": {
                    "id": distribution_type[0],
                    "text": distribution_type[1]
                },
                "basis_distribution": {
                    "id": basis_distribution[0],
                    "text": basis_distribution[1]
                },
                "basis_sending_file": None,
                "center_opinion_file": None,
                "is_training": distribute_info.is_training,
                "training_file": None,
                "skills_hobbies_file": None,
                "psyhology_condition": None
            }

            if distribute_info.basis_sending_file:
                data['basis_sending_file'] = request.build_absolute_uri(distribute_info.basis_sending_file.url)

            if distribute_info.center_opinion_file:
                data['center_opinion_file'] = request.build_absolute_uri(distribute_info.center_opinion_file.url)

            # if distribute_info.training_file:
            #     data['training_file'] = request.build_absolute_uri(distribute_info.training_file.url)

            # if distribute_info.skills_hobbies:
            #     data['skills_hobbies'] = request.build_absolute_uri(distribute_info.skills_hobbies.url)

            # if distribute_info.psyhology_condition:
            #     data['psyhology_condition'] = request.build_absolute_uri(distribute_info.psyhology_condition.url)
            if distribute_info.psychology_condition:
                data['pschology_condition'] = {
                    "id":distribute_info.psychology_condition.id,
                    "title": distribute_info.psychology_condition.title,
                    "description": distribute_info.psychology_condition.description
                }
            return data
        else:
            return None

    def get_monitoring_info(self, obj):
        request = self.context.get("request")
        monitoring_info = obj.monitoring_info

        if monitoring_info:
            monitoring_status = enums.MONITORING_STATUS_CHOICE[int(monitoring_info.monitoring_status) - 1]
            school_type = enums.SCHOOL_TYPE_CHOICE[int(monitoring_info.school_type) - 1]
            mastery = enums.MASTERY_TYPE_CHOICE[int(monitoring_info.mastery) - 1]
            character = enums.CHARACTER_TYPE_CHOICE[int(monitoring_info.character) - 1]

            data = {
                "monitoring_status": {
                    "id": monitoring_status[0],
                    "text": monitoring_status[1]
                },
                "school_type": {
                    "id": school_type[0],
                    "text": school_type[1]
                },
                "speciality": monitoring_info.speciality,
                "class_group": monitoring_info.class_group,
                "class_leader": monitoring_info.class_leader,
                "address": monitoring_info.address,
                "mastery": {
                    "id": mastery[0],
                    "text": mastery[1]
                },
                "character": {
                    "id": character[0],
                    "text": character[1]
                },
                "deed_and_pictures": None,
                "file_action_been_taken": None,
            }

            if monitoring_info.deed_and_pictures:
                data['deed_and_pictures'] = request.build_absolute_uri(monitoring_info.deed_and_pictures.url)

            if monitoring_info.file_action_been_taken:
                data['file_action_been_taken'] = request.build_absolute_uri(monitoring_info.file_action_been_taken.url)

            return data
        else:
            return None

    def get_employment_info(self, obj):
        request = self.context.get("request")
        employment_info = obj.employment_info

        if employment_info:
            data = {
                "employment_education_type": None,
                'is_applied_document': employment_info.is_applied_document,
                'not_applied_reason': employment_info.not_applied_reason,

                'school_name': employment_info.school_name,
                'education_direction': employment_info.education_direction,
                'employment_speciality': employment_info.employment_speciality,
                'is_accepted_to_school': employment_info.is_accepted_to_school,
                'accepted_school': employment_info.accepted_school,
                "school_applied_file": None,
                "military_conscripted_file": None,
                "employment_file": None,
                "neighborhood_coach": employment_info.neighborhood_coach,
                "employment_inspector": employment_info.employment_inspector,
            }

            if employment_info.school_applied_file:
                data['school_applied_file'] = request.build_absolute_uri(employment_info.school_applied_file.url)

            if employment_info.military_conscripted_file:
                data['military_conscripted_file'] = request.build_absolute_uri(
                    employment_info.military_conscripted_file.url)

            if employment_info.employment_file:
                data['employment_file'] = request.build_absolute_uri(employment_info.employment_file.url)

            if employment_info.employment_education_type:
                employment_education_type = enums.EMPLOYMENT_EDUCATION_TYPE_CHOICE[
                    int(employment_info.employment_education_type) - 1]
                data["employment_education_type"] = {
                                                        "id": employment_education_type[0],
                                                        "text": employment_education_type[1]
                                                    },
            return data
        else:
            return None

    def get_status(self, obj):
        status = enums.JUVENILE_STATUS_CHOICES[int(obj.status) - 1]

        data = {
            "id": status[0],
            "text": status[1]
        }
        return data


class JuvenileInfosDetailSerializer(serializers.ModelSerializer):
    personal_info = serializers.SerializerMethodField()
    address_info = serializers.SerializerMethodField()
    education_info = serializers.SerializerMethodField()
    parent_info = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    accept_center_info = serializers.SerializerMethodField()
    distribute_info = serializers.SerializerMethodField()
    monitoring_info = serializers.SerializerMethodField()
    employment_info = serializers.SerializerMethodField()


    class Meta:
        model = models.Juvenile
        fields = (
            'id',
            'personal_info',
            'address_info',
            'education_info',
            'parent_info',
            'status',
            'accept_center_info',
            'distribute_info',
            'monitoring_info',
            'employment_info',
        )

    def get_personal_info(self, obj):
        request = self.context.get("request")
        last_personal_info = models.PersonalInfoJuvenile.objects.filter(juvenile_id=obj.id).order_by(
            '-created_at').first()
        if last_personal_info:
            pasport_type = enums.PASSPORT_TYPE_CHOICE[int(last_personal_info.passport_type) - 1]
            data = {
                "id": last_personal_info.id,
                "first_name": last_personal_info.first_name,
                "last_name": last_personal_info.last_name,
                "father_name": last_personal_info.father_name,
                "birth_date": last_personal_info.birth_date,
                "birth_district": None,
                "birth_region": None,
                "pinfl": last_personal_info.pinfl,
                "gender": last_personal_info.gender,
                "photo": None,
                "passport_type": {
                    "id": pasport_type[0],
                    "name": pasport_type[1],
                },
                "passport_seria": last_personal_info.passport_seria,
                "reference_type": None,
                "foreign_country": None,
                "is_been_in_center": None
            }
            if last_personal_info.photo.url:
                data['photo'] = request.build_absolute_uri(last_personal_info.photo.url)
            if last_personal_info.reference_type:
                data['reference_type'] = request.build_absolute_uri(last_personal_info.reference_type.url)
            if last_personal_info.foreign_country:
                data['foreign_country'] = {
                    "id": last_personal_info.foreign_country.id,
                    "name": last_personal_info.foreign_country.name
                }
            if last_personal_info.birth_district:
                birth_region = info_db.Region.objects.get(
                    pk=last_personal_info.birth_district.region_id.id)
                data['birth_region'] = {
                    "id": birth_region.id,
                    "name": birth_region.name
                }
                data['birth_district'] = {
                    "id": last_personal_info.birth_district.id,
                    "name": last_personal_info.birth_district.name,
                }
            else:
                birth_region = None
            data['is_been_in_center'] = is_have_all_info(obj.id)
            return data
        return None

    def get_address_info(self, obj):
        last_address_info = models.AddressInfoJuvenile.objects.filter(juvenile_id=obj.id).order_by(
            '-created_at').first()
        if last_address_info:
            address_district = info_db.District.objects.get(pk=last_address_info.address_mahalla.district_id_id)
            address_region = info_db.Region.objects.get(pk=address_district.region_id_id)
            data = {
                "id": last_address_info.id,
                "address_region": {
                    "id": address_region.id,
                    "name": address_region.name
                },
                "address_district": {
                    "id": address_district.id,
                    "name": address_district.name
                },
                "address_mahalla": {
                    "id": last_address_info.address_mahalla.id,
                    "name": last_address_info.address_mahalla.name
                },
                "address": last_address_info.address,
            }
            return data
        return None

    def get_education_info(self, obj):
        last_education_info = models.EducationInfoJuvenile.objects.filter(juvenile_id=obj.id).order_by(
            '-created_at').first()

        if last_education_info:
            school_type = enums.SCHOOL_TYPE_CHOICE[int(last_education_info.school_type) - 1]
            data = {
                "id": last_education_info.id,
                "school_type": {
                    "id": school_type[0],
                    "text": school_type[1]
                },
                "kindergarten": None,
                "school": None,
                "university": None,
                "special_education": None,
                "litsey": None,
                "vocational_school": None,
                "college": None,
                "texnikum": None,
            }
            if last_education_info.kindergarten:
                kg_region = info_db.Region.objects.get(pk=last_education_info.kindergarten.district_id.region_id.id)
                data['kindergarten'] = {
                    "id": last_education_info.kindergarten.id,
                    "name": last_education_info.kindergarten.name,
                    "region": {
                        "id": kg_region.id,
                        "name": kg_region.name
                    },
                    "district": {
                        "id": last_education_info.kindergarten.district_id.id,
                        "name": last_education_info.kindergarten.district_id.name,
                    }
                }
            if last_education_info.school:
                school_region = info_db.Region.objects.get(pk=last_education_info.school.district_id.region_id.id)
                data['school'] = {
                    "id": last_education_info.school.id,
                    "name": last_education_info.school.name,
                    "region": {
                        "id": school_region.id,
                        "name": school_region.name
                    },
                    "district": {
                        "id": last_education_info.school.district_id.id,
                        "name": last_education_info.school.district_id.name,
                    }
                }
            if last_education_info.university:
                data['university'] = {
                    "id": last_education_info.university.id,
                    "name": last_education_info.university.name,
                    "region": {
                        "id": last_education_info.university.region_id.id,
                        "name": last_education_info.university.region_id.name
                    }
                }
            if last_education_info.special_education:
                data['special_education'] = {
                    "id": last_education_info.special_education.id,
                    "name": last_education_info.special_education.name,
                    "region": {
                        "id": last_education_info.special_education.region_id.id,
                        "name": last_education_info.special_education.region_id.name
                    }
                }
            if last_education_info.litsey:
                data['litsey'] = {
                    "id": last_education_info.litsey.id,
                    "name": last_education_info.litsey.name,
                    "region": {
                        "id": last_education_info.litsey.region_id.id,
                        "name": last_education_info.litsey.region_id.name
                    }
                }

            if last_education_info.vocational_school:
                data['vocational_school'] = {
                    "id": last_education_info.vocational_school.id,
                    "name": last_education_info.vocational_school.name,
                    "region": {
                        "id": last_education_info.vocational_school.region_id.id,
                        "name": last_education_info.vocational_school.region_id.name
                    }
                }
            if last_education_info.college:
                data['college'] = {
                    "id": last_education_info.college.id,
                    "name": last_education_info.college.name,
                    "region": {
                        "id": last_education_info.college.region_id.id,
                        "name": last_education_info.college.region_id.name
                    }
                }
            if last_education_info.texnikum:
                data['college'] = {
                    "id": last_education_info.texnikum.id,
                    "name": last_education_info.texnikum.name,
                    "region": {
                        "id": last_education_info.texnikum.region_id.id,
                        "name": last_education_info.texnikum.region_id.name
                    }
                }
            return data
        return None

    def get_parent_info(self, obj):
        last_parent_info = models.ParentInfoJuvenile.objects.filter(juvenile_id=obj.id).order_by(
            '-created_at').first()
        if last_parent_info:
            marital_status = enums.MARITAL_STATUS_TYPE_CHOICE[int(last_parent_info.marital_status) - 1]
            data = {
                "id": last_parent_info.id,
                "marital_status": {
                    "id": marital_status[0],
                    "name": marital_status[1]
                },
                "parents": [],
            }
            parents = models.JuvenileParent.objects.filter(relationship__parent_info_juvenile=last_parent_info)
            for parent in parents:
                relationship = models.Relationship.objects.filter(parent_info_juvenile__juvenile_id=obj.id).filter(
                    parent_id=parent.id).first()
                parent_type = enums.PARENT_TYPE_CHOICE[int(relationship.parent_type) - 1]
                parent = {
                    "id": parent.id,
                    "first_name": parent.first_name,
                    "last_name": parent.last_name,
                    "father_name": parent.father_name,
                    "birth_date": parent.birth_date,
                    "pinfl": parent.pinfl,
                    "employment": parent.employment,
                    "is_abroad": parent.is_abroad,
                    "is_wanted": parent.is_wanted,
                    "parent_type": parent_type[1]
                }
                data['parents'].append(parent)
            return data
        return None


    def get_accept_center_info(self, obj):
        request = self.context.get("request")
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            juvenile_id=obj.id).order_by('-created_at').first()
        center_info = juvenile_markaz.accept_center_info
        if center_info:
            determined_location = enums.DETERMINED_LOCATION_CHOICE[int(center_info.determined_location) - 1]
            arrived_reason = enums.ARRIVED_REASON_CHOICE[int(center_info.arrived_reason) - 1]

            data = {
                "reason_bringing_child": center_info.sub_reason_bringing_child.parent.title,
                "sub_reason_bringing_child": center_info.sub_reason_bringing_child.title,
                "determined_location": {
                    "id": determined_location[0],
                    "text": determined_location[1]
                },
                "arrived_date": center_info.arrived_date,
                "arrived_reason": {
                    "id": arrived_reason[0],
                    "text": arrived_reason[1]
                },
                "arrived_reason_file": None,
                "prophylactic_list": center_info.prophylactic_list,
                "center_come_number": juvenile_markaz.juvenile.accepted_center_number,
                "is_have_medical_list": False,
                "medical_list": [],
                "have_been_in_rotm_reason": None,
                "have_been_in_itm_reason": None,
                "inspector": {
                    "first_name": center_info.inspector.first_name,
                    "last_name": center_info.inspector.last_name,
                    "father_name": center_info.inspector.father_name,
                    "service_area": {
                        "region": center_info.inspector.district.region_id.name,
                        "district": center_info.inspector.district.name
                    },
                    "filled_date": center_info.created_at
                },
            }
            medical_list = models.JuvenileMedicalList.objects.filter(accept_center_info_id=center_info.id)

            for item in medical_list:
                medical_data = {
                    "id": item.medical_list.id,
                    "name": item.medical_list.title,
                }
                data['medical_list'].append(medical_data)
                if data['medical_list']:
                    data['is_have_medical_list'] = True
            if center_info.have_been_in_rotm_reason:
                have_been_in_rotm_reason = enums.HAVE_BEEN_IN_ROTM_REASON_CHOICE[int(center_info.have_been_in_rotm_reason) - 1]
                data['have_been_in_rotm_reason'] = {
                    "id": have_been_in_rotm_reason[0],
                    "text": have_been_in_rotm_reason[1]
                },
            if center_info.have_been_in_itm_reason:
                have_been_in_itm_reason = enums.HAVE_BEEN_IN_ITM_REASON_CHOICE[int(center_info.have_been_in_itm_reason) - 1]
                data['have_been_in_itm_reason'] = {
                    "id": have_been_in_itm_reason[0],
                    "text": have_been_in_itm_reason[1]
                },
            if center_info.arrived_reason_file:
                data['arrived_reason_file'] = request.build_absolute_uri(center_info.arrived_reason_file.url)
            return data
        else:
            return None

    def get_distribute_info(self, obj):
        request = self.context.get("request")
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            juvenile_id=obj.id).order_by('-created_at').first()
        distribute_info = juvenile_markaz.distributed_info

        if distribute_info:
            distribution_type = enums.DISTRIBUTION_TYPE_CHOICE[int(distribute_info.distribution_type) - 1]
            basis_distribution = enums.BASIS_DISTRIBUTION_CHOICE[int(distribute_info.basis_distribution) - 1]

            data = {
                "distribution_type": {
                    "id": distribution_type[0],
                    "text": distribution_type[1]
                },
                "basis_distribution": {
                    "id": basis_distribution[0],
                    "text": basis_distribution[1]
                },
                "basis_sending_file": None,
                "center_opinion_file": None,
                "is_training": distribute_info.is_training,
                "training_file": None,
                "skills_hobbies_file": None,
                "psyhology_condition": None
            }

            if distribute_info.basis_sending_file:
                data['basis_sending_file'] = request.build_absolute_uri(distribute_info.basis_sending_file.url)

            if distribute_info.center_opinion_file:
                data['center_opinion_file'] = request.build_absolute_uri(distribute_info.center_opinion_file.url)

            if distribute_info.training_file:
                data['training_file'] = request.build_absolute_uri(distribute_info.training_file.url)

            if distribute_info.skills_hobbies:
                data['skills_hobbies'] = request.build_absolute_uri(distribute_info.skills_hobbies.url)

            if distribute_info.psyhology_condition:
                data['psyhology_condition'] = request.build_absolute_uri(distribute_info.psyhology_condition.url)

            return data
        else:
            return None

    def get_monitoring_info(self, obj):
        request = self.context.get("request")
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            juvenile_id=obj.id).order_by('-created_at').first()
        monitoring_info = juvenile_markaz.monitoring_info

        if monitoring_info:
            monitoring_status = enums.MONITORING_STATUS_CHOICE[int(monitoring_info.monitoring_status) - 1]
            school_type = enums.SCHOOL_TYPE_CHOICE[int(monitoring_info.school_type) - 1]
            mastery = enums.MASTERY_TYPE_CHOICE[int(monitoring_info.mastery) - 1]
            character = enums.CHARACTER_TYPE_CHOICE[int(monitoring_info.character) - 1]

            data = {
                "monitoring_status": {
                    "id": monitoring_status[0],
                    "text": monitoring_status[1]
                },
                "school_type": {
                    "id": school_type[0],
                    "text": school_type[1]
                },
                "speciality": monitoring_info.speciality,
                "class_group": monitoring_info.class_group,
                "class_leader": monitoring_info.class_leader,
                "address": monitoring_info.address,
                "mastery": {
                    "id": mastery[0],
                    "text": mastery[1]
                },
                "character": {
                    "id": character[0],
                    "text": character[1]
                },
                "deed_and_pictures": None,
                "file_action_been_taken": None,
            }

            if monitoring_info.deed_and_pictures:
                data['deed_and_pictures'] = request.build_absolute_uri(monitoring_info.deed_and_pictures.url)

            if monitoring_info.file_action_been_taken:
                data['file_action_been_taken'] = request.build_absolute_uri(monitoring_info.file_action_been_taken.url)

            return data
        else:
            return None

    def get_employment_info(self, obj):
        request = self.context.get("request")
        juvenile_markaz = models.Juvenile_Markaz.objects.filter(
            juvenile_id=obj.id).order_by('-created_at').first()
        employment_info = juvenile_markaz.employment_info

        if employment_info:
            data = {
                "employment_education_type": None,
                'is_applied_document': employment_info.is_applied_document,
                'not_applied_reason': employment_info.not_applied_reason,

                'school_name': employment_info.school_name,
                'education_direction': employment_info.education_direction,
                'employment_speciality': employment_info.employment_speciality,
                'is_accepted_to_school': employment_info.is_accepted_to_school,
                'accepted_school': employment_info.accepted_school,
                "school_applied_file": None,
                "military_conscripted_file": None,
                "employment_file": None,
                "neighborhood_coach": employment_info.neighborhood_coach,
                "employment_inspector": employment_info.employment_inspector,
            }

            if employment_info.school_applied_file:
                data['school_applied_file'] = request.build_absolute_uri(employment_info.school_applied_file.url)

            if employment_info.military_conscripted_file:
                data['military_conscripted_file'] = request.build_absolute_uri(employment_info.military_conscripted_file.url)

            if employment_info.employment_file:
                data['employment_file'] = request.build_absolute_uri(employment_info.employment_file.url)

            if employment_info.employment_education_type:
                employment_education_type = enums.EMPLOYMENT_EDUCATION_TYPE_CHOICE[int(employment_info.employment_education_type) - 1]
                data["employment_education_type"] = {
                    "id": employment_education_type[0],
                    "text": employment_education_type[1]
                },
            return data
        else:
            return None

        
    def get_status(self, obj):
        request = self.context.get("request")


        is_superuser = request.user.is_superuser
        group_codes = request.user.groups.values_list('code', flat=True)
        user_code = None
        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1:
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                juvenile_id=obj.id).order_by('-created_at').first()
            status = enums.JUVENILE_STATUS_CHOICES[int(
                juvenile_markaz.status) - 1]
        else:
            if request.user.markaz:
                juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                    markaz=request.user.markaz).filter(juvenile_id=obj.id).order_by('-created_at').first()
                status = enums.JUVENILE_STATUS_CHOICES[int(juvenile_markaz.status) - 1]
            else:
                juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                    monitoring_markaz_tuman=request.user.markaz_tuman).filter(juvenile_id=obj.id).order_by(
                    '-created_at').first()
                status = enums.JUVENILE_STATUS_CHOICES[int(juvenile_markaz.status) - 1]

        data = {
            "id": status[0],
            "text": status[1]
        }
        return data


class JuvenileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Juvenile
        fields = (
            'id',
        )

    def get_birth_district(self, obj):
        if obj.birth_district != None:
            district_id = obj.birth_district_id
            district_name = obj.birth_district.name

            region = {
                "id": district_id,
                "name": district_name,
            }
            return region
        return None

    def get_birth_region(self, obj):
        if obj.birth_district != None:
            region_id = obj.birth_district.region_id.id
            region_name = obj.birth_district.region_id.name

            region = {
                "id": region_id,
                "name": region_name,
            }
            return region
        return None

    #
    # def get_status(self, obj):
    #     if obj.status != None:
    #         list = JUVENILE_STATUS_CHOICES[int(obj.status) - 1]
    #         data = {
    #             "id": list[0],
    #             "text": list[1]
    #         }
    #         return data
    #     return None

    # def get_address(self, obj):
    #     if obj.address_mahalla != None:
    #         return f" {obj.address_district.district_id} {obj.address_district} {obj.address}"
    #     return None

    # def get_address_region(self, obj):
    #     if obj.address_district != None:
    #         return obj.address_district.region_id.id
    #     return None

    def get_school_region(self, obj):
        if obj.school_district != None:
            return obj.school_district.region_id.id
        return None

    def get_parent(self, obj):
        parents = []
        if obj:
            for item in obj.parent.all():
                relation = models.Relationship.objects.get(parent=item.id)
                parents.append(
                    {
                        "id": item.id,
                        "first_name": item.first_name,
                        "last_name": item.last_name,
                        "father_name": item.father_name,
                        "birth_date": item.birth_date,
                        "employment": item.employment,
                        "parent_type": int(relation.parent_type),
                        "pinfl": item.pinfl
                    }
                )
            return parents
        return None

    def get_reference_type(self, obj):
        if obj.reference_type != '':
            request = self.context.get('request')
            file_name = os.path.basename(obj.reference_type.name)
            file_size = size(obj.reference_type.size, system=alternative)
            file_type = mimetypes.guess_type(os.path.basename(obj.reference_type.name))[0]
            file_path = request.build_absolute_uri(obj.reference_type.url)
            file = {
                "path": file_path,
                "name": file_name,
                "size": file_size,
                "content_type": file_type,
            }
            return file

    def get_photo(self, obj):
        if obj.photo != '':
            request = self.context.get('request')
            file_name = os.path.basename(obj.photo.name)
            file_size = size(obj.photo.size, system=alternative)
            file_type = mimetypes.guess_type(os.path.basename(obj.photo.name))[0]
            file_path = request.build_absolute_uri(obj.photo.url)
            file = {
                "path": file_path,
                "name": file_name,
                "size": file_size,
                "content_type": file_type,
            }
            return file


class JuvenileAcceptDetailSerializer(serializers.ModelSerializer):
    accept_center_info = JuvenileAcceptCenterInfoDetailSerializer()

    class Meta:
        model = models.Juvenile
        fields = (
            'id',
            'accept_center_info'
        )


# Juvenile expelled detail
class JuvenileExpelledDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Juvenile
        fields = (
            'id',
        )


# Juvenile monitoring detail 
class JuvenileMonitoringDetailSerializer(serializers.ModelSerializer):
    monitoring_info = MonitoringInfoDetailSerializer()

    class Meta:
        model = models.Juvenile
        fields = (
            'id',
            'monitoring_info',
        )


# Juvenile employment detail
class JuvenileEmploymentDetailSerializer(serializers.ModelSerializer):
    employment_info = EmploymentInfoDetailSerializer()

    class Meta:
        model = models.Juvenile
        fields = (
            'id',
            'employment_info',
        )


# Prophylactic inspector serializer
class ProphylacticInspectorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProphylacticInspector
        fields = (
            "first_name",
            "last_name",
            "father_name",
            "inspector_id",
            "pinfl",
            'inspector_type',
            'certificate_number',
            'district'
        )


class ProphylacticInspectorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProphylacticInspector
        fields = (
            "first_name",
            "last_name",
            "father_name",
            "inspector_id",
            "pinfl",
            'inspector_type',
            'certificate_number',
            'district'
        )

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.inspector_id = validated_data.get('inspector_id', instance.inspector_id)
        instance.pinfl = validated_data.get('pinfl', instance.pinfl)
        instance.inspector_type = validated_data.get('inspector_type', instance.inspector_type)
        instance.certificate_number = validated_data.get('certificate_number', instance.certificate_number)
        instance.district = validated_data.get('district', instance.district)
        instance.save()
        return instance


class JuvenileStepFilledSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Juvenile
        fields = (
            'id',
        )





def get_distribution_type_choice(type):
    if type == '1':
        return 'Oila'
    elif type == '2':
        return 'Vasiylik organi orqali'
    elif type == '3':
        return 'ITM'
    elif type == '4':
        return "RO'TM"
    elif type == '5':
        return "Sog'liqni saqlash muassasasi"
    elif type == '6':
        return "Boshqa markazga yuborish"
    elif type == '7':
        return "Boshqa davlatga yuborish"
    elif type == '8':
        return "Boshqalar"


class JuvenileMarkazSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='juvenile.id')
    markaz_name = serializers.CharField(source='markaz.name')
    created_at = serializers.SerializerMethodField()
    first_name = serializers.CharField(source='juvenile.juvenile.first.first_name')
    last_name = serializers.CharField(source='juvenile.juvenile.first.last_name')
    father_name = serializers.CharField(source='juvenile.juvenile.first.father_name')
    passport_seria = serializers.CharField(source='juvenile.juvenile.first.passport_seria')
    pinfl = serializers.CharField(source='juvenile.juvenile.first.pinfl')
    birth_date = serializers.DateField(source='juvenile.juvenile.first.birth_date')
    birth_region = serializers.SerializerMethodField()
    birth_district = serializers.SerializerMethodField()
    parent_first_name = serializers.SerializerMethodField()
    parent_last_name = serializers.SerializerMethodField()
    parent_father_name = serializers.SerializerMethodField()
    distributed_info = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile_Markaz
        fields = ['id','created_at','first_name','last_name','father_name','passport_seria','pinfl',
                  'birth_date','birth_district','birth_region','parent_first_name','parent_father_name',
                  'parent_last_name','markaz_name','distributed_info']

    def get_birth_region(self,obj):
        try:
            return obj.juvenile.juvenile.first().birth_district.region_id.name
        except:
            return None
    def get_birth_district(self,obj):
        try:
            return obj.juvenile.juvenile.first().birth_district.name
        except:
            return None
    def get_created_at(self,obj):
        return obj.accept_center_info.arrived_date + timezone.timedelta(hours=5)


    def get_parent_first_name(self,obj):
        try:
            return obj.juvenile.parentinfojuvenile_set.first().parent.first().first_name
        except:
            return None
    def get_parent_last_name(self,obj):
        try:
            return obj.juvenile.parentinfojuvenile_set.first().parent.first().last_name
        except:
            return None
    def get_parent_father_name(self,obj):
        try:
            return obj.juvenile.parentinfojuvenile_set.first().parent.first().father_name
        except:
            return None
    def get_distributed_info(self,obj):
        try:
            distribute = obj.distributed_info.distributes.first()
            result = {
                'distribution_type':get_distribution_type_choice(obj.distributed_info.distribution_type),
                'pinfl':distribute.pinfl,
                'first_name':distribute.first_name,
                'last_name': distribute.last_name,
                'father_name': distribute.father_name,
            }
            return result
        except:
            return None




class JuvenileNoEducationListSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='juvenile.id')
    birth_district = serializers.CharField(source='birth_district.name', read_only=True)  # Change 'name' to the actual field you want to display
    foreign_country = serializers.SerializerMethodField()
    passport_type = serializers.SerializerMethodField()
    class Meta:
        model = models.PersonalInfoJuvenile
        exclude = ('juvenile','created_at','updated_at','created_by','updated_by')  # Exclude fields you don't want in the CSV


    def get_passport_type(self,instance):
        if instance.passport_type == '1':
            return 'Biometrik pasport'
        if instance.passport_type == '2':
            return 'ID-karta'
        if instance.passport_type == '3':
            return "Tug'ilganlik haqida guvohnoma"
        if instance.passport_type == '4':
            return "Kinder pasport"
        if instance.passport_type == '5':
            return "Horijiy davlat hujjatlari"
        if instance.passport_type == '6':
            return "Boshqalar"

    def get_foreign_country(self, instance):
        # Check if foreign_country is not None before accessing its name attribute
        return instance.foreign_country.name if instance.foreign_country else None
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.photo:
            data['photo'] = self.context['request'].build_absolute_uri(instance.photo.url)
        if instance.reference_type:
            data['reference_type'] = self.context['request'].build_absolute_uri(instance.reference_type.url)
        return data



class UnidentifiedJuvenileForNewStatusListSerializer(serializers.ModelSerializer):
    birth_district = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    time_arrival_center = serializers.SerializerMethodField()
    time_departure_center = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    birth_region = serializers.SerializerMethodField()

    class Meta:
        model = models.UnidentifiedJuvenile
        fields = (
            "id",
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'gender',
            'birth_district',
            'birth_region',
            'time_arrival_center',
            'time_departure_center',
            'status',
            'photo'
        )
    def get_photo(self, obj):
        request = self.context.get("request")
        if obj.photo is not None:
            return request.build_absolute_uri(obj.photo.url)
        return None
    def get_birth_district(self, obj):
        if obj.birth_district is not None:
            district_id = obj.birth_district_id
            district_name = obj.birth_district.name

            district = {
                "id": district_id,
                "name": district_name,
            }
            return district
        return None
    def get_birth_region(self, obj):
        if obj.birth_district is not None:
            region_id = obj.birth_district.region_id.id
            region_name = obj.birth_district.region_id.name

            region = {
                "id": region_id,
                "name": region_name,
            }
            return region
        return None
    def get_status(self, obj):
        data = {
            "text": 'Aniqlanmagan'
        }
        return data

    def get_time_departure_center(self, obj):
        return None
    def get_time_arrival_center(self,obj):
        return obj.created_at.date()



class UnidentifiedJuvenileForNewStatusDetailSerializer(serializers.ModelSerializer):
    birth_district = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    time_arrival_center = serializers.SerializerMethodField()
    time_departure_center = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    birth_region = serializers.SerializerMethodField()

    class Meta:
        model = models.UnidentifiedJuvenile
        fields = (
            "id",
            'first_name',
            'last_name',
            'father_name',
            'birth_date',
            'gender',
            'birth_district',
            'birth_region',
            'time_arrival_center',
            'time_departure_center',
            'status',
            'photo'
        )
    def get_photo(self, obj):
        request = self.context.get("request")
        if obj.photo is not None:
            return request.build_absolute_uri(obj.photo.url)
        return None
    def get_birth_district(self, obj):
        if obj.birth_district is not None:
            district_id = obj.birth_district_id
            district_name = obj.birth_district.name

            district = {
                "id": district_id,
                "name": district_name,
            }
            return district
        return None
    def get_birth_region(self, obj):
        if obj.birth_district is not None:
            region_id = obj.birth_district.region_id.id
            region_name = obj.birth_district.region_id.name

            region = {
                "id": region_id,
                "name": region_name,
            }
            return region
        return None
    def get_status(self, obj):
        data = {
            "text": 'Aniqlanmagan'
        }
        return data

    def get_time_departure_center(self, obj):
        return None
    def get_time_arrival_center(self,obj):
        return obj.created_at.date()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation['id'],
            'personal_info': {
            "first_name": representation["first_name"],
            "last_name": representation["last_name"],
            "father_name": representation["father_name"],
            "birth_date": representation["birth_date"],
            "gender": representation["gender"],
            "birth_district": representation["birth_district"],
            "birth_region": representation["birth_region"],
            "time_arrival_center": representation["time_arrival_center"],
            "time_departure_center": representation["time_departure_center"],
            "status": representation["status"],
            "photo": representation["photo"],
            }
        }

class PsychologyConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PsychologyCondition
        fields = ['id','title']





class JuvenileMarkazListByProphylacticInspectorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    father_name = serializers.CharField(read_only=True)
    class Meta:
        model = models.Juvenile_Markaz
        fields = ['id','first_name','last_name','father_name']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        distribution_type = enums.DISTRIBUTION_TYPE_CHOICE[int(instance.distribute_info.distribution_type) - 1]
        distribution_file = instance.distribute_info.basis_sending_file
        representation['distribution_time'] = instance.distribute_info.created_at
        representation['distribution_type'] = {
            "id": distribution_type[0],
            "text": distribution_type[1]
        }
        if distribution_file:
            with open(distribution_file.path, 'rb') as f:
                file_data = f.read()
                base64_encoded_file = base64.b64encode(file_data).decode('utf-8')
                return f'data:{distribution_file.file.content_type};base64,{base64_encoded_file}'
        else:
            return None

        return representation


class JuvenilesInfoByProphylacticInspectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProphylacticInspector
        fields = ['id','first_name','last_name','father_name',]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        juvenile_markazs = models.Juvenile_Markaz.objects.filter(
            accept_center_info__inspector = instance).exclude(distributed_info=None).annotate(
            first_name = F('juvenile__juvenile__first_name'),
            last_name=F('juvenile__juvenile__last_name'),
            father_name=F('juvenile__juvenile__father_name'),

        )
        representation['juvenile_markazs'] = JuvenileMarkazListSerializer(juvenile_markazs,many=True).data
        return representation
