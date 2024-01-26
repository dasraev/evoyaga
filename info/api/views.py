import requests
from country_regions.models import Country
from django.shortcuts import get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from info.models import District, Region, Markaz, MarkazTuman, MedicalList, SubReasonBringingChild, ReasonBringingChild, Mahalla, \
    Kindergarten, School, University, SpecialEducation, Litsey, VocationalSchool, College, Texnikum
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from . import serializers


# Region Viewset
class RegionViewset(ModelViewSet):
    queryset = Region.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.RegionCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.RegionUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.RegionListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.RegionDetailSerializer
        return serializer_class


class RegionForDeveloper(APIView):
    # permission_classes = [AllowAny]
    queryset = Region.objects.all()

    def post(self, request, format=None):
        serializer = serializers.RegionCreateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# District Viewset
class DistrictViewset(ModelViewSet):
    queryset = District.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.DistrictCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.DistrictUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.DistrictListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.DistrictDetailSerializer
        return serializer_class

    @action(methods=['get'], detail=False)
    def ByRegionId(self, request, **kwargs):
        try:
            param_region = request.query_params['region']
            region_id = get_object_or_404(Region, pk=param_region)
            response = District.objects.all().filter(region_id=region_id)
            serializer = serializers.DistrictListSerializer(response, many=True)
            return Response(serializer.data)
        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DistrictForDeveloper(APIView):
    # permission_classes = [AllowAny]
    queryset = District.objects.all()

    def post(self, request, format=None):
        serializer = serializers.DistrictCreateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Mahalla Viewset
class MahallaViewset(ModelViewSet):
    queryset = Mahalla.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.MahallaCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.MahallaUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.MahallaListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.MahallaDetailSerializer
        return serializer_class

    @action(methods=['get'], detail=False)
    def ByDistrictId(self, request, **kwargs):
        try:
            param_distirct = request.query_params['district']
            district_id = get_object_or_404(District, pk=param_distirct)
            response = Mahalla.objects.all().filter(district_id=district_id)
            serializer = serializers.MahallaListSerializer(response, many=True)
            return Response(serializer.data)
        except MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Kindergarten Viewset
