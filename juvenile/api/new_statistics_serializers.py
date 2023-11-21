from rest_framework import serializers
from juvenile import models
from django.utils import timezone
from juvenile import models
from rest_framework import serializers
from info.enums import PASSPORT_TYPE_CHOICE


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
    birth_district = serializers.SerializerMethodField()
    parent_first_name = serializers.SerializerMethodField()
    parent_last_name = serializers.SerializerMethodField()
    parent_father_name = serializers.SerializerMethodField()
    distribution_type = serializers.SerializerMethodField()
    distribution_to_whom = serializers.SerializerMethodField()

    class Meta:
        model = models.Juvenile_Markaz
        fields = ['id','created_at','first_name','last_name','father_name','passport_seria','pinfl',
                  'birth_date','birth_district','parent_first_name','parent_father_name',
                  'parent_last_name','markaz_name','distribution_type','distribution_to_whom']


    def get_created_at(self,obj):
        return obj.accept_center_info.created_at + timezone.timedelta(hours=5)

    def get_birth_district(self,obj):
        return f'{obj.juvenile.juvenile.first().birth_district.name}, {obj.juvenile.juvenile.first().birth_district.region_id.name}'

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
    def get_distribution_type(self, obj):
        try:
            distributed_info = obj.distributed_info
            if int(distributed_info.distribution_type) == 1:
                return 'Oila'
            elif int(distributed_info.distribution_type) == 2:
                return 'Vasiylik organi orqali'
            elif int(distributed_info.distribution_type) == 3:
                return 'ITM'
            elif int(distributed_info.distribution_type) == 4:
                return "RO'TM"
            elif int(distributed_info.distribution_type) == 5:
                return "Sog'liqni saqlash muassasasi"
            elif int(distributed_info.distribution_type) == 6:
                return "Boshqa markazga yuborish"
            elif int(distributed_info.distribution_type) == 7:
                return "Boshqa davlatga yuborish"
            elif int(distributed_info.distribution_type) == 8:
                return "Boshqalar"
        except:
            return None

    def get_distribution_to_whom(self, obj):
        try:
            distribution_to_whom = models.DistributionToWhom.objects.get(distribution_info = obj.distributed_info)
            if distribution_to_whom.first_name or distribution_to_whom.last_name or distribution_to_whom.father_name or distribution_to_whom.pinfl:
                return f'{distribution_to_whom.first_name} {distribution_to_whom.last_name} {distribution_to_whom.father_name}, pinfl:{distribution_to_whom.pinfl}'
            else:
                return None
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