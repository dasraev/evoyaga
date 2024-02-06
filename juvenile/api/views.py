import json

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from info import enums
from info.models import Markaz
from juvenile import models
from . import filters as filter
from . import serializers
from .paginations import JuvenilePagination
from notification.api.views import send_notification_other_center
from django.utils import timezone
from rest_framework.permissions import AllowAny
import csv
from django.http import HttpResponse
from django.db.models import Count

# Bola 2 marta bo'lib qolmaslik uchun tekshirish
def check_is_exist_in_center(juvenile_info):
    available = {
        "status": True,
        "message": "Bu bola allaqachon qo'shilgan!"
    }

    not_available = {
        "status": False,
        "message": ""
    }
    first_name = juvenile_info['first_name']
    last_name = juvenile_info['last_name']
    birth_date = juvenile_info['birth_date']

    # Agar bolaning pasporti bo'masa yoki boshqa davlat fuqarosi bo'lsa ism, familiya, tug'ilgan yil bo'yicha qidirib
    # ko'riladi.
    if int(juvenile_info['passport_type']) == 4 or int(juvenile_info['passport_type']) == 5:

        try:
            models.PersonalInfoJuvenile.objects.filter(first_name=first_name, last_name=last_name, birth_date=birth_date)
            return available
        except:
            return not_available
    else:
        try:
            # models.PersonalInfoJuvenile.objects.get(pinfl=juvenile_info['pinfl'])
            # personal_info = models.PersonalInfoJuvenile.objects.get(pinfl=juvenile_info['pinfl'])
            # is_in_markaz = models.Juvenile_Markaz.objects.get(juvenile__juvenile__pinfl=juvenile_info['pinfl'])
            is_in_markaz = models.Juvenile_Markaz.objects.filter(juvenile__juvenile__pinfl=juvenile_info['pinfl']).order_by('-created_at').first()
            # # if is_in_markaz.status == "3":
            #     return not_available
            #
            # return available
            if int(is_in_markaz.status) < 3 or int(is_in_markaz.status) == 10:
                return available
            else:
                return not_available

        except:
            return not_available


# Aniqlangan bolaning ma'lumoti to'liqligini tekshirish
def check_juvenile_information(user_markaz):
    juveniles = models.Juvenile.objects.filter(current_markaz=user_markaz).filter(juvenile_markaz__status=1).order_by(
        '-created_at')
    list_juvenile_ids = []
    for juvenile in juveniles:

        personal_info = models.PersonalInfoJuvenile.objects.filter(
            juvenile=juvenile)

        address_info = models.AddressInfoJuvenile.objects.filter(juvenile=juvenile)

        education_info = models.EducationInfoJuvenile.objects.filter(
            juvenile=juvenile)

        parent_info = models.ParentInfoJuvenile.objects.filter(
            juvenile=juvenile)

        if personal_info:
            for item in personal_info:
                if int(item.passport_type) == 5:
                    list_juvenile_ids.append(item.juvenile_id)
        if personal_info and address_info and education_info and parent_info:
            list_juvenile_ids.append(juvenile.id)

    complete_info_juveniles = models.Juvenile.objects.filter(id__in=list_juvenile_ids)
    return complete_info_juveniles