class KindergartenViewset(ModelViewSet):
    queryset = Kindergarten.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.KindergartenCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.KindergartenUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.KindergartenListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.KindergartenDetailSerializer
        return serializer_class

    @action(methods=['get'], detail=False)
    def ByDistrictId(self, request, **kwargs):
        try:
            param_distirct = request.query_params['district']
            district_id = get_object_or_404(District, pk=param_distirct)
            response = Kindergarten.objects.all().filter(district_id=district_id)
            serializer = serializers.KindergartenListSerializer(response, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# School Viewset
class SchoolViewset(ModelViewSet):
    queryset = School.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.SchoolCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.SchoolUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.SchoolListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.SchoolDetailSerializer
        return serializer_class

    @action(methods=['get'], detail=False)
    def ByDistrictId(self, request, **kwargs):
        try:
            param_distirct = request.query_params['district']
            district_id = get_object_or_404(District, pk=param_distirct)
            response = School.objects.all().filter(district_id=district_id)
            serializer = serializers.SchoolListSerializer(response, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# University Viewset
class UniversityViewset(ModelViewSet):
    queryset = University.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.UniversityCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.UniversityUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.UniversityListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.UniversityDetailSerializer
        return serializer_class

    @action(methods=['get'], detail=False)
    def ByRegionId(self, request, **kwargs):
        try:
            param_region = request.query_params['region']
            region_id = get_object_or_404(Region, pk=param_region)
            response = University.objects.all().filter(region_id=region_id)
            serializer = serializers.UniversityListSerializer(response, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Special Education Viewset
class SpecialEducationViewset(ModelViewSet):
    queryset = SpecialEducation.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.SpecialEducationCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.SpecialEducationUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.SpecialEducationListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.SpecialEducationDetailSerializer
        return serializer_class

    @action(methods=['get'], detail=False)
    def ByRegionId(self, request, **kwargs):
        try:
            param_region = request.query_params['region']
            region_id = get_object_or_404(Region, pk=param_region)
            response = SpecialEducation.objects.all().filter(region_id=region_id)
            serializer = serializers.SpecialEducationListSerializer(response, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Litsey Viewset
class LitseyViewset(ModelViewSet):
    queryset = Litsey.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.LitseyCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.LitseyUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.LitseyListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.LitseyDetailSerializer
        return serializer_class

    @action(methods=['get'], detail=False)
    def ByRegionId(self, request, **kwargs):
        try:
            param_region = request.query_params['region']
            region_id = get_object_or_404(Region, pk=param_region)
            response = Litsey.objects.all().filter(region_id=region_id)
            serializer = serializers.LitseyListSerializer(response, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Vocational School Viewset
class VocationalSchoolViewset(ModelViewSet):
    queryset = VocationalSchool.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.VocationalSchoolCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.VocationalSchoolUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.VocationalSchoolListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.VocationalSchoolDetailSerializer
        return serializer_class

    @action(methods=['get'], detail=False)
    def ByRegionId(self, request, **kwargs):
        try:
            param_region = request.query_params['region']
            region_id = get_object_or_404(Region, pk=param_region)
            response = VocationalSchool.objects.all().filter(region_id=region_id)
            serializer = serializers.VocationalSchoolListSerializer(response, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# College Viewset
class CollegeViewset(ModelViewSet):
    queryset = College.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.CollegeCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.CollegeUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.CollegeListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.CollegeDetailSerializer
        return serializer_class

    @action(methods=['get'], detail=False)
    def ByRegionId(self, request, **kwargs):
        try:
            param_region = request.query_params['region']
            region_id = get_object_or_404(Region, pk=param_region)
            response = College.objects.all().filter(region_id=region_id)
            serializer = serializers.CollegeListSerializer(response, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Texnikum Viewset
class TexnikumViewset(ModelViewSet):
    queryset = Texnikum.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.TexnikumCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.TexnikumUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.TexnikumListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.TexnikumDetailSerializer
        return serializer_class

    @action(methods=['get'], detail=False)
    def ByRegionId(self, request, **kwargs):
        try:
            param_region = request.query_params['region']
            region_id = get_object_or_404(Region, pk=param_region)
            response = Texnikum.objects.all().filter(region_id=region_id)
            serializer = serializers.TexnikumListSerializer(response, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Markaz Viewset
class MarkazViewset(ModelViewSet):
    queryset = Markaz.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.MarkazCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.MarkazUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.MarkazListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.MarkazDetailSerializer
        return serializer_class

    def create(self, request, *args, **kwargs):
        region_id = request.data['region']
        try:
            is_have_Markaz = Markaz.objects.get(
                region=region_id)
        except Markaz.DoesNotExist:
            is_have_Markaz = None

        if is_have_Markaz:
            return Response({"message": "Bu hududga markaz allaqachon qo'shilgan"}, status=status.HTTP_400_BAD_REQUEST)
        response = super().create(request, *args, **kwargs)
        return Response({"message": "Markaz muvaffaqqiyatli qo'shildi"}, status=status.HTTP_201_CREATED)
    def get_queryset(self):
        user = self.request.user
        request_code = user.groups.all()[0].code
        if request_code == 2:
            return Markaz.objects.filter(region = user.markaz.region)
        return Markaz.objects.all()


class MarkazTumanViewset(ModelViewSet):
    queryset = MarkazTuman.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.MarkazTumanCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.MarkazTumanUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.MarkazTumanListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.MarkazTumanDetailSerializer
        return serializer_class

    def create(self, request, *args, **kwargs):
        district_id = request.data['district']
        try:
            is_have_Markaz = MarkazTuman.objects.get(
                district=district_id)
        except MarkazTuman.DoesNotExist:
            is_have_Markaz = None
        if is_have_Markaz:
            return Response({"message": "Bu hududga markaz allaqachon qo'shilgan"}, status=status.HTTP_400_BAD_REQUEST)
        super().create(request, *args, **kwargs)
        return Response({"message": "Markaz muvaffaqqiyatli qo'shildi"}, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        region_id = self.request.GET.get('region_id', None)
        user = self.request.user
        request_code = user.groups.all()[0].code
        if request_code == 2:
            markaz_tumans = MarkazTuman.objects.filter(district__region_id = user.markaz.region)
        elif region_id:
            markaz_tumans = MarkazTuman.objects.filter(district__region_id_id=region_id)
        else:
            markaz_tumans = MarkazTuman.objects.all()
        serializer = serializers.MarkazTumanListSerializer(markaz_tumans, many=True, context={"request": request})
        return Response(serializer.data)

# Markaz Viewset
class MedicalListViewset(ModelViewSet):
    queryset = MedicalList.objects.all()

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.MedicalListCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.MedicalListUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.MedicalListListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.MedicalListDetailSerializer
        return serializer_class


# Countries List
class CountriesListView(APIView):
    queryset = Country.objects.all()

    def get(self, request):
        countries = Country.objects.all()
        serializer = serializers.CountryListSerializer(countries, many=True)
        return Response({"countries": serializer.data})


# Bolaning markazga olib kelish sababi
class ReasonBringingListView(APIView):
    queryset = ReasonBringingChild.objects.all()

    def get(self, request):
        reason = ReasonBringingChild.objects.all()
        serializer = serializers.ReasonBringingChildListSerializer(reason, many=True)
        return Response({"reason_bringing_child": serializer.data})


class SubReasonBringingChildByParentListView(APIView):
    queryset = SubReasonBringingChild.objects.all()

    def get(self, request):
        parent_id = request.query_params.get('parent', None)
        sub_reason = SubReasonBringingChild.objects.filter(parent_id=parent_id)
        serializer = serializers.SubReasonBringingChildByParentListSerializer(sub_reason, many=True)
        return Response({"sub_reason_bringing_child": serializer.data})