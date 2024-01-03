from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import APIView

from django.db import connection



from datetime import datetime
from juvenile import models
from juvenile.statistics import serializers
import pytz

from rest_framework.views import APIView
from config.settings import env

from django.http import HttpResponse

from . import reports
from rest_framework import permissions
import xlsxwriter

class DashboarCardStatisticsAPIView(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.DashboardCardStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)

        
class ReasonBringingStatisticsAPIView(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.ReasonBringingStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)


class DistributionTypeStatisticsAPIView(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.DistributionTypeStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)

        
class EducationTypeStatisticsAPIView(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.EducationTypeStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)


class ComeMore2TimesStatisticsAPIView(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.ComeMore2TimesStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)


class InCenterNowStatisticsAPIView(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.InCenterNowStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)


class DownloadStatisticsAPIView(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()

        dashboard_card_statistics_serializer = serializers.DashboardCardStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        reason_bringing_statistics_serializer = serializers.ReasonBringingStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        in_center_now_statistics_serializer = serializers.InCenterNowStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        come_more_2_times_statistics_serializer = serializers.ComeMore2TimesStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        education_type_statistics_serializer = serializers.EducationTypeStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        
        local_time = datetime.now(pytz.timezone('Asia/Tashkent'))
        download_time = format(local_time, '%Y-%m-%d-%H-%M-%S')

        workbook = xlsxwriter.Workbook(f"media/{download_time}.xlsx")
        worksheet = workbook.add_worksheet("statistics")

        domain_name = env('DOMAIN_NAME')
        file_path = f'{domain_name}/{workbook.filename}'

        #Umumiy ma'lumotlar
        data1 = dashboard_card_statistics_serializer.data

        worksheet.write(0, 0, "Umumiy Ma'lumotlar")

        worksheet.write(1, 1, "Markazga qabul qilingan bola")
        worksheet.write(1, 2, "O‘g‘il bola")
        worksheet.write(1, 3, "Qiz bola")
        worksheet.write(1, 4, "ITMni tamomlagan")
        worksheet.write(1, 5, "Bandligi tal’minlangan")
        worksheet.write(1, 6, "Shaxsi aniqlanmagan")

        worksheet.write(2, 1, data1["accepted_center_childs"])
        worksheet.write(2, 2, data1["boys"])
        worksheet.write(2, 3, data1["girls"])
        worksheet.write(2, 4, data1["graduated_itm"])
        worksheet.write(2, 5, data1["employment_guaranteed"])
        worksheet.write(2, 6, data1["not_identified"])

        #Olib Kelish sababi
        data2 = reason_bringing_statistics_serializer.data

        worksheet.write(3, 0, "Olib kelish sababi")

        worksheet.write(4, 0, "Nazoratsiz qolgan")
        worksheet.write(4, 1, "Qarovsiz qolgan")
        worksheet.write(4, 2, "Davlat va jamoatchilik yordamiga muhtoj")
        worksheet.write(4, 3, "Ijtimoiy jixatda xavfli axvolda yashayotgan")
        worksheet.write(4, 4, "Bedarak yo‘qolgan va qidiruvda bo‘lgan")
        worksheet.write(4, 5, "Tarbiyasi og‘ir")

        worksheet.write(5, 0, data2["unsupervised_child"])
        worksheet.write(5, 1, data2["neglected_child"])
        worksheet.write(5, 2, data2["needs_state_public_support"])
        worksheet.write(5, 3, data2["dangerous_social_situation"])
        worksheet.write(5, 4, data2["missing_and_wanted"])
        worksheet.write(5, 5, data2["difficult_upbringing"])

        #Kimlarga topshirildi
        data3 = 0

        worksheet.write(6, 0, "Kimlarga topshirildi")

        worksheet.write(7, 0, "ota-ona yoki o‘rnini bosuvchi shaxsga")
        worksheet.write(7, 1, "RO‘TM")
        worksheet.write(7, 2, "ITM")
        worksheet.write(7, 3, "Mehribonlik uylari")
        worksheet.write(7, 4, "Oilaviy bolalar uyi")
        worksheet.write(7, 5, "“SOS” bolalar mahallasi")
        worksheet.write(7, 6, "Vasiylik va homiylik")
        worksheet.write(7, 7, "Sog‘liqni saqlash")

        worksheet.write(8, 0, data3)
        worksheet.write(8, 1, data3)
        worksheet.write(8, 2, data3)
        worksheet.write(8, 3, data3)
        worksheet.write(8, 4, data3)
        worksheet.write(8, 5, data3)
        worksheet.write(8, 6, data3)
        worksheet.write(8, 7, data3)

        #Hozir markazda
        data4 = in_center_now_statistics_serializer.data

        worksheet.write(9, 0, "Hozir markazda")

        worksheet.write(10, 0, "Barchasi")
        worksheet.write(10, 1, "Qiz bolalar")
        worksheet.write(10, 2, "O‘g‘il bolalar")

        worksheet.write(11, 0, data4['all_juveniles'])
        worksheet.write(11, 1, data4['boys'])
        worksheet.write(11, 2, data4['girls'])

        #2 va undan ortiq kelgan bolalar
        data5 = come_more_2_times_statistics_serializer.data

        worksheet.write(12, 0, "2 va undan ortiq kelgan bolalar")

        worksheet.write(13, 0, "Barchasi")
        worksheet.write(13, 1, "Qiz bolalar")
        worksheet.write(13, 2, "O‘g‘il bolalar")

        worksheet.write(14, 0, data5['all_juveniles'])
        worksheet.write(14, 1, data5['boys'])
        worksheet.write(15, 2, data5['girls'])

        # Markazga qabul qilingan bolalarning o‘qish muasassasi
        data6 = education_type_statistics_serializer.data

        worksheet.write(
            16, 0, "Markazga qabul qilingan bolalarning o'qish muasassasi")

        worksheet.write(17, 0, "Maktabgacha ta'lim")
        worksheet.write(17, 1, "Maktab")
        worksheet.write(17, 2, "Kasb-hunar maktabi")
        worksheet.write(17, 3, "Kasb-hunar kolleil")
        worksheet.write(17, 4, "Litsev")
        worksheet.write(17, 5, "Texnikum")
        worksheet.write(17, 6, "Maxsus ta'lim")
        worksheet.write(17, 7, "OTM")
        worksheet.write(17, 8, "Ishlaydi")
        worksheet.write(17, 9, "O'qimaydi / Ishlamaydi")

        worksheet.write(18, 0, data6['kindergarten'])
        worksheet.write(18, 1, data6['school'])
        worksheet.write(18, 2, data6['vocational_school'])
        worksheet.write(18, 3, data6['vocational_college'])
        worksheet.write(18, 4, data6['litsey'])
        worksheet.write(18, 5, data6['texnikum'])
        worksheet.write(18, 6, data6['special_education'])
        worksheet.write(18, 7, data6['otm'])
        worksheet.write(18, 8, data6['working'])
        worksheet.write(18, 9, data6['not_study_not_working'])

        workbook.close()
        return Response({'file': file_path})


class ApparatDashboarCardStatisticsAPIView(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.ApparatDashboardCardStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)


class ApparatReasonBringingStatisticsAPIView(APIView):
    permission_classes = []

    def get(self,request):
        with connection.cursor() as cursor:
            query = """SELECT
                COALESCE(SUM(CASE WHEN arbc.parent_id = 1 THEN 1 ELSE 0 END), 0) AS unsupervised_child,
                COALESCE(SUM(CASE WHEN arbc.parent_id = 2 THEN 1 ELSE 0 END), 0) AS neglected_child,
                COALESCE(SUM(CASE WHEN arbc.parent_id = 3 THEN 1 ELSE 0 END), 0) AS needs_state_public_support,
                COALESCE(SUM(CASE WHEN arbc.parent_id = 4 THEN 1 ELSE 0 END), 0) AS dangerous_social_situation,
                COALESCE(SUM(CASE WHEN arbc.parent_id = 6 THEN 1 ELSE 0 END), 0) AS missing_and_wanted,
                COALESCE(SUM(CASE WHEN arbc.parent_id = 5 THEN 1 ELSE 0 END), 0) AS difficult_upbringing
            FROM
                juvenile_markaz jm
            LEFT JOIN
                juvenile_accept_center_info jaci ON jm.accept_center_info_id = jaci.id
            LEFT JOIN
                sub_reason_bringning_child arbc ON jaci.sub_reason_bringing_child_id = arbc.id;
                    """
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            if results:
                return Response(results[0],status=200)




class ApparatReasonBringingStatisticsAPIView2(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.ApparatReasonBringingStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)


class ApparatInCenterNowStatisticsAPIView(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.ApparatInCenterNowStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)


class ApparatDistributionTypeStatisticsAPIView(APIView):
    permission_classes = []

    def get(self, request):
        with connection.cursor() as cursor:
            query = """SELECT
    COALESCE(SUM(CASE WHEN jdi.distribution_type IN ('1','8') THEN 1 ELSE 0 END), 0) AS to_parents,
    COALESCE(SUM(CASE WHEN jdi.distribution_type = '4' THEN 1 ELSE 0 END), 0) AS to_rotm,
    COALESCE(SUM(CASE WHEN jdi.type_guardianship = '5' THEN 1 ELSE 0 END), 0) AS to_orphanages,
    COALESCE(SUM(CASE WHEN jdi.type_guardianship = '6' THEN 1 ELSE 0 END), 0) AS get_to_family_orphanages,
    COALESCE(SUM(CASE WHEN jdi.type_guardianship = '7' THEN 1 ELSE 0 END), 0) AS to_sos,
    COALESCE(SUM(CASE WHEN jdi.type_guardianship IN ('1','2') THEN 1 ELSE 0 END), 0) AS to_other_center,
    COALESCE(SUM(CASE WHEN jdi.distribution_type = '5' THEN 1 ELSE 0 END), 0) AS to_healthcare,
    COALESCE(SUM(CASE WHEN jdi.distribution_type = '6' THEN 1 ELSE 0 END), 0) AS to_other_center,
    COALESCE(SUM(CASE WHEN jdi.distribution_type = '7' THEN 1 ELSE 0 END), 0) AS to_other_country
FROM
    juvenile_distributed_info as jdi;

                       """

            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            if results:
                return Response(results[0], status=200)


class ApparatDistributionTypeStatisticsAPIView2(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.ApparatDistributionTypeStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)


class ApparatComeMore2TimesStatisticsAPIView(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.ApparatComeMore2TimesStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)


class ApparatEducationTypeStatisticsAPIView(APIView):
    permission_classes = []
    # authentication_classes = []

    def get(self,request):
        with connection.cursor() as cursor:
            query = """SELECT 
                        SUM(CASE WHEN ej.kindergarten_id IS NOT NULL THEN 1 ELSE 0 END) AS kindergarten,
                        SUM(CASE WHEN ej.school_id IS NOT NULL THEN 1 ELSE 0 END) AS school,
                        SUM(CASE WHEN ej.vocational_school_id IS NOT NULL THEN 1 ELSE 0 END) AS vocational_school,
                        SUM(CASE WHEN ej.college_id IS NOT NULL THEN 1 ELSE 0 END) AS vocational_college,
                        SUM(CASE WHEN ej.litsey_id IS NOT NULL THEN 1 ELSE 0 END) AS litsey,
                        SUM(CASE WHEN ej.texnikum_id IS NOT NULL THEN 1 ELSE 0 END) AS texnikum,
                        SUM(CASE WHEN ej.special_education_id IS NOT NULL THEN 1 ELSE 0 END) AS special_education,
                        SUM(CASE WHEN ej.university_id IS NOT NULL THEN 1 ELSE 0 END) AS otm,
                        SUM(CASE WHEN ej.school_type = 'O‘qimaydi/Ishlamaydi' THEN 1 ELSE 0 END) AS not_study_not_working 
                    FROM education_info_juvenile ej;
                    """

            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            if results:
                return Response(results[0],status=200)






class ApparatEducationTypeStatisticsAPIView2(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = serializers.ApparatEducationTypeStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        return Response(serializer.data)


class ApparatDownloadStatisticsAPIView(generics.ListAPIView):
    queryset = models.Juvenile.objects.all()

    def list(self, request):
        queryset = self.get_queryset()

        dashboard_card_statistics_serializer = serializers.ApparatDashboardCardStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        reason_bringing_statistics_serializer = serializers.ApparatReasonBringingStatisticsSerializer2(queryset, many=False, context={
            'request': request
        })
        in_center_now_statistics_serializer = serializers.ApparatInCenterNowStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        come_more_2_times_statistics_serializer = serializers.ApparatComeMore2TimesStatisticsSerializer(queryset, many=False, context={
            'request': request
        })
        education_type_statistics_serializer = serializers.ApparatEducationTypeStatisticsSerializer(queryset, many=False, context={
            'request': request
        })

        local_time = datetime.now(pytz.timezone('Asia/Tashkent'))
        download_time = format(local_time, '%Y-%m-%d-%H-%M-%S')

        workbook = xlsxwriter.Workbook(f"media/{download_time}.xlsx")
        worksheet = workbook.add_worksheet("statistics")

        domain_name = env('DOMAIN_NAME')

        print(domain_name)
        file_path = f'{domain_name}/{workbook.filename}'
        print(file_path)
        
        #Umumiy ma'lumotlar
        data1 = dashboard_card_statistics_serializer.data

        worksheet.write(0, 0, "Umumiy Ma'lumotlar")

        worksheet.write(1, 1, "Markazga qabul qilingan bola")
        worksheet.write(1, 2, "O‘g‘il bola")
        worksheet.write(1, 3, "Qiz bola")
        worksheet.write(1, 4, "ITMni tamomlagan")
        worksheet.write(1, 5, "Bandligi tal’minlangan")
        worksheet.write(1, 6, "Shaxsi aniqlanmagan")

        worksheet.write(2, 1, data1["accepted_center_childs"])
        worksheet.write(2, 2, data1["boys"])
        worksheet.write(2, 3, data1["girls"])
        worksheet.write(2, 4, data1["graduated_itm"])
        worksheet.write(2, 5, data1["employment_guaranteed"])
        worksheet.write(2, 6, data1["not_identified"])

        #Olib Kelish sababi
        data2 = reason_bringing_statistics_serializer.data
        # return Response(data2)
        worksheet.write(3, 0, "Olib kelish sababi")

        worksheet.write(4, 0, "Nazoratsiz qolgan")
        worksheet.write(4, 1, "Qarovsiz qolgan")
        worksheet.write(4, 2, "Davlat va jamoatchilik yordamiga muhtoj")
        worksheet.write(4, 3, "Ijtimoiy jixatda xavfli axvolda yashayotgan")
        worksheet.write(4, 4, "Bedarak yo‘qolgan va qidiruvda bo‘lgan")
        worksheet.write(4, 5, "Tarbiyasi og‘ir")

        worksheet.write(5, 0, data2["unsupervised_child"])
        worksheet.write(5, 1, data2["neglected_child"])
        worksheet.write(5, 2, data2["needs_state_public_support"])
        worksheet.write(5, 3, data2["dangerous_social_situation"])
        worksheet.write(5, 4, data2["missing_and_wanted"])
        worksheet.write(5, 5, data2["difficult_upbringing"])

        #Kimlarga topshirildi
        data3 = 0

        worksheet.write(6, 0, "Kimlarga topshirildi")

        worksheet.write(7, 0, "ota-ona yoki o‘rnini bosuvchi shaxsga")
        worksheet.write(7, 1, "RO‘TM")
        worksheet.write(7, 2, "ITM")
        worksheet.write(7, 3, "Mehribonlik uylari")
        worksheet.write(7, 4, "Oilaviy bolalar uyi")
        worksheet.write(7, 5, "“SOS” bolalar mahallasi")
        worksheet.write(7, 6, "Vasiylik va homiylik")
        worksheet.write(7, 7, "Sog‘liqni saqlash")

        worksheet.write(8, 0, data3)
        worksheet.write(8, 1, data3)
        worksheet.write(8, 2, data3)
        worksheet.write(8, 3, data3)
        worksheet.write(8, 4, data3)
        worksheet.write(8, 5, data3)
        worksheet.write(8, 6, data3)
        worksheet.write(8, 7, data3)

        #Hozir markazda
        data4 = in_center_now_statistics_serializer.data

        worksheet.write(9, 0, "Hozir markazda")

        worksheet.write(10, 0, "Barchasi")
        worksheet.write(10, 1, "Qiz bolalar")
        worksheet.write(10, 2, "O‘g‘il bolalar")

        worksheet.write(11, 0, data4['all_juveniles'])
        worksheet.write(11, 1, data4['boys'])
        worksheet.write(11, 2, data4['girls'])

        #2 va undan ortiq kelgan bolalar
        data5 = come_more_2_times_statistics_serializer.data

        worksheet.write(12, 0, "2 va undan ortiq kelgan bolalar")

        worksheet.write(13, 0, "Barchasi")
        worksheet.write(13, 1, "Qiz bolalar")
        worksheet.write(13, 2, "O‘g‘il bolalar")

        worksheet.write(14, 0, data5['all_juveniles'])
        worksheet.write(14, 1, data5['boys'])
        worksheet.write(15, 2, data5['girls'])

        # Markazga qabul qilingan bolalarning o‘qish muasassasi
        data6 = education_type_statistics_serializer.data

        worksheet.write(
            16, 0, "Markazga qabul qilingan bolalarning o'qish muasassasi")

        worksheet.write(17, 0, "Maktabgacha ta'lim")
        worksheet.write(17, 1, "Maktab")
        worksheet.write(17, 2, "Kasb-hunar maktabi")
        worksheet.write(17, 3, "Kasb-hunar kolleil")
        worksheet.write(17, 4, "Litsev")
        worksheet.write(17, 5, "Texnikum")
        worksheet.write(17, 6, "Maxsus ta'lim")
        worksheet.write(17, 7, "OTM")
        worksheet.write(17, 8, "Ishlaydi")
        worksheet.write(17, 9, "O'qimaydi / Ishlamaydi")

        worksheet.write(18, 0, data6['kindergarten'])
        worksheet.write(18, 1, data6['school'])
        worksheet.write(18, 2, data6['vocational_school'])
        worksheet.write(18, 3, data6['vocational_college'])
        worksheet.write(18, 4, data6['litsey'])
        worksheet.write(18, 5, data6['texnikum'])
        worksheet.write(18, 6, data6['special_education'])
        worksheet.write(18, 7, data6['otm'])
        worksheet.write(18, 8, data6['working'])
        worksheet.write(18, 9, data6['not_study_not_working'])

        workbook.close()
        return Response({'file': file_path})

# class TotalStatisticListAPIView(generics.ListAPIView):
#     queryset = models.Juvenile.objects.all()

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = serializers.TotalStatisticSerializer(queryset, many=False, context={
#             'request': request
#         })
#         return Response(serializer.data)


# class ArrivalAndSubmitedStatisticListAPIView(generics.ListAPIView):
#     queryset = models.Juvenile.objects.all()

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = serializers.ArrivalAndSubmitedSerializer(queryset, many=False, context={
#             'request': request
#         })
#         return Response(serializer.data)


# class ITMAndAcceptedStatisticListAPIView(generics.ListAPIView):
#     queryset = models.Juvenile.objects.all()

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = serializers.ITMAndAcceptedSerializer(queryset, many=False, context={
#             'request': request
#         })
#         return Response(serializer.data)


###### new code ######


class ApparatDownloadStatisticsAPIView10(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        file_path = reports.apparat_to_excel_10()
        return Response({'file':file_path})

class CenterDownloadStatisticsApiView1(generics.GenericAPIView):
    def get_queryset(self):
        return models.Juvenile.objects.all()
    def get(self,request):
        file_path1 = reports.center_to_excel_9(request)
        # file_path2 = reports.center_to_excel_8_1(request)
        # file_path3 = reports.center_to_excel_8_1(request)
        # file_path4 = reports.center_to_excel_8_1(request)
        return Response({
            'file':file_path1,
            # 'file2': file_path2,
            # 'file3': file_path3,
            # 'file4': file_path4,
        #
        })
class CenterDownloadStatisticsApiView2(generics.GenericAPIView):
    def get_queryset(self):
        return models.Juvenile.objects.all()
    def get(self,request):
        file_path2 = reports.center_to_excel_8_1(request)
        # file_path2 = reports.center_to_excel_8_1(request)
        # file_path3 = reports.center_to_excel_8_1(request)
        # file_path4 = reports.center_to_excel_8_1(request)
        return Response({
            'file':file_path2,
            # 'file2': file_path2,
            # 'file3': file_path3,
            # 'file4': file_path4,

        })
class CenterDownloadStatisticsApiView3(generics.GenericAPIView):
    def get_queryset(self):
        return models.Juvenile.objects.all()

    def get(self,request):
        # file_path1 = reports.center_to_excel_9(request)
        file_path3 = reports.center_to_excel_8_2(request)
        # file_path3 = reports.center_to_excel_8_1(request)
        # file_path4 = reports.center_to_excel_8_1(request)
        return Response({
            # 'file':file_path1,
            'file': file_path3,
            # 'file3': file_path3,
            # 'file4': file_path4,

        })
class CenterDownloadStatisticsApiView4(generics.GenericAPIView):
    def get_queryset(self):
        return models.Juvenile.objects.all()

    def get(self,request):
        file_path3 = reports.center_to_excel_8_3(request)
        # file_path4 = reports.center_to_excel_8_3(request)
        return Response({
            # 'file':file_path1,
            # 'file2': file_path2,
            'file': file_path3,
            # 'file4': file_path4,

        })


class ApparatDownloadStatisticsApiView1(generics.GenericAPIView):
    # permission_classes =  [permissions.AllowAny]
    def get_queryset(self):
        return models.Juvenile.objects.all()
    def get(self,request):
        print('CDF',request.user)
        file_path1 = reports.apparat_to_excel_10(request)
        # file_path2 = reports.apparat_to_excel_7_1(request)
        # file_path3 = reports.apparat_to_excel_7_2(request)
        # file_path4 = reports.apparat_to_excel_7_3(request)
        return Response({
            'file':file_path1,
            # 'file2': file_path2,
            # 'file3': file_path3,
            # 'file4': file_path4,

        })

class ApparatDownloadStatisticsApiView2(generics.GenericAPIView):
    # permission_classes =  [permissions.AllowAny]
    def get_queryset(self):
        return models.Juvenile.objects.all()
    def get(self,request):
        print('CDF',request.user)
        # file_path1 = reports.apparat_to_excel_10(request)
        file_path2 = reports.apparat_to_excel_7_1(request)
        # file_path3 = reports.apparat_to_excel_7_2(request)
        # file_path4 = reports.apparat_to_excel_7_3(request)
        return Response({
            'file':file_path2,
            # 'file2': file_path2,
            # 'file3': file_path3,
            # 'file4': file_path4,

        })
class ApparatDownloadStatisticsApiView3(generics.GenericAPIView):
    # permission_classes =  [permissions.AllowAny]
    def get_queryset(self):
        return models.Juvenile.objects.all()
    def get(self,request):
        print('CDF',request.user)
        # file_path1 = reports.apparat_to_excel_10(request)
        # file_path2 = reports.apparat_to_excel_7_1(request)
        file_path3 = reports.apparat_to_excel_7_2(request)
        # file_path4 = reports.apparat_to_excel_7_3(request)
        return Response({
            'file':file_path3,
            # 'file2': file_path2,
            # 'file3': file_path3,
            # 'file4': file_path4,

        })
class ApparatDownloadStatisticsApiView4(generics.GenericAPIView):
    # permission_classes =  [permissions.AllowAny]
    def get_queryset(self):
        return models.Juvenile.objects.all()
    def get(self,request):
        print('CDF',request.user)
        # file_path1 = reports.apparat_to_excel_10(request)
        # file_path2 = reports.apparat_to_excel_7_1(request)
        # file_path3 = reports.apparat_to_excel_7_2(request)
        file_path4 = reports.apparat_to_excel_7_3(request)
        return Response({
            'file':file_path4,
            # 'file2': file_path2,
            # 'file3': file_path3,
            # 'file4': file_path4,

        })