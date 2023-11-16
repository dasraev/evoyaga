from country_regions.models import Country
from rest_framework.serializers import ModelSerializer, StringRelatedField

from info.models import District, Markaz, Region, MedicalList, SubReasonBringingChild, ReasonBringingChild, \
    Kindergarten, School, University, SpecialEducation, Litsey, VocationalSchool, College, Texnikum

from rest_framework.serializers import ModelSerializer, SlugRelatedField

from info.models import District, Markaz, Region, Mahalla, MarkazTuman


# Region Serializer
class RegionListSerializer(ModelSerializer):
    class Meta:
        model = Region
        exclude = ('created_by', 'updated_by',)
        # fields = '__all__'


class RegionDetailSerializer(ModelSerializer):
    class Meta:
        model = Region
        exclude = ('created_by', 'updated_by')


class RegionUpdateSerializer(ModelSerializer):
    class Meta:
        model = Region
        exclude = ('created_by', 'updated_by')


class RegionCreateSerializer(ModelSerializer):
    class Meta:
        model = Region
        exclude = ('created_by', 'updated_by')


# District Serializer
class DistrictListSerializer(ModelSerializer):
    class Meta:
        model = District
        exclude = ('created_by', 'updated_by',)
        # fields = '__all__'


class DistrictDetailSerializer(ModelSerializer):
    class Meta:
        model = District
        exclude = ('created_by', 'updated_by')


class DistrictUpdateSerializer(ModelSerializer):
    class Meta:
        model = District
        exclude = ('created_by', 'updated_by')


class DistrictCreateSerializer(ModelSerializer):
    class Meta:
        model = District
        exclude = ('created_by', 'updated_by')


# Mahalla Serializer
class MahallaListSerializer(ModelSerializer):
    class Meta:
        model = Mahalla
        exclude = ('created_by', 'updated_by',)
        # fields = '__all__'


class MahallaDetailSerializer(ModelSerializer):
    class Meta:
        model = Mahalla
        exclude = ('created_by', 'updated_by')


class MahallaUpdateSerializer(ModelSerializer):
    class Meta:
        model = Mahalla
        exclude = ('created_by', 'updated_by')


class MahallaCreateSerializer(ModelSerializer):
    class Meta:
        model = Mahalla
        exclude = ('created_by', 'updated_by')


# Kindergarten Serializer
class KindergartenListSerializer(ModelSerializer):
    class Meta:
        model = Kindergarten
        exclude = ('created_by', 'updated_by',)
        # fields = '__all__'


class KindergartenDetailSerializer(ModelSerializer):
    class Meta:
        model = Kindergarten
        exclude = ('created_by', 'updated_by')


class KindergartenUpdateSerializer(ModelSerializer):
    class Meta:
        model = Kindergarten
        exclude = ('created_by', 'updated_by')


class KindergartenCreateSerializer(ModelSerializer):
    class Meta:
        model = Kindergarten
        exclude = ('created_by', 'updated_by')


# School Serializer
class SchoolListSerializer(ModelSerializer):
    class Meta:
        model = School
        exclude = ('created_by', 'updated_by',)
        # fields = '__all__'


class SchoolDetailSerializer(ModelSerializer):
    class Meta:
        model = School
        exclude = ('created_by', 'updated_by')


class SchoolUpdateSerializer(ModelSerializer):
    class Meta:
        model = School
        exclude = ('created_by', 'updated_by')


class SchoolCreateSerializer(ModelSerializer):
    class Meta:
        model = School
        exclude = ('created_by', 'updated_by')


# University Serializer
class UniversityListSerializer(ModelSerializer):
    class Meta:
        model = University
        exclude = ('created_by', 'updated_by',)


class UniversityDetailSerializer(ModelSerializer):
    class Meta:
        model = University
        exclude = ('created_by', 'updated_by')


class UniversityUpdateSerializer(ModelSerializer):
    class Meta:
        model = University
        exclude = ('created_by', 'updated_by')


class UniversityCreateSerializer(ModelSerializer):
    class Meta:
        model = University
        exclude = ('created_by', 'updated_by')


# Special Education Serializer
class SpecialEducationListSerializer(ModelSerializer):
    class Meta:
        model = SpecialEducation
        exclude = ('created_by', 'updated_by',)


class SpecialEducationDetailSerializer(ModelSerializer):
    class Meta:
        model = SpecialEducation
        exclude = ('created_by', 'updated_by')


class SpecialEducationUpdateSerializer(ModelSerializer):
    class Meta:
        model = SpecialEducation
        exclude = ('created_by', 'updated_by')


class SpecialEducationCreateSerializer(ModelSerializer):
    class Meta:
        model = SpecialEducation
        exclude = ('created_by', 'updated_by')