# Juvenile Viewset
class JuvenileViewset(ModelViewSet):
    pagination_class = JuvenilePagination
    filterset_class = filter.JuvenileFilter

    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all().order_by('-created_at')

        user_markaz = self.request.user.markaz
        # Agar aniqlangan bolaning ma'lumoti to'liq bo'lmasa markazga qabul qilish bo'limida chiqib qolishi kerak emas
        # juveniles = check_juvenile_information(user_markaz)
        juveniles = (models.Juvenile.objects.filter(current_markaz=user_markaz).filter(
            juvenile_markaz__status=1,juvenile__isnull=False,addressinfojuvenile__isnull=False,
            educationinfojuvenile__isnull=False,parentinfojuvenile__isnull=False)
             |models.Juvenile.objects.filter(juvenile__passport_type=5,current_markaz=user_markaz,juvenile_markaz__status=1)).distinct().order_by('-created_at')



        return juveniles

    def get_serializer_class(self):
        serializer_class = serializers.JuvenileListSerializer

        if self.action in ['create']:
            serializer_class = serializers.JuvenileCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.JuvenileUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.JuvenileListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.JuvenileDetailSerializer

        return serializer_class

    def create(self, request, *args, **kwargs):
        user = request.user
        try:
            is_in_identified_list = request.data['is_in_identified_list']
        except:
            is_in_identified_list = False
        try:
            juvenile_id = request.data['juvenile_id']
        except:
            juvenile_id = None
        if request.data['is_identified'] == 'false':
            unidentified_serializers = serializers.UnidentifiedJuvenileCreateSerializer(data=request.data)
            if unidentified_serializers.is_valid():
                first_name = unidentified_serializers.validated_data.get('first_name')
                last_name = unidentified_serializers.validated_data.get('last_name')
                father_name = unidentified_serializers.validated_data.get('father_name')
                birth_date = unidentified_serializers.validated_data.get('birth_date')
                full_name = f'{first_name} {last_name} {father_name}'
                unidentified_juvenile_list = models.UnidentifiedJuvenile.objects.filter(
                    first_name=first_name).filter(last_name=last_name).filter(father_name=father_name).filter(
                    birth_date=birth_date)
                if unidentified_juvenile_list:
                    return Response({"message": f" {full_name} aniqlanmaganlar ro'yxatiga allaqachon qo'shilgan"},
                                    status=status.HTTP_400_BAD_REQUEST)
                unidentified_juvenile = models.UnidentifiedJuvenile.objects.create(
                    **unidentified_serializers.validated_data)

                unidentified_juvenile.created_by = user
                unidentified_juvenile.markaz = user.markaz
                unidentified_juvenile.save()

                return Response({"message": "Bola aniqlanmaganlar ro'yxatiga qo'shildi!"},
                                status=status.HTTP_201_CREATED)
            return Response(unidentified_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        if bool(request.data['is_identified']) == True:
            if bool(is_in_identified_list):
                try:
                    models.UnidentifiedJuvenile.objects.get(pk=juvenile_id).delete()
                except:
                    return Response({"message": "Aniqlanmagan bolaning idsi noto'g'ri!"},
                                    status=status.HTTP_404_NOT_FOUND)
            personal_info_serializer = serializers.PersonalInfoJuvenileCreateSerializer(data=request.data)
            try:
                passport_type = request.data.get('passport_type')
                if int(passport_type) == 5 or int(passport_type) == 6:
                    first_name = request.data.get('first_name')
                    last_name = request.data.get('last_name')
                    father_name = request.data.get('father_name')
                    birth_date = request.data.get('birth_date')
                    personal_info = models.PersonalInfoJuvenile.objects.get(first_name__icontains=first_name,last_name__icontains=last_name,
                                                                            father_name__icontains=father_name,birth_date=birth_date)

                else:
                    if request.data.get("pinfl"):
                        personal_info = models.PersonalInfoJuvenile.objects.get(pinfl=request.data.get("pinfl"))
                    else:
                        personal_info = models.PersonalInfoJuvenile.objects.get(passport_seria=request.data.get('passport_seria'))

            except:
                personal_info = None

            # is_available = check_is_exist_in_center(request.data)
            #
            # if is_available['status']:
            #     passport_type = request.data.get('passport_type')
            #     if passport_type == 4 or passport_type == 5:
            #         personal_info = models.PersonalInfoJuvenile.objects.get()
            #     personal_info = models.PersonalInfoJuvenile.objects.get(pinfl=request.data.get('pinfl'))
            #     juvenile_markaz = models.Juvenile_Markaz.objects.filter(juvenile_id=personal_info.juvenile_id).order_by('-created_at').first()
            #     if juvenile_markaz.status == '1':
            #         message = f"{personal_info.first_name} {personal_info.last_name} {personal_info.father_name} {juvenile_markaz.markaz.name} ga qabul qilingan!"
            #     else:
            #         message = f"{personal_info.first_name} {personal_info.last_name} {personal_info.father_name} {juvenile_markaz.markaz.name} ga qabul qilingan!. Lekin taqsimlanmagan"
            #     return Response({message}, status=status.HTTP_400_BAD_REQUEST)
            if personal_info:
                ######
                # juvenile = models.Juvenile.objects.get(id=personal_info.juvenile_id)
                # juvenile.updated_by = user
                # juvenile.current_markaz = user.markaz
                # juvenile.save()
                #
                # juvenile_markaz = models.Juvenile_Markaz.objects.get(juvenile_id=juvenile.id)
                # juvenile_markaz.status = 1
                # juvenile_markaz.save()
                # return Response({
                #     "message": "Bola aniqlanganlar ro'yxatiga qo'shildi!",
                #     "juvenile_id": juvenile.id
                # }, status=status.HTTP_201_CREATED)

                user = request.user
                juvenile = personal_info.juvenile

                juvenile_markaz = models.Juvenile_Markaz.objects.filter(juvenile=juvenile).order_by(
                    '-created_at').first()
                if int(juvenile_markaz.status) == 1:
                    return Response({f"{personal_info.first_name} {personal_info.last_name} {personal_info.father_name} {juvenile_markaz.markaz.name} ga qabul qilingan"}, status=status.HTTP_400_BAD_REQUEST)
                if int(juvenile_markaz.status) == 2 or int(juvenile_markaz.status) == 10:
                    return Response({f"{personal_info.first_name} {personal_info.last_name} {personal_info.father_name} {juvenile_markaz.markaz.name} ga qabul qilingan, lekin taqsimlanmagan!"}, status=status.HTTP_400_BAD_REQUEST)
                models.Juvenile_Markaz.objects.create(juvenile=juvenile, markaz=user.markaz, status=1)
                juvenile.current_markaz = user.markaz
                # juvenile.accepted_center_number += 1
                juvenile.save()
                return Response({
                    "message": "Bola aniqlanganlar ro'yxatiga qo'shildi!",
                    "juvenile_id": juvenile.id
                }, status=status.HTTP_201_CREATED)


            if personal_info_serializer.is_valid():

                juvenile = models.Juvenile.objects.create()
                personal_info = models.PersonalInfoJuvenile.objects.create(**personal_info_serializer.validated_data,
                                                                           juvenile=juvenile)
                juvenile.created_by = user
                juvenile.current_markaz = user.markaz
                # juvenile.accepted_center_number += 1
                juvenile.save()
                personal_info.save()
                models.Juvenile_Markaz.objects.create(juvenile=juvenile, markaz=user.markaz, status=1)
                return Response({
                    "message": "Bola aniqlanganlar ro'yxatiga qo'shildi!",
                    "juvenile_id": juvenile.id
                }, status=status.HTTP_201_CREATED)
            return Response(personal_info_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        personal_infos = models.PersonalInfoJuvenile.objects.filter(
            juvenile_id=instance.id)
        for personal_info in personal_infos:
            personal_info.delete()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Mavjud bolani aniqlash
    @action(detail=False, methods=['post'])
    def create_available_juvenile(self, request):
        user = request.user
        juvenile_id = self.request.GET.get('juvenile_id', None)

        try:
            juvenile = models.Juvenile.objects.get(pk=juvenile_id)

        except:
            return Response({"message": "Bola mavjud emas!"}, status=status.HTTP_404_NOT_FOUND)
        personal_info = models.PersonalInfoJuvenile.objects.get(juvenile=juvenile)

        juvenile_markaz = models.Juvenile_Markaz.objects.filter(juvenile=juvenile).order_by(
            '-created_at').first()
        if int(juvenile_markaz.status) == 1:
            return Response({
                                f"{personal_info.first_name} {personal_info.last_name} {personal_info.father_name} {juvenile_markaz.markaz.name} ga qabul qilingan"},
                            status=status.HTTP_400_BAD_REQUEST)
        if int(juvenile_markaz.status) == 2 or int(juvenile_markaz.status) == 10:
            return Response({
                                f"{personal_info.first_name} {personal_info.last_name} {personal_info.father_name} {juvenile_markaz.markaz.name} ga qabul qilingan, lekin taqsimlanmagan!"},
                            status=status.HTTP_400_BAD_REQUEST)
        models.Juvenile_Markaz.objects.create(juvenile=juvenile, markaz=user.markaz, status=1)
        juvenile.current_markaz = user.markaz
        # juvenile.accepted_center_number += 1
        juvenile.save()
        return Response({
            "message": "Bola aniqlanganlar ro'yxatiga qo'shildi!",
            "juvenile_id": juvenile.id
        }, status=status.HTTP_201_CREATED)





        # user = request.user
        # juvenile_id = self.request.GET.get('juvenile_id', None)
        # try:
        #     juvenile = models.Juvenile.objects.get(pk=juvenile_id)
        # except:
        #     return Response({"message": "Bola mavjud emas!"}, status=status.HTTP_404_NOT_FOUND)
        #
        # juvenile_markaz = models.Juvenile_Markaz.objects.filter(juvenile=juvenile).order_by('-created_at').first()
        #
        # # if juvenile_markaz.status == '1':
        # #     return Response({"Bu bola hali taqsimlanmagan!"}, status=status.HTTP_400_BAD_REQUEST)
        #
        # if int(juvenile_markaz.status) < 3 or int(juvenile_markaz.status) == 10:
        #     return Response({"Bu bola hali taqsimlanmagan!"}, status=status.HTTP_400_BAD_REQUEST)
        # models.Juvenile_Markaz.objects.create(juvenile_id=juvenile_id, markaz=user.markaz, status=1)
        # juvenile.current_markaz = user.markaz
        # juvenile.save()
        # return Response({"Bola markazga muvaffaqqiyatli qabul qilindi!"})




    @action(detail=True, methods=['put'])
    def juvenile_personalinfo_update(self, request, pk=None):
        try:
            juvenile = models.Juvenile.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance = models.PersonalInfoJuvenile.objects.get(juvenile=juvenile)
        serializer = serializers.PersonalInfoJuvenileUpdateSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def juvenile_addressinfo_create_or_update(self, request, pk=None):
        try:
            juvenile = models.Juvenile.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            address_info = models.AddressInfoJuvenile.objects.get(juvenile=juvenile)
            serializer = serializers.AddressInfoJuvenileCreateSerializer(address_info, data=request.data)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(juvenile=juvenile).order_by('-created_at').first()
            # if juvenile_markaz.markaz != request.user.markaz:
            #     return Response("Malumotlarni o'zgartira olmaysiz,bola boshqa markaz tomonidan qo'shilgan", status=status.HTTP_401_UNAUTHORIZED)
        except ObjectDoesNotExist:
            serializer = serializers.AddressInfoJuvenileCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(juvenile=juvenile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post','put'])
    def juvenile_educationinfo_create_or_update(self, request, pk=None):
        try:
            juvenile = models.Juvenile.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            education_info = models.EducationInfoJuvenile.objects.get(juvenile = juvenile)
            serializer = serializers.EducationInfoJuvenileCreateSerializer(education_info,data = request.data)
            # juvenile_markaz = models.Juvenile_Markaz.objects.filter(juvenile = juvenile).order_by('-created_at').first()
            # if juvenile_markaz.markaz != request.user.markaz:
            #     return Response("Malumotlarni o'zgartira olmaysiz,bola boshqa markaz tomonidan qo'shilgan", status=status.HTTP_401_UNAUTHORIZED)

        except ObjectDoesNotExist:
            serializer = serializers.EducationInfoJuvenileCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(juvenile=juvenile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def juvenile_parentinfo_create_or_update(self, request, pk=None):
        try:
            juvenile = models.Juvenile.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # serializer = serializers.ParentInfoJuvenileCreateSerializer(data=request.data)
        try:
            parent_info = models.ParentInfoJuvenile.objects.get(juvenile=juvenile)
            serializer = serializers.ParentInfoJuvenileCreateSerializer(parent_info, data=request.data)
        except ObjectDoesNotExist:
            serializer = serializers.ParentInfoJuvenileCreateSerializer(data = request.data)

        if serializer.is_valid():
            # parent_info = models.ParentInfoJuvenile.objects.create(**serializer.validated_data, juvenile=juvenile)
            # parent_info.save()
            parent_info = serializer.save(juvenile=juvenile)
            return Response({"id": parent_info.id, "data": serializer.data}, status=status.HTTP_201_CREATED)
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Aniqlanmangan bolalar ro'yxati
    @action(detail=False)
    def unidentified_juveniles(self, request):
        user_markaz = request.user.markaz
        unidentified_juveniles = models.UnidentifiedJuvenile.objects.filter(
            markaz=user_markaz)

        page = self.paginate_queryset(unidentified_juveniles)
        if page is not None:
            serializer = serializers.UnidentifiedJuvenileListSerializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)

        serializer = serializers.UnidentifiedJuvenileListSerializer(unidentified_juveniles, many=True,
                                                                    context={"request": request})
        return Response(serializer.data)

    # Aniqlangan bolalar shaxsiy ma'lumotlari ro'yxati
    @action(detail=False)
    def juvenile_personal_info(self, request):
        user = request.user
        juveniles = models.Juvenile.objects.filter(juvenile_markaz__markaz=user.markaz)

        page = self.paginate_queryset(juveniles)
        if page is not None:
            serializer = serializers.JuvenileListPersonalInfoSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = serializers.JuvenileListPersonalInfoSerializer(juveniles, many=True, context={'request': request})
        return Response(serializer.data)

    # Aniqlangan bolalarning ma'lumotlari to'liq to'ldirilmaganlar ro'yxati
    @action(detail=False)
    def incomplete_juveniles(self, request):
        full_name = request.GET.get('full_name')
        birth_date = request.GET.get('birth_date')
        birth_district = request.GET.get('birth_district')
        birth_region = request.GET.get('birth_region')
        user = request.user
        incomplete_juveniles = models.Juvenile.objects.filter(
            Q(juvenile_markaz__markaz=user.markaz) and (
                    Q(addressinfojuvenile=None) | Q(educationinfojuvenile=None) | Q(parentinfojuvenile=None))
        ).exclude(juvenile__passport_type='5')

        if full_name:
            for term in full_name.split():
                incomplete_juveniles = incomplete_juveniles.filter(
                    Q(juvenile__first_name__icontains=term) | Q(juvenile__last_name__icontains=term) | Q(juvenile__father_name__icontains=term)).exclude(juvenile__passport_type='5')
        if birth_date:
                incomplete_juveniles = incomplete_juveniles.filter(juvenile__birth_date=birth_date)
        if birth_district:
            incomplete_juveniles = incomplete_juveniles.filter(juvenile__birth_district=birth_district)
        if birth_region:
            incomplete_juveniles = incomplete_juveniles.filter(juvenile__birth_district__region_id=birth_region)



        page = self.paginate_queryset(incomplete_juveniles)
        if page is not None:
            serializer = serializers.JuvenileListPersonalInfoSerializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)
        serializer = serializers.JuvenileListPersonalInfoSerializer(incomplete_juveniles, many=True,
                                                                    context={"request": request})
        return Response(serializer.data)

    # def juvenile_personal_info(self, request):
    #     user = request.user
    #     juveniles = models.Juvenile.objects.filter(juvenile_markaz__markaz=user.markaz)
    #
    #     page = self.paginate_queryset(juveniles)
    #     if page is not None:
    #         serializer = serializers.JuvenileListPersonalInfoSerializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = serializers.JuvenileListPersonalInfoSerializer(juveniles, many=True)
    #     return Response(serializer.data)

    @action(detail=True, methods=['DELETE'])
    def delete_incomplete_juvenile(self, request, pk):
        try:
            models.Juvenile.objects.get(pk=pk)
        except:
            return Response({"message": "juvenile_id is not valid or not found Juvenile!"},
                            status=status.HTTP_400_BAD_REQUEST)
        models.PersonalInfoJuvenile.objects.filter(juvenile_id=pk).delete()
        models.AddressInfoJuvenile.objects.filter(juvenile_id=pk).delete()
        models.EducationInfoJuvenile.objects.filter(juvenile_id=pk).delete()
        models.ParentInfoJuvenile.objects.filter(juvenile_id=pk).delete()
        models.Juvenile.objects.get(pk=pk).delete()
        return Response({"message": "Yakunlanmagan bola o'chirildi!"}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['DELETE'])
    def delete_unidentified_juvenile(self, request, pk):
        try:
            models.UnidentifiedJuvenile.objects.get(pk=pk)
        except:
            return Response(
                {"message": "unidentified_juvenile_id is not valid or not found Unidentified juvenile id!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        models.UnidentifiedJuvenile.objects.get(pk=pk).delete()
        return Response({"message": "Shaxsi aniqlanmagan bola o'chirildi!"}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True)
    def juvenile_personal_info_detail(self, request, pk=None):
        user = request.user
        queryset = models.Juvenile.objects.filter(juvenile_markaz__markaz=user.markaz)
        juvenile = get_object_or_404(queryset, pk=pk)
        serializer = serializers.JuvenileDetailPersonalInfoSerializer(juvenile)
        return Response(serializer.data)

    @action(detail=True)
    def juvenile_info_detail(self, request, pk=None):
        user = request.user

        queryset = models.Juvenile.objects.get(pk=pk)
        serializer = serializers.JuvenileInfosDetailSerializer(queryset, context={"request": request})
        return Response(serializer.data)

    # Bola database da bor yo'qligini tekshirish (oldin markazga tushganmi tushmaganmi)
    @action(detail=False, methods=['get'])
    def search_juvenile(self, request, *args, **kwargs):
        pinfl = self.request.GET.get('juvenile_pinfl', None)
        first_name = self.request.GET.get('first_name', None)
        last_name = self.request.GET.get('last_name', None)
        birth_date = self.request.GET.get('birth_date', None)

        if pinfl:
            try:
                personal_info = models.PersonalInfoJuvenile.objects.get(pinfl=pinfl)
                juvenile = models.Juvenile.objects.get(pk=personal_info.juvenile_id)
            except:
                return Response({"message": "Bola topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
            serializer = serializers.JuvenileListPersonalInfoSerializer(juvenile, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        if first_name and last_name and birth_date:
            try:
                personal_info = models.PersonalInfoJuvenile.objects.get(first_name=first_name, last_name=last_name,
                                                                        birth_date=birth_date)
                juvenile = models.Juvenile.objects.get(pk=personal_info.juvenile_id)
                serializer = serializers.JuvenileListPersonalInfoSerializer(juvenile, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"message": "Bola mavjud emas!"}, status=status.HTTP_404_NOT_FOUND)


        return Response(
            {
                "message": " query_param: juvenile_pinfl yoki first_name, last_name, birth_date mavjud emas!"
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=True, methods=['put'])
    def edit_juvenile(self, request, pk=None):
        try:
            instance = models.Juvenile.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.JuvenileUpdateSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Accept to center juvenile
    @action(detail=False, methods=['post'])
    def accept_juvenile(self, request, *args, **kwargs):
        request.data._mutable = True
        inspector = json.loads(request.data.pop('prophylactic_inspector')[0])
        medical_list = json.loads(request.data.pop('medical_list')[0])
        juvenile_id = self.request.GET.get('juvenile_id', None)
        request.data._mutable = False

        try:
            juvenile = models.Juvenile.objects.get(id=juvenile_id)
        except:

            return Response(
                {"message": "Juvenile id not valid!"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.JuvenileAcceptCenterInfoCreateSerializer(
            data=request.data)


        inspector_serializer = serializers.ProphylacticInspectorCreateSerializer(data=inspector)

        if serializer.is_valid():
            if inspector_serializer.is_valid():
                juvenile = models.Juvenile.objects.get(id=juvenile_id)
                pinfl = inspector_serializer.validated_data.get('pinfl', None)
                try:
                    inspector_obj = models.ProphylacticInspector.objects.get(pinfl=pinfl)
                except ObjectDoesNotExist:
                    inspector_obj = models.ProphylacticInspector.objects.create(
                        **inspector_serializer.validated_data)
                accept_info = models.JuvenileAcceptCenterInfo.objects.create(
                    **serializer.validated_data)
                accept_info.inspector = inspector_obj

                for item in medical_list:
                    models.JuvenileMedicalList.objects.create(medical_list_id=item, accept_center_info=accept_info)
                juvenile_markaz = models.Juvenile_Markaz.objects.filter(juvenile=juvenile).order_by(
                    '-created_at').first()
                juvenile_markaz.accept_center_info = accept_info
                juvenile_markaz.status = 2
                juvenile.accepted_center_number += 1
                juvenile.current_markaz = juvenile_markaz.markaz
                juvenile_markaz.save()
                accept_info.save()
                juvenile.save()
                return Response({
                    'message': 'Bola markazga muvaffaqqiyatli qabul qilindi!'
                }, status=status.HTTP_201_CREATED)
                request.data._mutable = False
            else:
                return Response(
                    {"inspector": inspector_serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def distribute(self, juvenile_markaz, distributed_info, juvenile_status, message,first_name=None,last_name=None,father_name=None,pinfl=None):
        juvenile_markaz.distributed_info = distributed_info
        juvenile_markaz.status = juvenile_status
        juvenile_markaz.time_departure_center = distributed_info.created_at
        distributed_info.save()
        juvenile_markaz.save()
        distribution_to_whom = models.DistributionToWhom.objects.create(distribution_info=distributed_info,
                                                                        first_name=first_name,
                                                                        last_name=last_name,
                                                                        father_name=father_name,
                                                                        pinfl=pinfl)



        return Response(
            {'message': message}, status=status.HTTP_201_CREATED)

    # Distribute juvenile
    @action(detail=False, methods=['post'])
    def distribute_juvenile(self, request, *args, **kwargs):
        user = request.user
        serializer = serializers.JuvenileDistributedInfoCreateSerializer(data=request.data)
        if serializer.is_valid():
            juvenile_id = self.request.GET.get('juvenile_id', None)
            monitoring_markaz_tuman = request.data.get('monitoring_markaz_tuman')
            distribution_type = serializer.validated_data.get('distribution_type')
            receiver_center = serializer.validated_data.get('markaz')
            try:
                juvenile = models.Juvenile.objects.get(id=juvenile_id)
            except:
                return Response(
                    {"message": "Juvenile id not valid!"},
                    status=status.HTTP_400_BAD_REQUEST)
            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                juvenile=juvenile).order_by('-created_at').first()
            if juvenile_markaz.distributed_info is None:
                distributed_info = models.JuvenileDistributedInfo.objects.create(**serializer.validated_data)
                juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                    juvenile=juvenile).order_by('-created_at').first()

                first_name = request.data.get('first_name')
                last_name = request.data.get('last_name')
                father_name = request.data.get('father_name')
                pinfl = request.data.get('pinfl')

                if distribution_type == 6:
                    if receiver_center == None:
                        return Response({'message': f"Yubormoqchi bo'lgan markazni tanlamadingiz!"},
                                        status=status.HTTP_400_BAD_REQUEST)

                    if user.markaz == receiver_center:
                        return Response({'message': f"Bolani '{receiver_center}' ga yuborib bo'lmaydi"},
                                        status=status.HTTP_400_BAD_REQUEST)


                    message = f'Bola {receiver_center} ga yuborildi'
                    send_notification_other_center(juvenile, user, receiver_center)
                    return self.distribute(juvenile_markaz, distributed_info, 10, message)
                if distribution_type == 7:
                    message = f'Bola boshqa davlatga yuborildi'
                    return self.distribute(juvenile_markaz, distributed_info, 7, message)

                if monitoring_markaz_tuman:
                    juvenile_markaz.monitoring_markaz_tuman_id = monitoring_markaz_tuman
                    juvenile_markaz.save()
                message = f'Bola taqsimlandi!'
                return self.distribute(juvenile_markaz, distributed_info, 3, message)
            else:
                return Response({"message": "Bu bola allaqachon taqsimlangan!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # Monitoring info
    @action(detail=False, methods=['post'])
    def add_monitoring_info(self, request, *args, **kwargs):
        serializer = serializers.JuvenileMonitoringInfoCreateSerializer(data=request.data)
        if serializer.is_valid():
            juvenile_id = self.request.GET.get('juvenile_id', None)
            try:
                juvenile = models.Juvenile.objects.get(id=juvenile_id)
            except:
                return Response(
                    {"message": "Juvenile id not valid!"},
                    status=status.HTTP_400_BAD_REQUEST)

            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                juvenile=juvenile).order_by('-created_at').first()

            if juvenile_markaz.monitoring_info is None:
                monitoring_info = models.JuvenileMonitoringInfo.objects.create(**serializer.validated_data)

                juvenile_markaz.monitoring_info = monitoring_info
                monitoring_status = serializer.validated_data.get('monitoring_status')
                if monitoring_status == 1:
                    juvenile_markaz.status = 4
                if monitoring_status == 2:
                    juvenile_markaz.status = 5
                elif monitoring_status == 3:
                    juvenile_markaz.status = 11
                elif monitoring_status == 4:
                    juvenile_markaz.status = 12
                elif monitoring_status == 5:
                    juvenile_markaz.status = 13

                juvenile_markaz.save()

                return Response(
                    {'message': "Monitoring ma'lumotlar muvaffaqqiyatli qo'shildi"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Bu bolada monitoring ma'lumotlar allaqachon mavjud!"},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Employment info
    @action(detail=False, methods=['post'])
    def add_employment_info(self, request, *args, **kwargs):
        serializer = serializers.JuvenileEmploymentInfoCreateSerializer(data=request.data)
        if serializer.is_valid():
            juvenile_id = self.request.GET.get('juvenile_id', None)
            try:
                juvenile = models.Juvenile.objects.get(id=juvenile_id)
            except:
                return Response(
                    {"message": "Juvenile id not valid!"},
                    status=status.HTTP_400_BAD_REQUEST)

            juvenile_markaz = models.Juvenile_Markaz.objects.filter(
                juvenile=juvenile).order_by('-created_at').first()

            if juvenile_markaz.employment_info is None:
                employment_info = models.JuvenileEmploymentInfo.objects.create(**serializer.validated_data)

                juvenile_markaz.employment_info = employment_info
                juvenile_markaz.status = 6

                juvenile_markaz.save()
                return Response(
                    {'message': "Bandlik ma'lumotlar muvaffaqqiyatli qo'shildi"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Bu bolada bandlik ma'lumotlar allaqachon mavjud!"},
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # return list of enums
    @action(detail=False, methods=['get'])
    def passport_types(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.PASSPORT_TYPE_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def school_types(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.SCHOOL_TYPE_CHOICE]
        return Response(values)

    # @action(detail=False, methods=['get'])
    # def get_came_back_center(self, request):
    #     values = [{'id': key, 'text': val} for key, val in enums.COUNT_BACK_CENTER_CHOICE]
    #     return Response(values)

    @action(detail=False, methods=['get'])
    def inspector_types(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.INSPECTOR_TYPE_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def marital_statuses(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.MARITAL_STATUS_TYPE_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def parent_types(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.PARENT_TYPE_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def distribution_types(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.DISTRIBUTION_TYPE_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def level_kindships(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.LEVEL_KINKDSHIP_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def basis_distributions(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.BASIS_DISTRIBUTION_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def type_guardianships(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.TYPE_GUARDIANSHIP_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def itm_directions(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.ITM_DIRECTION_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def rotm_types(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.ROTM_TYPE_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def arrived_reasons(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.ARRIVED_REASON_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def determined_locations(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.DETERMINED_LOCATION_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def have_been_in_itm_reasons(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.HAVE_BEEN_IN_ITM_REASON_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def have_been_in_rotm_reasons(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.HAVE_BEEN_IN_ROTM_REASON_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def juvenile_statuses(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.JUVENILE_STATUS_CHOICES]
        # Shaxsi aniqlanmagan , 2 va undan ortiq kelgan , # Markazda saqlanayotgan
        new_status = [{'id':14,'text':'Shaxsi aniqlanmagan'}, {'id':15,'text':'2 va undan ortiq kelgan'}, {'id':16,'text':'Markazda saqlanayotgan'}]
        values += new_status
        count = 17
        for psychology_condition in models.PsychologyCondition.objects.all().order_by('-created_at'):
            psychology_status = {"id":count,"text":psychology_condition.title}
            count += 1
            values.append(psychology_status)
        # psycholoy_status = [
        #     {"id": 123313, 'text': "Shaxsiy sifatida muammolari mavjud"},
        #     {"id": 18, 'text': "Shaxslararo mulokotda muammosi mavjud"},
        #     {"id": 19, 'text': "Destruktiv xulk atvoriga moyilligi mavjud"},
        #     {"id": 20, 'text': "Аutodestruktiv xulq atvoriga moyilligi mavjud"},
        #     {"id": 21, 'text': "Ijtimoiy psixologik muammosi mavjud bulmagan"},
        #     {"id": 22, 'text': "Emotsional soxasida muammosi mavjud"}
        # ]
        return Response(values)

    @action(detail=False, methods=['get'])
    def employment_education_types(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.EMPLOYMENT_EDUCATION_TYPE_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def foreign_to_whom_given(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.FOREIGN_TO_WHOM_GIVEN_CHOICES]
        return Response(values)

    @action(detail=False, methods=['get'])
    def mastery(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.MASTERY_TYPE_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def characters(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.CHARACTER_TYPE_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def type_healthcare_facility(self, request):
        values = [{'id': key, 'text': val} for key, val in enums.TYPE_HEALTHCARE_FACILITY]
        return Response(values)

    @action(detail=False, methods=['get'])
    def notification_status(self, request):
        values = [{'id': key, 'text': val}
                  for key, val in enums.NOTIFICATION_STATUS_CHOICE]
        return Response(values)

    @action(detail=False, methods=['get'])
    def monitoring_status(self, request):
        values = [{'id': key, 'text': val}
                  for key, val in enums.MONITORING_STATUS_CHOICE]
        return Response(values)


# All reports of Juvenile
class JuvenileReportsListView(generics.ListAPIView):
    # serializer_class = serializers.JuvenileListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = filter.JuvenileReportFilter
    pagination_class = JuvenilePagination
    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile_Markaz.objects.all().order_by('-created_at')

        if user_code == 4:
            markaz_tuman = self.request.user.markaz_tuman
            return models.Juvenile_Markaz.objects.all().filter(monitoring_markaz_tuman=markaz_tuman).order_by(
                '-created_at')

        user_markaz = self.request.user.markaz

        return models.Juvenile_Markaz.objects.all().filter(markaz=user_markaz).order_by('-created_at')

    def get_serializer_class(self):
        status = self.request.GET.get('status')
        if status and int(status) == 14:
            return serializers.UnidentifiedJuvenileForNewStatusListSerializer
        else:
            return serializers.JuvenileMarkazListSerializer




# class JuvenileReportsListView(generics.ListAPIView):
#     def get_queryset(self):
#         is_superuser = self.request.user.is_superuser
#         group_codes = self.request.user.groups.values_list('code', flat=True)
#         user_code = None
#
#         if not is_superuser:
#             user_code = list(group_codes)[0]
#
#         if user_code == 1 or is_superuser:
#             return models.Juvenile.objects.all().order_by('-created_at')
#
#         if user_code == 4:
#             markaz_tuman = self.request.user.markaz_tuman
#             return models.Juvenile.objects.all().filter(juvenile_markaz__monitoring_markaz_tuman=markaz_tuman).order_by('-created_at')
#
#         user_markaz = self.request.user.markaz
#
#         return models.Juvenile.objects.all().filter(juvenile_markaz__markaz=user_markaz).order_by('-created_at')
#



class JuvenileReportsDetailView(generics.GenericAPIView):
    serializer_class = serializers.JuvenileMarkazInfosDetailSerializer

    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None
        markaz_tuman = self.request.user.markaz_tuman

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile_Markaz.objects.all()

        if user_code == 4 or is_superuser:
            return models.Juvenile_Markaz.objects.all().filter(monitoring_markaz_tuman=markaz_tuman)

        user_markaz = self.request.user.markaz
        return models.Juvenile_Markaz.objects.all().filter(markaz=user_markaz)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            pk=int(pk)
        except:
            pass
        if isinstance(pk,int):
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            instance = get_object_or_404(models.UnidentifiedJuvenile,id = pk)
            serializer = serializers.UnidentifiedJuvenileForNewStatusDetailSerializer(instance,context={'request':request})
            return Response(serializer.data)
        # try:
        #     instance = self.get_object()
        #     serializer = self.get_serializer(instance)
        #     return Response(serializer.data)
        # except:
        #     instance =
        # instance = self.get_object()
        # serializer = self.get_serializer(instance)
        # return Response(serializer.data)


#
# class JuvenileReportsDetailView(generics.GenericAPIView):
#     serializer_class = serializers.JuvenileInfosDetailSerializer
#
#     def get_queryset(self):
#         is_superuser = self.request.user.is_superuser
#         group_codes = self.request.user.groups.values_list('code', flat=True)
#         user_code = None
#         markaz_tuman = self.request.user.markaz_tuman
#
#         if not is_superuser:
#             user_code = list(group_codes)[0]
#
#         if user_code == 1 or is_superuser:
#             return models.Juvenile.objects.all().order_by('-created_at')
#
#         if user_code == 4 or is_superuser:
#             return models.Juvenile.objects.all().filter(juvenile_markaz__monitoring_markaz_tuman=markaz_tuman).order_by('-created_at')
#
#
#         user_markaz = self.request.user.markaz
#         return models.Juvenile.objects.all().filter(juvenile_markaz__markaz=user_markaz).order_by('-created_at')
#
#     def get(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)


# JUVENILE ACCEPTED get views
class JuvenileAcceptedListView(generics.ListAPIView):
    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all().order_by('-created_at')

        user_markaz = self.request.user.markaz
        juvenile_ids = []

        juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz).filter(status=2)
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile_id)
        return models.Juvenile.objects.filter(id__in=juvenile_ids)

    serializer_class = serializers.JuvenileListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = filter.JuvenileAcceptedFilter
    pagination_class = JuvenilePagination


class JuvenileAcceptedDetailView(generics.GenericAPIView):
    serializer_class = serializers.JuvenileAcceptDetailSerializer

    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all().filter(status="3")

        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.all().filter(markaz=user_markaz).filter(status="3")

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class JuvenileAcceptedDetailForEditView(generics.GenericAPIView):
    serializer_class = serializers.JuvenileAcceptDetailSerializer

    def get_object(self, pk):
        try:
            juvenile = models.Juvenile.objects.get(pk=pk)
            accepted_info_id = juvenile.accept_center_info.id

            return models.JuvenileAcceptCenterInfo.objects.get(pk=accepted_info_id)
        except models.Juvenile.DoesNotExist:
            raise Http404

    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all()

        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.all().filter(markaz=user_markaz)

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = serializers.JuvenileAcceptCenterInfoCreateSerializer(instance, context={
            'request': request
        })
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        juvenile = self.get_object(pk)
        serializer = serializers.JuvenileAcceptCenterInfoUpdateSerializer(juvenile, data=request.data)

        inspector = json.loads(request.data.pop('prophylactic_inspector')[0])
        # inspector = request.data.pop('prophylactic_inspector')
        inspector_serializer = serializers.ProphylacticInspectorUpdateSerializer(data=inspector)
        if serializer.is_valid() and inspector_serializer.is_valid():
            pinfl = inspector_serializer.validated_data.get('pinfl', None)
            try:
                prophylactic_inspector = models.ProphylacticInspector.objects.get(pinfl=pinfl)
                inspector_serializer.update(prophylactic_inspector, inspector_serializer.data)
            except ObjectDoesNotExist:
                inspector = juvenile.inspector.id
                models.ProphylacticInspector.objects.filter(pk=inspector).delete()
                inspector_obj = models.ProphylacticInspector.objects.create(
                    **inspector_serializer.validated_data)
                juvenile.inspector = inspector_obj
            serializer.save()
            return Response(serializer.data)
        return Response({'juvenile_error': serializer.errors, 'inspector_error': inspector_serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)


# JUVENILE Expelled get views
class JuvenileExpelledListView(generics.ListAPIView):
    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all().order_by('-created_at')

        user_markaz_tuman = self.request.user.markaz_tuman
        juvenile_ids = []

        juvenile_markaz = models.Juvenile_Markaz.objects.filter(monitoring_markaz_tuman=user_markaz_tuman).filter(
            status=3)
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile_id)
        return models.Juvenile.objects.filter(id__in=juvenile_ids)

    serializer_class = serializers.JuvenileListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = filter.JuvenileExpelledFilter
    pagination_class = JuvenilePagination


class JuvenileExpelledDetailView(generics.GenericAPIView):
    serializer_class = serializers.JuvenileExpelledDetailSerializer

    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all().filter(status="4").order_by('-created_at')

        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.all().filter(markaz=user_markaz).filter(status="4").order_by('-created_at')

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class JuvenileExpelledDetailForEditView(generics.GenericAPIView):
    serializer_class = serializers.JuvenileExpelledDetailSerializer

    def get_object(self, pk):
        try:
            juvenile = models.Juvenile.objects.get(pk=pk)
            distributed_info_id = juvenile.distributed_info.id
            return models.JuvenileDistributedInfo.objects.get(pk=distributed_info_id)
        except models.Juvenile.DoesNotExist:
            raise Http404

    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all()

        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.all().filter(markaz=user_markaz)

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = serializers.JuvenileDistributedInfoDetailSerializer(instance, context={
            'request': request
        })
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        juvenile = self.get_object(pk)
        serializer = serializers.JuvenileDistributedInfoUpdateSerializer(juvenile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Juvenile monitoring get views
class JuvenileMonitoringDetailView(generics.GenericAPIView):
    serializer_class = serializers.JuvenileMonitoringDetailSerializer

    def get_object(self, pk):
        try:
            juvenile = models.Juvenile.objects.get(pk=pk)
            monitoring_info_id = juvenile.monitoring_info.id
            return models.JuvenileMonitoringInfo.objects.get(pk=monitoring_info_id)
        except models.Juvenile.DoesNotExist:
            raise Http404

    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all().filter(status="5").order_by('-created_at')

        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.all().filter(markaz=user_markaz).filter(status="5").order_by('-created_at')

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class JuvenileMonitoringDetailForEditView(generics.GenericAPIView):
    serializer_class = serializers.JuvenileMonitoringDetailSerializer

    def get_object(self, pk):
        try:
            juvenile = models.Juvenile.objects.get(pk=pk)
            monitoring_info_id = juvenile.monitoring_info.id
            return models.JuvenileMonitoringInfo.objects.get(pk=monitoring_info_id)
        except models.Juvenile.DoesNotExist:
            raise Http404

    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all()

        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.all().filter(markaz=user_markaz)

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = serializers.MonitoringInfoDetailSerializer(instance, context={
            'request': request
        })
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        juvenile = self.get_object(pk)
        serializer = serializers.JuvenileMonitoringInfoUpdateSerializer(juvenile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Juvenile Employment get views
class JuvenileEmploymentDetailView(generics.GenericAPIView):
    serializer_class = serializers.JuvenileEmploymentDetailSerializer

    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all().filter(status="6").order_by('-created_at')

        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.all().filter(markaz=user_markaz).filter(status="6").order_by('-created_at')

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class JuvenileEmploymentDetailForEditView(generics.GenericAPIView):
    serializer_class = serializers.JuvenileEmploymentDetailSerializer

    def get_object(self, pk):
        try:
            juvenile = models.Juvenile.objects.get(pk=pk)
            employment_info_id = juvenile.employment_info.id
            return models.JuvenileEmploymentInfo.objects.get(pk=employment_info_id)
        except models.Juvenile.DoesNotExist:
            raise Http404

    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all()

        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.all().filter(markaz=user_markaz)

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = serializers.EmploymentInfoDetailSerializer(instance, context={
            'request': request
        })
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        juvenile = self.get_object(pk)
        serializer = serializers.JuvenileEmploymentInfoUpdateSerializer(juvenile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JuvenileStepFilledView(generics.GenericAPIView):
    serializer_class = serializers.JuvenileStepFilledSerializer

    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all()

        user_markaz = self.request.user.markaz
        return models.Juvenile.objects.all().filter(markaz=user_markaz)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


# Juvenile employment info list view
class JuvenileEmploymentListView(generics.ListAPIView):
    def get_queryset(self):
        is_superuser = self.request.user.is_superuser
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = None

        if not is_superuser:
            user_code = list(group_codes)[0]

        if user_code == 1 or is_superuser:
            return models.Juvenile.objects.all().order_by('-created_at')

        user_markaz = self.request.user.markaz
        juvenile_ids = []

        juvenile_markaz = models.Juvenile_Markaz.objects.filter(markaz=user_markaz).filter(status=5)
        for item in juvenile_markaz:
            juvenile_ids.append(item.juvenile_id)
        return models.Juvenile.objects.filter(id__in=juvenile_ids)

    serializer_class = serializers.JuvenileListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = filter.JuvenileExpelledFilter
    pagination_class = JuvenilePagination


class AddCurrentMarkaz(APIView):
    queryset = models.Juvenile.objects.all()

    def post(self, request, format=None):
        user_markaz = request.user.markaz
        juveniles = models.Juvenile.objects.filter(juvenile_markaz__markaz=user_markaz)
        for juvenile in juveniles:
            juvenile.current_markaz = user_markaz
            juvenile.save()
        return Response({'message': 'Added current_markaz'})


# class LastAcceptedJuvenilesView(generics.ListAPIView):
#     serializer_class = serializers.JuvenileMarkazSerializer
#     # permission_classes = [AllowAny]  # Allow any permission for testing
#
#     def get_queryset(self):
#         now = timezone.now()
#         start_datetime = timezone.datetime(now.year, now.month, now.day - 2 , 19, 0, 0)
#         # start_datetime = timezone.datetime(now.year, now.month, now.day - 10 , 19, 0, 0)
#         end_datetime = timezone.datetime(now.year, now.month, now.day - 1, 19, 0, 0)
#         # end_datetime = timezone.datetime(now.year, now.month, now.day, 19, 0, 0)
#         juvenile_markazs = models.Juvenile_Markaz.objects.filter(
#             Q(status__in=['2','3','4','5','6','7','8','9','10', '11','12','13'])
#             & Q(accept_center_info__created_at__range=[start_datetime, end_datetime])
#         ).order_by('-created_at')
#         return juvenile_markazs



class JuvenileNoEducationListView(generics.ListAPIView):
    permission_classes = [AllowAny]  # Allow any permission for testing

    serializer_class = serializers.JuvenileNoEducationListSerializer

    def get_queryset(self):
        juveniles_no_education = models.PersonalInfoJuvenile.objects.filter(juvenile__educationinfojuvenile__isnull=True,juvenile__isnull=False).distinct()
        return juveniles_no_education


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Create a response object with CSV content
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="juvenile_no_education.csv"'

        # Create a CSV writer
        csv_writer = csv.writer(response)

        # Write header
        header = serializers.JuvenileNoEducationListSerializer().fields.keys()
        csv_writer.writerow(header)

        # Write data
        for juvenile in queryset:
            serializer = serializers.JuvenileNoEducationListSerializer(juvenile,context={'request': request})
            row = [serializer.data[field] for field in header]
            csv_writer.writerow(row)

        return response


# class test(generics.GenericAPIView):
#     permission_classes = [AllowAny]  # Allow any permission for testing
#
#     def post(self,request):
#         return HttpResponse('ba')

# class UnidentifiedReportsDetailView(generics.RetrieveAPIView):
#     serializer_class = serializers.UnidentifiedJuvenileForNewStatusDetailSerializer
#     queryset = models.UnidentifiedJuvenile.objects.all()

class PsychologyConditionListView(generics.ListAPIView):
    queryset = models.PsychologyCondition.objects.all()
    serializer_class = serializers.PsychologyConditionSerializer

class JuvenileDeleteView(generics.DestroyAPIView):
    queryset = models.Juvenile.objects.all()
    def get_object(self,pk):

        if isinstance(pk, int):
            instance = get_object_or_404(models.Juvenile_Markaz,pk=pk)

        else:
            instance = get_object_or_404(models.UnidentifiedJuvenile, id=pk)
        return instance

    def delete(self, request, *args, **kwargs):
        request_code = request.user.groups.all()[0].code
        if request_code != 1:
            return Response({"message": "joriy foydalanuvchi apparat emas!"}, status=status.HTTP_401_UNAUTHORIZED)
        pk = kwargs.get('pk')
        try:
            pk = int(pk)
        except:
            pass
        instance = self.get_object(pk)
        instance.delete()
        print('test')
        return Response("Muvaffaqiyatli o'chirildi",status=status.HTTP_204_NO_CONTENT)

# class MarkazListView(generics.ListAPIView):
#     queryset = Markaz.objects.all()
#     serializer_class = MarkazListSerializer