# Litsey Serializer
class LitseyListSerializer(ModelSerializer):
    class Meta:
        model = Litsey
        exclude = ('created_by', 'updated_by',)


class LitseyDetailSerializer(ModelSerializer):
    class Meta:
        model = Litsey
        exclude = ('created_by', 'updated_by')


class LitseyUpdateSerializer(ModelSerializer):
    class Meta:
        model = Litsey
        exclude = ('created_by', 'updated_by')


class LitseyCreateSerializer(ModelSerializer):
    class Meta:
        model = Litsey
        exclude = ('created_by', 'updated_by')


# Vocational School Serializer
class VocationalSchoolListSerializer(ModelSerializer):
    class Meta:
        model = VocationalSchool
        exclude = ('created_by', 'updated_by',)


class VocationalSchoolDetailSerializer(ModelSerializer):
    class Meta:
        model = VocationalSchool
        exclude = ('created_by', 'updated_by')


class VocationalSchoolUpdateSerializer(ModelSerializer):
    class Meta:
        model = VocationalSchool
        exclude = ('created_by', 'updated_by')


class VocationalSchoolCreateSerializer(ModelSerializer):
    class Meta:
        model = VocationalSchool
        exclude = ('created_by', 'updated_by')


# College Serializer
class CollegeListSerializer(ModelSerializer):
    class Meta:
        model = College
        exclude = ('created_by', 'updated_by',)


class CollegeDetailSerializer(ModelSerializer):
    class Meta:
        model = College
        exclude = ('created_by', 'updated_by')


class CollegeUpdateSerializer(ModelSerializer):
    class Meta:
        model = College
        exclude = ('created_by', 'updated_by')


class CollegeCreateSerializer(ModelSerializer):
    class Meta:
        model = College
        exclude = ('created_by', 'updated_by')


# Texnikum Serializer
class TexnikumListSerializer(ModelSerializer):
    class Meta:
        model = Texnikum
        exclude = ('created_by', 'updated_by',)


class TexnikumDetailSerializer(ModelSerializer):
    class Meta:
        model = Texnikum
        exclude = ('created_by', 'updated_by')


class TexnikumUpdateSerializer(ModelSerializer):
    class Meta:
        model = Texnikum
        exclude = ('created_by', 'updated_by')


class TexnikumCreateSerializer(ModelSerializer):
    class Meta:
        model = Texnikum
        exclude = ('created_by', 'updated_by')


# Markaz Serializer
class MarkazListSerializer(ModelSerializer):
    region = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Markaz
        exclude = ('created_by', 'updated_by')


class MarkazDetailSerializer(ModelSerializer):
    class Meta:
        model = Markaz
        exclude = ('created_by', 'updated_by')


class MarkazUpdateSerializer(ModelSerializer):
    class Meta:
        model = Markaz
        exclude = ('created_by', 'updated_by')


class MarkazCreateSerializer(ModelSerializer):
    class Meta:
        model = Markaz
        exclude = ('created_by', 'updated_by')

# MarkazTuman Serializer
class MarkazTumanListSerializer(ModelSerializer):
    district = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = MarkazTuman
        exclude = ('created_by', 'updated_by')


class MarkazTumanDetailSerializer(ModelSerializer):
    class Meta:
        model = MarkazTuman
        exclude = ('created_by', 'updated_by')


class MarkazTumanUpdateSerializer(ModelSerializer):
    class Meta:
        model = MarkazTuman
        exclude = ('created_by', 'updated_by')


class MarkazTumanCreateSerializer(ModelSerializer):
    class Meta:
        model = MarkazTuman
        exclude = ('created_by', 'updated_by')


# MedicalList Serializer
class MedicalListListSerializer(ModelSerializer):
    class Meta:
        model = MedicalList
        exclude = ('created_by', 'updated_by')


class MedicalListDetailSerializer(ModelSerializer):
    class Meta:
        model = MedicalList
        exclude = ('created_by', 'updated_by')


class MedicalListUpdateSerializer(ModelSerializer):
    class Meta:
        model = MedicalList
        exclude = ('created_by', 'updated_by')


class MedicalListCreateSerializer(ModelSerializer):
    class Meta:
        model = MedicalList
        exclude = ('created_by', 'updated_by')


# Country Serializer
class CountryListSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


# Bolaning markazga olib kelish sababi
class ReasonBringingChildListSerializer(ModelSerializer):
    class Meta:
        model = ReasonBringingChild
        fields = ('id', 'title')


class SubReasonBringingChildByParentListSerializer(ModelSerializer):
    parent = SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = SubReasonBringingChild
        fields = ('id', 'title', 'parent')
