from .words import headers,subheaders,headers_2,subheaders_2
import io
import xlsxwriter
from .. import models
from info.models import Region,Markaz
from django.db.models import Q,F,Count,Sum
from datetime import timedelta,date,datetime
import pytz
from notification.models import Notification
from config.settings import env

from info.enums import DETERMINED_LOCATION_CHOICE
regions = Region.objects.all()
base_query_2024 = models.Juvenile_Markaz.objects.filter(status__in=['2','3','4','5','6','7','8','9','10','11','12','13'],accept_center_info__arrived_date__year=2024)

base_query_2023 = models.Juvenile_Markaz.objects.filter(status__in=['2','3','4','5','6','7','8','9','10','11','12','13'],accept_center_info__arrived_date__year=2023)
# base_query_2024 = models.Juvenile_Markaz.objects.select_related('juvenile','markaz','accept_center_info').exclude(status='1').filter(accept_center_info__arrived_date__year = 2024)
# base_query_2023 = models.Juvenile_Markaz.objects.select_related('juvenile','markaz','accept_center_info').exclude(status='1').filter(accept_center_info__arrived_date__year = 2023)

respublika_base_query_2024 = models.Juvenile_Markaz.objects.filter(status__in=['2','3','4','5','6','7','8','9','10','11','12','13'],accept_center_info__arrived_date__year=2024)
respublika_base_query_2023 = models.Juvenile_Markaz.objects.filter(status__in=['2','3','4','5','6','7','8','9','10','11','12','13'],accept_center_info__arrived_date__year=2023)

query_taqsimlangan = models.Juvenile_Markaz.objects.filter(status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13'])


def apparat_to_excel_10(requset):
    local_time = datetime.now(pytz.timezone('Asia/Tashkent'))
    download_time = format(local_time, '%Y-%m-%d-%H-%M-%S')

    workbook = xlsxwriter.Workbook(f"media/apparat_statistics_10__{download_time}.xlsx")
    worksheet = workbook.add_worksheet("Statistics")
    # domain_name = 'http://127.0.0.1:8000/'
    domain_name = env('DOMAIN_NAME')

    file_path = f'{domain_name}/{workbook.filename}'

    header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size':14
        # 'fg_color': '#F0F4FF'
    })
    header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size':14
        # 'fg_color': '#F0F4FF'
    })

    header_merge_format.set_border_color("#1d588b")
    header_merge_format_bold.set_border_color("#1d588b")
    # wrap_format_horizontal = workbook.add_format({'text_wrap': True,
    #                                    'bold': 1,
    #                                    'border': 1,
    #                                    'align': 'center',
    #                                    'valign': 'vcenter',
    #                                    })

    vertical_header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size':14
        # 'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size':14
        # 'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format.set_rotation(90)
    vertical_header_merge_format.set_border_color("#1d588b")
    vertical_header_merge_format_bold.set_rotation(90)
    vertical_header_merge_format_bold.set_border_color("#1d588b")

    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    merge_format.set_border_color("#1d588b")

    file_name_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
    })

    bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'
    })
    bold.set_rotation(90)
    bold.set_border_color("#1d588b")

    worksheet.set_column(0, 1, 8)
    worksheet.set_column(1,2,20)
    worksheet.set_column(2,3,12)
    worksheet.set_column(5, 32, 8)
    worksheet.set_column(33, 33, 12)
    worksheet.set_column(34, 69, 8)
    # worksheet.set_column(10, 16, 40)



    worksheet.merge_range(3, 0, 4, 0, headers[0], header_merge_format_bold)
    worksheet.merge_range(3, 1, 4, 1, headers[1], header_merge_format_bold)
    worksheet.merge_range(3, 2, 4, 2, headers[2], header_merge_format_bold)
    worksheet.merge_range(3, 3, 4, 3, headers[3], header_merge_format_bold)

    worksheet.write(3, 4,  headers[4], header_merge_format_bold)
    worksheet.write(4, 4, headers[5], vertical_header_merge_format)

    worksheet.merge_range(3, 5, 3, 9, headers[6], header_merge_format_bold)
    worksheet.write(4, 5, subheaders[headers[6]][0], vertical_header_merge_format)
    worksheet.write(4, 6, subheaders[headers[6]][1], vertical_header_merge_format)
    worksheet.write(4, 7, subheaders[headers[6]][2], vertical_header_merge_format)
    worksheet.write(4, 8, subheaders[headers[6]][3], vertical_header_merge_format)
    worksheet.write(4, 9, subheaders[headers[6]][4], vertical_header_merge_format)

    worksheet.merge_range(3, 10, 3, 14, headers[7], header_merge_format_bold)
    worksheet.write(4, 10, subheaders[headers[7]][0], vertical_header_merge_format)
    worksheet.write(4, 11,  subheaders[headers[7]][1], vertical_header_merge_format)
    worksheet.write(4, 12, subheaders[headers[7]][2], vertical_header_merge_format)
    worksheet.write(4, 13, subheaders[headers[7]][3], vertical_header_merge_format)
    worksheet.write(4, 14,  subheaders[headers[7]][4], vertical_header_merge_format)

    worksheet.merge_range(3, 15, 3, 18, headers[8], header_merge_format_bold)
    worksheet.write(4, 15, subheaders[headers[8]][0], vertical_header_merge_format)
    worksheet.write(4, 16,  subheaders[headers[8]][1], vertical_header_merge_format)
    worksheet.write(4, 17,  subheaders[headers[8]][2], vertical_header_merge_format)
    worksheet.write(4, 18,  subheaders[headers[8]][3], vertical_header_merge_format)

    worksheet.merge_range(3, 19, 3, 28, headers[9], header_merge_format_bold)
    worksheet.write(4, 19,  subheaders[headers[9]][0], vertical_header_merge_format)
    worksheet.write(4, 20,  subheaders[headers[9]][1], vertical_header_merge_format)
    worksheet.write(4, 21, subheaders[headers[9]][2], vertical_header_merge_format)
    worksheet.write(4, 22,  subheaders[headers[9]][3], vertical_header_merge_format)
    worksheet.write(4, 23,  subheaders[headers[9]][4], vertical_header_merge_format)
    worksheet.write(4, 24,  subheaders[headers[9]][5], vertical_header_merge_format)
    worksheet.write(4, 25,  subheaders[headers[9]][6], vertical_header_merge_format)
    worksheet.write(4, 26,  subheaders[headers[9]][7], vertical_header_merge_format)
    worksheet.write(4, 27,  subheaders[headers[9]][8], vertical_header_merge_format)
    worksheet.write(4, 28,  subheaders[headers[9]][9], vertical_header_merge_format)

    worksheet.merge_range(3, 29, 3, 32, headers[10], header_merge_format_bold)
    worksheet.write(4, 29,  subheaders[headers[10]][0], vertical_header_merge_format)
    worksheet.write(4, 30,  subheaders[headers[10]][1], vertical_header_merge_format)
    worksheet.write(4, 31, subheaders[headers[10]][2], vertical_header_merge_format)
    worksheet.write(4, 32,  subheaders[headers[10]][3], vertical_header_merge_format)

    worksheet.merge_range(3, 33, 4, 33, headers[11], vertical_header_merge_format_bold)

    worksheet.merge_range(3, 34, 3, 35, headers[12], header_merge_format_bold)
    worksheet.write(4, 34,  subheaders[headers[12]][0], vertical_header_merge_format)
    worksheet.write(4, 35,  subheaders[headers[12]][1], vertical_header_merge_format)

    worksheet.merge_range(3, 36, 3, 41, headers[13], header_merge_format_bold)
    worksheet.write(4, 36,  subheaders[headers[13]][0], vertical_header_merge_format)
    worksheet.write(4, 37,  subheaders[headers[13]][1], vertical_header_merge_format)
    worksheet.write(4, 38,  subheaders[headers[13]][2], vertical_header_merge_format)
    worksheet.write(4, 39,  subheaders[headers[13]][3], vertical_header_merge_format)
    worksheet.write(4, 40,  subheaders[headers[13]][4], vertical_header_merge_format)
    worksheet.write(4, 41,  subheaders[headers[13]][5], vertical_header_merge_format)


    worksheet.merge_range(3, 42, 3, 47, headers[15], header_merge_format_bold)
    worksheet.write(4, 42,  subheaders[headers[15]][0], vertical_header_merge_format)
    worksheet.write(4, 43, subheaders[headers[15]][1], vertical_header_merge_format)
    worksheet.write(4, 44, subheaders[headers[15]][2], vertical_header_merge_format)
    worksheet.write(4, 45,  subheaders[headers[15]][3], vertical_header_merge_format)
    worksheet.write(4, 46,  subheaders[headers[15]][4], vertical_header_merge_format)
    worksheet.write(4, 47, subheaders[headers[15]][5], vertical_header_merge_format)

    # worksheet.merge_range(3, 48, 3, 53, headers[15], header_merge_format_bold)
    # worksheet.write(4, 48,  subheaders[headers[15]][0], vertical_header_merge_format)
    # worksheet.write(4, 49,  subheaders[headers[15]][1], vertical_header_merge_format)
    # worksheet.write(4, 50,  subheaders[headers[15]][2], vertical_header_merge_format)
    # worksheet.write(4, 51,  subheaders[headers[15]][3], vertical_header_merge_format)
    # worksheet.write(4, 52,  subheaders[headers[15]][4], vertical_header_merge_format)
    # worksheet.write(4, 53,  subheaders[headers[15]][5], vertical_header_merge_format)


    worksheet.merge_range(3, 48, 3, 60, headers[17], header_merge_format_bold)
    worksheet.write(4, 48,  subheaders[headers[17]][0], vertical_header_merge_format)
    worksheet.write(4, 49,  subheaders[headers[17]][1], vertical_header_merge_format)
    worksheet.write(4, 50,  subheaders[headers[17]][2], vertical_header_merge_format)
    worksheet.write(4, 51,  subheaders[headers[17]][3], vertical_header_merge_format)
    worksheet.write(4, 52, subheaders[headers[17]][4], vertical_header_merge_format)
    worksheet.write(4, 53,  subheaders[headers[17]][5], vertical_header_merge_format)
    worksheet.write(4, 54,  subheaders[headers[17]][6], vertical_header_merge_format)
    worksheet.write(4, 55,  subheaders[headers[17]][7], vertical_header_merge_format)
    worksheet.write(4, 56, subheaders[headers[17]][8], vertical_header_merge_format)
    worksheet.write(4, 57, subheaders[headers[17]][9], vertical_header_merge_format)
    worksheet.write(4, 58,  subheaders[headers[17]][10], vertical_header_merge_format)
    worksheet.write(4, 59, subheaders[headers[17]][11], vertical_header_merge_format)
    worksheet.write(4, 60,  subheaders[headers[17]][12], vertical_header_merge_format)

    #Бошка давлатларда яшовчи фуқаролар фарзандлари
    worksheet.merge_range(3, 61, 3, 66, headers[14], header_merge_format_bold)
    worksheet.write(4,61,subheaders[headers[14]][0],vertical_header_merge_format)
    worksheet.write(4,62,subheaders[headers[14]][1],vertical_header_merge_format)
    worksheet.write(4,63,subheaders[headers[14]][2],vertical_header_merge_format)
    worksheet.write(4,64,subheaders[headers[14]][3],vertical_header_merge_format)
    worksheet.write(4,65,subheaders[headers[14]][4],vertical_header_merge_format)
    worksheet.write(4,66,subheaders[headers[14]][5],vertical_header_merge_format)


    # worksheet.merge_range(3, 61, 3,62, headers[16], header_merge_format_bold)
    # worksheet.write(4, 61,  subheaders[headers[16]][0], vertical_header_merge_format)
    # worksheet.write(4, 62, subheaders[headers[16]][2], vertical_header_merge_format)
    # worksheet.write(4, 63,  subheaders[headers[16]][2], vertical_header_merge_format)

    # juvenile_markaz_2024 = models.Juvenile_Markaz.objects.filter(accept_center_info__arrived_date__year=2024).exclude(status='1')
    # juvenile_markaz_2023 = models.Juvenile_Markaz.objects.filter(accept_center_info__arrived_date__year=2023).exclude(status='1')
    # juveniles_2024 = models.Juvenile.objects.filter(juvenile_markaz__in=juvenile_markaz_2024).distinct()
    # juveniles_2023 = models.Juvenile.objects.filter(juvenile_markaz__in=juvenile_markaz_2023).distinct()
    regions = Region.objects.all()
    i=0
    j=0
    while j < regions.count():
        worksheet.merge_range(i+5, 0, i+6, 0,  j+1,header_merge_format)
        worksheet.merge_range(i+5, 1, i+6, 1,  regions[j].name,header_merge_format)
        worksheet.write(i+5, 2,  2024,header_merge_format_bold)
        worksheet.write(i+6, 2,  2023,header_merge_format)
        #Жами қабул қилинганлар сони
        worksheet.write(i+5,3, base_query_2024.filter(markaz__region = regions[j]).count(),header_merge_format )
        worksheet.write(i+6,3, base_query_2023.filter(markaz__region = regions[j]).count(),header_merge_format )

        #қиз болалар
        worksheet.write(i+5,4, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__juvenile__gender='F').distinct().count(),header_merge_format)
        worksheet.write(i+6,4, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__juvenile__gender='F').distinct().count(),header_merge_format)

        #Қабул қилинганларни сақлаш муддатлари
        # query = query_taqsimlangan
        # 48 soat
        worksheet.write(i+5,5, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2024,markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(hours=48)

        ).distinct().count(),header_merge_format)

        worksheet.write(i+6,5, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2023,markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(hours=48)
        ).distinct().count(),header_merge_format)

        #10 kun
        worksheet.write(i+5,6, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2024,markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=2),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=10)

        ).distinct().count(),header_merge_format)

        worksheet.write(i+6,6, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2023,markaz__region=regions[j]).filter(
            time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=2),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=10)
        ).distinct().count(),header_merge_format)

        #20 kun
        worksheet.write(i+5,7, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2024,markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=10),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=20)
        ).distinct().count(),header_merge_format)

        worksheet.write(i+6,7, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2023,markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=10),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=20)
        ).distinct().count(),header_merge_format)

        #30 kun
        worksheet.write(i+5,8, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2024,markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=20),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=30)
        ).distinct().count(),header_merge_format)

        worksheet.write(i+6,8, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2023,markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=20),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=30)
        ).distinct().count(),header_merge_format)

        #45 kun
        worksheet.write(i+5,9, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2024,markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            # accept_center_info__arrived_date__lte=F('time_arrival_center') + timedelta(days=45),
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=30),
        ).distinct().count(),header_merge_format)

        worksheet.write(i+6,9, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2023,markaz__region = regions[j]).filter(
            # time_departure_center__isnull=False,
            # accept_center_info__arrived_date__lte=F('time_arrival_center') + timedelta(days=45),
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=30),
        ).distinct().count(),header_merge_format)

        #Олиб келинган жойлари

        #bozor
        worksheet.write(i+5,10, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__determined_location='1').distinct().count(),header_merge_format )
        worksheet.write(i+6,10, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__determined_location='1').distinct().count(),header_merge_format )

        #kocha
        worksheet.write(i+5,11, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__determined_location='3').distinct().count(),header_merge_format )
        worksheet.write(i+6,11, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__determined_location='3').distinct().count(),header_merge_format )

        #yer tola
        worksheet.write(i+5,12, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__determined_location='2').distinct().count(),header_merge_format )
        worksheet.write(i+6,12, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__determined_location='2').distinct().count(),header_merge_format )

        #boshqa joy
        worksheet.write(i+5,13, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__determined_location='4').distinct().count(),header_merge_format )
        worksheet.write(i+6,13, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__determined_location='4').distinct().count(),header_merge_format )

        #boshqa davlat
        worksheet.write(i+5,14, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__determined_location='5').distinct().count(),header_merge_format )
        worksheet.write(i+6,14, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__determined_location='5').distinct().count(),header_merge_format )

        #yoshi
        today = date.today()
        #3 yosh 6 yosh
        end_date = today - timedelta(days=3 * 365)
        start_date = today - timedelta(days=6 * 365)
        worksheet.write(i+5,15, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lte=end_date).distinct().count(),header_merge_format )
        worksheet.write(i+6,15, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lte=end_date).distinct().count(),header_merge_format )

        #7-13 yosh
        end_date = today - timedelta(days=6 * 365)
        start_date = today - timedelta(days=13 * 365)
        worksheet.write(i+5,16, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lt=end_date).distinct().count(),header_merge_format )
        worksheet.write(i+6,16, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lt=end_date).distinct().count(),header_merge_format )

        # 14-18 yosh
        end_date = today - timedelta(days=13 * 365)
        start_date = today - timedelta(days=20 * 365)
        worksheet.write(i+5,17, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lt=end_date).distinct().count(),header_merge_format )
        worksheet.write(i+6,17, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lt=end_date).distinct().count(),header_merge_format )
        #yoshi nomalum
        worksheet.write(i+5,18, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__juvenile__birth_date__isnull=True).distinct().count(),header_merge_format )
        worksheet.write(i+6,18, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__juvenile__birth_date__isnull=True).distinct().count(),header_merge_format )

        #Олиб келинганлардан

        #maktabgacha talim
        worksheet.write(i+5,19, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='1').distinct().count(),header_merge_format )
        worksheet.write(i+6,19, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='1').distinct().count(),header_merge_format )

        worksheet.write(i+5,20, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='2').distinct().count(),header_merge_format )
        worksheet.write(i+6,20, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='2').distinct().count(),header_merge_format )

        worksheet.write(i+5,21, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='3').distinct().count(),header_merge_format )
        worksheet.write(i+6,21, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='3').distinct().count(),header_merge_format )

        worksheet.write(i+5,22, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='4').distinct().count(),header_merge_format )
        worksheet.write(i+6,22, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='4').distinct().count(),header_merge_format )

        worksheet.write(i+5,23, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='5').distinct().count(),header_merge_format )
        worksheet.write(i+6,23, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='5').distinct().count(),header_merge_format )

        worksheet.write(i+5,24, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='6').distinct().count(),header_merge_format )
        worksheet.write(i+6,24, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='6').distinct().count(),header_merge_format )

        worksheet.write(i+5,25, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='7').distinct().count(),header_merge_format )
        worksheet.write(i+6,25, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='7').distinct().count(),header_merge_format )

        worksheet.write(i+5,26, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='8').distinct().count(),header_merge_format )
        worksheet.write(i+6,26, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='8').distinct().count(),header_merge_format )

        worksheet.write(i+5,27, base_query_2024.filter(markaz__region = regions[j]).filter(Q(juvenile__educationinfojuvenile__school_type='9')|Q(juvenile__juvenile__passport_type=5)).distinct().count(),header_merge_format )
        worksheet.write(i+6,27, base_query_2023.filter(markaz__region = regions[j]).filter(Q(juvenile__educationinfojuvenile__school_type='9')|Q(juvenile__juvenile__passport_type=5)).distinct().count(),header_merge_format )

        worksheet.write(i+5,28, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='10').distinct().count(),header_merge_format )
        worksheet.write(i+6,28, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__educationinfojuvenile__school_type='10').distinct().count(),header_merge_format )



        #oilaviy ahvoli ParentInfoJuvenile
        worksheet.write(i+5,29, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__marital_status='1').distinct().count(),header_merge_format )
        worksheet.write(i+6,29, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__marital_status='1').distinct().count(),header_merge_format )

        worksheet.write(i+5,30, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__marital_status='2').distinct().count(),header_merge_format )
        worksheet.write(i+6,30, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__marital_status='2').distinct().count(),header_merge_format )

        worksheet.write(i+5,31, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__marital_status='3').distinct().count(),header_merge_format )
        worksheet.write(i+6,31, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__marital_status='3').distinct().count(),header_merge_format )

        worksheet.write(i+5,32, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__marital_status='4').distinct().count(),header_merge_format )
        worksheet.write(i+6,32, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__marital_status='4').distinct().count(),header_merge_format )

        #profilaktik hisobda
        worksheet.write(i+5,33, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__prophylactic_list=True).distinct().count(),header_merge_format )
        worksheet.write(i+6,33, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__prophylactic_list=True).distinct().count(),header_merge_format )
        #
        # qayta joylashtirilaganlar
        two_times_2024 = base_query_2024.filter(markaz__region = regions[j]).values('juvenile','markaz').annotate(markaz_count=Count('id')).filter(markaz_count=2)
        two_times_2023 = base_query_2023.filter(markaz__region = regions[j]).values('juvenile','markaz').annotate(markaz_count=Count('id')).filter(markaz_count=2)
        two_more_times_2024 = base_query_2024.filter(markaz__region = regions[j]).values('juvenile','markaz').annotate(markaz_count=Count('id')).filter(markaz_count__gt=2)
        two_more_times_2023 = base_query_2024.filter(markaz__region = regions[j]).values('juvenile','markaz').annotate(markaz_count=Count('id')).filter(markaz_count__gt=2)

        worksheet.write(i+5,34, two_times_2024.count() ,header_merge_format )
        worksheet.write(i+6,34, two_times_2023.count(),header_merge_format )
        worksheet.write(i+5,35, two_more_times_2024.count(),header_merge_format )
        worksheet.write(i+6,35, two_more_times_2023.count(),header_merge_format )

        # #olib kelish sababi
        worksheet.write(i+5,36, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='1').distinct().count(),header_merge_format )
        worksheet.write(i+6,36, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='1').distinct().count(),header_merge_format )

        worksheet.write(i+5,37, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='2').distinct().count(),header_merge_format )
        worksheet.write(i+6,37, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='2').distinct().count(),header_merge_format )

        worksheet.write(i+5,38, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='3').distinct().count(),header_merge_format )
        worksheet.write(i+6,38, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='3').distinct().count(),header_merge_format )

        worksheet.write(i+5,39, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='4').distinct().count(),header_merge_format )
        worksheet.write(i+6,39, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='4').distinct().count(),header_merge_format )

        worksheet.write(i+5,40, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='5').distinct().count(),header_merge_format )
        worksheet.write(i+6,40, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='5').distinct().count(),header_merge_format )

        worksheet.write(i+5,41, base_query_2024.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='6').distinct().count(),header_merge_format )
        worksheet.write(i+6,41, base_query_2023.filter(markaz__region = regions[j]).filter(accept_center_info__sub_reason_bringing_child__parent__order='6').distinct().count(),header_merge_format )
        # worksheet.write(i+6,41, 'AAAA',header_merge_format )

        # #Бошка давлатларда яшовчи фуқаролар фарзандлари
        # worksheet.write(i+5,42, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__relationship__parent__is_abroad=True).count(),header_merge_format )
        # worksheet.write(i+6,42, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__relationship__parent__is_abroad=True).count(),header_merge_format )


        #Бошка давлатлардан олиб келинган қаровсиз қолган вояга етмаганлар
        worksheet.write(i+5,42, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__name='Russia').distinct().count(),header_merge_format )
        worksheet.write(i+6,42, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__name='Russia').distinct().count(),header_merge_format )
        #
        worksheet.write(i+5,43, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__name='Kazakhstan').distinct().count(),header_merge_format )
        worksheet.write(i+6,43, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__name='Kazakhstan').distinct().count(),header_merge_format )

        worksheet.write(i+5,44, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__name='Kyrgyzstan').distinct().count(),header_merge_format )
        worksheet.write(i+6,44, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__name='Kyrgyzstan').distinct().count(),header_merge_format )

        worksheet.write(i+5,45, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__name='Tajikistan').distinct().count(),header_merge_format )
        worksheet.write(i+6,45, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__name='Tajikistan').distinct().count(),header_merge_format )


        worksheet.write(i+5,46, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__name='Turkmenistan').distinct().count(),header_merge_format )
        worksheet.write(i+6,46, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__name='Turkmenistan').distinct().count(),header_merge_format )

        worksheet.write(i+5,47, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__isnull=False).exclude(juvenile__juvenile__foreign_country__name__in=['Russia','Kazakhstan','Kyrgyzstan','Tajikistan','Turkmenistan',]).distinct().count(),header_merge_format )
        worksheet.write(i+6,47, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__juvenile__foreign_country__isnull=False).exclude(juvenile__juvenile__foreign_country__name__in=['Russia','Kazakhstan','Kyrgyzstan','Tajikistan','Turkmenistan',]).distinct().count(),header_merge_format )


        #kimlarga topshirilgan
        # boshqa markazga yuborilgan
        worksheet.write(i+5,48, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j]) & Q(status='8') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,48, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j]) & Q(status='8') ).distinct().count(),header_merge_format )

        # ota-ona yoki ornini bosuvchi
        worksheet.write(i + 5, 49, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j])).filter(Q(distributed_info__distribution_type='1') | Q(distributed_info__distribution_type='8')).distinct().count(), header_merge_format)
        worksheet.write(i+6,49, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j])).filter(Q(distributed_info__distribution_type='1')| Q(distributed_info__distribution_type='8')).distinct().count(),header_merge_format )

        #rotm ogil bola
        worksheet.write(i+5,50, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j]) & Q(distributed_info__rotm_type='2') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,50, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j]) & Q(distributed_info__rotm_type='2') ).distinct().count(),header_merge_format )
        #qiz ogil bola
        worksheet.write(i+5,51, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j]) & Q(distributed_info__rotm_type='1') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,51, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j]) & Q(distributed_info__rotm_type='1') ).distinct().count(),header_merge_format )

        #itm
        worksheet.write(i+5,52, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j]) & Q(distributed_info__distribution_type='3') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,52, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j]) & Q(distributed_info__distribution_type='3') ).distinct().count(),header_merge_format )

        #mehribonlik uyi
        worksheet.write(i+5,53, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j]) & Q(distributed_info__type_guardianship='5') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,53, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j]) & Q(distributed_info__type_guardianship='5') ).distinct().count(),header_merge_format )

        #sos bolalar
        worksheet.write(i+5,54, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j]) & Q(distributed_info__type_guardianship='7') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,54, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j]) & Q(distributed_info__type_guardianship='7') ).distinct().count(),header_merge_format )

        #oilaviy bolalar uyi
        worksheet.write(i+5,55, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j]) & Q(distributed_info__type_guardianship='6') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,55, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j]) & Q(distributed_info__type_guardianship='6') ).distinct().count(),header_merge_format )

        #patronat
        worksheet.write(i+5,56, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j]) & Q(distributed_info__type_guardianship='3') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,56, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j]) & Q(distributed_info__type_guardianship='3') ).distinct().count(),header_merge_format )

        #farzandlik
        worksheet.write(i+5,57, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j]) & Q(distributed_info__type_guardianship='4') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,57, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j]) & Q(distributed_info__type_guardianship='4') ).distinct().count(),header_merge_format )

        #vasiy homiy
        worksheet.write(i+5,58, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j])).filter(Q(distributed_info__type_guardianship='1') | Q(distributed_info__type_guardianship='2')).exclude(distributed_info__distribution_type='1').distinct().count(),header_merge_format )
        worksheet.write(i+6,58, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j])).filter(Q(distributed_info__type_guardianship='1') | Q(distributed_info__type_guardianship='2')).exclude(distributed_info__distribution_type='1').distinct().count(),header_merge_format )

        #sogliqni saqlash
        worksheet.write(i+5,59, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j]) & Q(distributed_info__distribution_type='5') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,59, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j]) & Q(distributed_info__distribution_type='5') ).distinct().count(),header_merge_format )

        #boshqa davlatga yuborish
        worksheet.write(i+5,60, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz__region = regions[j]) & Q(distributed_info__distribution_type='7') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,60, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz__region = regions[j]) & Q(distributed_info__distribution_type='7') ).distinct().count(),header_merge_format )

        #Бошка давлатларда яшовчи фуқаролар фарзандлари

        worksheet.write(i + 5, 61, 0, header_merge_format)
        worksheet.write(i + 6, 61, 0, header_merge_format)

        worksheet.write(i + 5, 62, 0, header_merge_format)
        worksheet.write(i + 6, 62, 0, header_merge_format)

        worksheet.write(i + 5, 63, 0, header_merge_format)
        worksheet.write(i + 6, 63, 0, header_merge_format)

        worksheet.write(i + 5, 64, 0, header_merge_format)
        worksheet.write(i + 6, 64, 0, header_merge_format)

        worksheet.write(i + 5, 65, 0, header_merge_format)
        worksheet.write(i + 6, 65, 0, header_merge_format)

        worksheet.write(i + 5, 66, 0, header_merge_format)
        worksheet.write(i + 6, 66, 0, header_merge_format)


        j+=1
        i+=2



                                #respublika boyicha

    worksheet.merge_range(33,0, 34,1, "Respublik bo'yicha",header_merge_format_bold)
    worksheet.write(33,2, 2024,header_merge_format_bold)
    worksheet.write(34,2, 2023,header_merge_format)

    # Жами қабул қилинганлар сони

    worksheet.write(33,3,base_query_2024.count(),header_merge_format_bold)
    worksheet.write(34,3,base_query_2023.count(),header_merge_format)


    # # қиз болалар

    worksheet.write(33, 4,
                    respublika_base_query_2024.filter(juvenile__juvenile__gender='F').distinct().count(),
                    header_merge_format_bold)
    worksheet.write(34, 4,
                    respublika_base_query_2023.filter(juvenile__juvenile__gender='F').distinct().count(),
                    header_merge_format)

    # Қабул қилинганларни сақлаш муддатлари
    # 48 soat
    worksheet.write(33, 5, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2024,
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(days=2)

    ).distinct().count(), header_merge_format_bold)

    worksheet.write(34, 5, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2023,
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(days=2)
    ).distinct().count(), header_merge_format)

    # 10 kun
    worksheet.write(33, 6, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2024,
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__lt = F('time_departure_center') - timedelta(days=2),
        accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(days=10)
    ).distinct().count(), header_merge_format_bold)

    worksheet.write(34, 6, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2023,
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__lt = F('time_departure_center') - timedelta(days=2),
        accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(days=10)
    ).distinct().count(), header_merge_format)

    # 20 kun
    worksheet.write(33, 7, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2024,
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__lt = F('time_departure_center') - timedelta(days=10),
        accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(days=20)
    ).distinct().count(), header_merge_format_bold)

    worksheet.write(34, 7, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2023,
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__lt = F('time_departure_center') - timedelta(days=10),
        accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(days=20)
    ).distinct().count(), header_merge_format)
    # 30 kun
    worksheet.write(33, 8, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2024,
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__lt = F('time_departure_center') - timedelta(days=20),
        accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(days=30)
    ).distinct().count(), header_merge_format_bold)

    worksheet.write(34, 8, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2023,
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__lt = F('time_departure_center') - timedelta(days=20),
        accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(days=30)
    ).distinct().count(), header_merge_format)

    # 45 kun
    worksheet.write(33, 9, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2024,
        # time_departure_center__isnull=False,
        # accept_center_info__arrived_date__lte=F('time_arrival_center') + timedelta(days=45),
        accept_center_info__arrived_date__lt = F('time_departure_center') - timedelta(days=30),
    ).distinct().count(), header_merge_format_bold)

    worksheet.write(34, 9, query_taqsimlangan.filter(accept_center_info__arrived_date__year=2023,
        # time_departure_center__isnull=False,
        # accept_center_info__arrived_date__lte=F('time_arrival_center') + timedelta(days=45),
        accept_center_info__arrived_date__lt = F('time_departure_center') - timedelta(days=30),
    ).distinct().count(), header_merge_format)

    # Олиб келинган жойлари

    # bozor
    worksheet.write(33, 10, respublika_base_query_2024.filter(
        accept_center_info__determined_location='1').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 10, respublika_base_query_2023.filter(
        accept_center_info__determined_location='1').distinct().count(), header_merge_format)

    # kocha
    worksheet.write(33, 11, respublika_base_query_2024.filter(
        accept_center_info__determined_location='3').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 11, respublika_base_query_2023.filter(
        accept_center_info__determined_location='3').distinct().count(), header_merge_format)

    # yer tola
    worksheet.write(33, 12, respublika_base_query_2024.filter(
        accept_center_info__determined_location='2').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 12, respublika_base_query_2023.filter(
        accept_center_info__determined_location='2').distinct().count(), header_merge_format)

    # boshqa joy
    worksheet.write(33, 13, respublika_base_query_2024.filter(
        accept_center_info__determined_location='4').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 13, respublika_base_query_2023.filter(
        accept_center_info__determined_location='4').distinct().count(), header_merge_format)

    # boshqa davlat
    worksheet.write(33, 14, respublika_base_query_2024.filter(
        accept_center_info__determined_location='5').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 14, respublika_base_query_2023.filter(
        accept_center_info__determined_location='5').distinct().count(), header_merge_format)

    # yoshi
    today = date.today()
    # 3 yosh 6 yosh
    end_date = today - timedelta(days=3 * 365)
    start_date = today - timedelta(days=6 * 365)
    worksheet.write(33, 15, respublika_base_query_2024.filter(
        juvenile__juvenile__birth_date__gte=start_date, juvenile__juvenile__birth_date__lte=end_date).distinct().count(),
                    header_merge_format_bold)
    worksheet.write(34, 15, respublika_base_query_2023.filter(
        juvenile__juvenile__birth_date__gte=start_date, juvenile__juvenile__birth_date__lte=end_date).distinct().count(),
                    header_merge_format)

    # 7-13 yosh
    end_date = today - timedelta(days=6 * 365)
    start_date = today - timedelta(days=13 * 365)
    worksheet.write(33, 16, respublika_base_query_2024.filter(
        juvenile__juvenile__birth_date__gte=start_date, juvenile__juvenile__birth_date__lt=end_date).distinct().count(),
                    header_merge_format_bold)
    worksheet.write(34, 16, respublika_base_query_2023.filter(
        juvenile__juvenile__birth_date__gte=start_date, juvenile__juvenile__birth_date__lt=end_date).distinct().count(),
                    header_merge_format)

    # 14-18 yosh
    end_date = today - timedelta(days=13 * 365)
    start_date = today - timedelta(days=20 * 365)
    worksheet.write(33, 17, respublika_base_query_2024.filter(
        juvenile__juvenile__birth_date__gte=start_date, juvenile__juvenile__birth_date__lt=end_date).distinct().count(),
                    header_merge_format_bold)
    worksheet.write(34, 17, respublika_base_query_2023.filter(
        juvenile__juvenile__birth_date__gte=start_date, juvenile__juvenile__birth_date__lt=end_date).distinct().count(),
                    header_merge_format)
    # yoshi nomalum
    worksheet.write(33, 18, respublika_base_query_2024.filter(
        juvenile__juvenile__birth_date__isnull=True).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 18, respublika_base_query_2023.filter(
        juvenile__juvenile__birth_date__isnull=True).distinct().count(), header_merge_format)

    # Олиб келинганлардан

    # maktabgacha talim
    worksheet.write(33, 19, respublika_base_query_2024.filter(
        juvenile__educationinfojuvenile__school_type='1').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 19, respublika_base_query_2023.filter(
        juvenile__educationinfojuvenile__school_type='1').distinct().count(), header_merge_format)

    worksheet.write(33, 20, respublika_base_query_2024.filter(
        juvenile__educationinfojuvenile__school_type='2').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 20, respublika_base_query_2023.filter(
        juvenile__educationinfojuvenile__school_type='2').distinct().count(), header_merge_format)

    worksheet.write(33, 21, respublika_base_query_2024.filter(
        juvenile__educationinfojuvenile__school_type='3').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 21, respublika_base_query_2023.filter(
        juvenile__educationinfojuvenile__school_type='3').distinct().count(), header_merge_format)

    worksheet.write(33, 22, respublika_base_query_2024.filter(
        juvenile__educationinfojuvenile__school_type='4').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 22, respublika_base_query_2023.filter(
        juvenile__educationinfojuvenile__school_type='4').distinct().count(), header_merge_format)

    worksheet.write(33, 23, respublika_base_query_2024.filter(
        juvenile__educationinfojuvenile__school_type='5').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 23, respublika_base_query_2023.filter(
        juvenile__educationinfojuvenile__school_type='5').distinct().count(), header_merge_format)

    worksheet.write(33, 24, respublika_base_query_2024.filter(
        juvenile__educationinfojuvenile__school_type='6').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 24, respublika_base_query_2023.filter(
        juvenile__educationinfojuvenile__school_type='6').distinct().count(), header_merge_format)

    worksheet.write(33, 25, respublika_base_query_2024.filter(
        juvenile__educationinfojuvenile__school_type='7').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 25, respublika_base_query_2023.filter(
        juvenile__educationinfojuvenile__school_type='7').distinct().count(), header_merge_format)

    worksheet.write(33, 26, respublika_base_query_2024.filter(
        juvenile__educationinfojuvenile__school_type='8').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 26, respublika_base_query_2023.filter(
        juvenile__educationinfojuvenile__school_type='8').distinct().count(), header_merge_format)

    worksheet.write(33, 27, respublika_base_query_2024.filter(
        Q(juvenile__educationinfojuvenile__school_type='9')|Q(juvenile__juvenile__passport_type=5)).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 27, respublika_base_query_2023.filter(
        Q(juvenile__educationinfojuvenile__school_type='9')|Q(juvenile__juvenile__passport_type=5)).distinct().count(), header_merge_format)

    worksheet.write(33, 28, respublika_base_query_2024.filter(
        juvenile__educationinfojuvenile__school_type='10').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 28, respublika_base_query_2023.filter(
        juvenile__educationinfojuvenile__school_type='10').distinct().count(), header_merge_format)

    # oilaviy ahvoli ParentInfoJuvenile
    worksheet.write(33, 29, respublika_base_query_2024.filter(
        juvenile__parentinfojuvenile__marital_status='1').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 29, respublika_base_query_2023.filter(
        juvenile__parentinfojuvenile__marital_status='1').distinct().count(), header_merge_format)

    worksheet.write(33, 30, respublika_base_query_2024.filter(
        juvenile__parentinfojuvenile__marital_status='2').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 30, respublika_base_query_2023.filter(
        juvenile__parentinfojuvenile__marital_status='2').distinct().count(), header_merge_format)

    worksheet.write(33, 31, respublika_base_query_2024.filter(
        juvenile__parentinfojuvenile__marital_status='3').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 31, respublika_base_query_2023.filter(
        juvenile__parentinfojuvenile__marital_status='3').distinct().count(), header_merge_format)

    worksheet.write(33, 32, respublika_base_query_2024.filter(
        juvenile__parentinfojuvenile__marital_status='4').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 32, respublika_base_query_2023.filter(
        juvenile__parentinfojuvenile__marital_status='4').distinct().count(), header_merge_format)

    # profilaktik hisobda
    worksheet.write(33, 33, respublika_base_query_2024.filter(
        accept_center_info__prophylactic_list=True).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 33, respublika_base_query_2023.filter(
        accept_center_info__prophylactic_list=True).distinct().count(), header_merge_format)
    #
    # qayta joylashtirilaganlar
    # qayta joylashtirilaganlar
    two_times_2024 = base_query_2024.values('juvenile', 'markaz').annotate(
        markaz_count=Count('id')).filter(markaz_count=2)
    two_times_2023 = base_query_2023.values('juvenile', 'markaz').annotate(
        markaz_count=Count('id')).filter(markaz_count=2)
    two_more_times_2024 = base_query_2024.values('juvenile', 'markaz').annotate(
        markaz_count=Count('id')).filter(markaz_count__gt=2)
    two_more_times_2023 = base_query_2024.values('juvenile', 'markaz').annotate(
        markaz_count=Count('id')).filter(markaz_count__gt=2)

    worksheet.write(33, 34, two_times_2024.count(), header_merge_format)
    worksheet.write(34, 34, two_times_2023.count(), header_merge_format)
    worksheet.write(33, 35, two_more_times_2024.count(), header_merge_format)
    worksheet.write(34, 35, two_more_times_2023.count(), header_merge_format)

    # worksheet.write(33, 34, respublika_base_query_2024.filter(
    #     juvenile__accepted_center_number=2).distinct().count(), header_merge_format_bold)
    # worksheet.write(34, 34, respublika_base_query_2023.filter(
    #     juvenile__accepted_center_number=2).distinct().count(), header_merge_format)
    # worksheet.write(33, 35, respublika_base_query_2024.filter(
    #     juvenile__accepted_center_number__gt=2).distinct().count(), header_merge_format_bold)
    # worksheet.write(34, 35, respublika_base_query_2023.filter(
    #     juvenile__accepted_center_number__gt=2).distinct().count(), header_merge_format)

    # #olib kelish sababi
    worksheet.write(33, 36, respublika_base_query_2024.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='1').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 36, respublika_base_query_2023.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='1').distinct().count(), header_merge_format)

    worksheet.write(33, 37, respublika_base_query_2024.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='2').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 37, respublika_base_query_2023.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='2').distinct().count(), header_merge_format)

    worksheet.write(33, 38, respublika_base_query_2024.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='3').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 38, respublika_base_query_2023.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='3').distinct().count(), header_merge_format)

    worksheet.write(33, 39, respublika_base_query_2024.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='4').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 39, respublika_base_query_2023.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='4').distinct().count(), header_merge_format)

    worksheet.write(33, 40, respublika_base_query_2024.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='5').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 40, respublika_base_query_2023.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='5').distinct().count(), header_merge_format)

    worksheet.write(33, 41, respublika_base_query_2024.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='6').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 41, respublika_base_query_2023.filter(
        accept_center_info__sub_reason_bringing_child__parent__order='6').distinct().count(), header_merge_format)
    # worksheet.write(i+6,41, 'AAAA',header_merge_format )

    # Бошка давлатларда яшовчи фуқаролар фарзандлари
    # worksheet.write(i+5,42, base_query_2024.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__relationship__parent__is_abroad=True).count(),header_merge_format )
    # worksheet.write(i+6,42, base_query_2023.filter(markaz__region = regions[j]).filter(juvenile__parentinfojuvenile__relationship__parent__is_abroad=True).count(),header_merge_format )

    # Бошка давлатлардан олиб келинган қаровсиз қолган вояга етмаганлар
    worksheet.write(33, 42, respublika_base_query_2024.filter(
        juvenile__juvenile__foreign_country__name='Russia').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 42, respublika_base_query_2023.filter(
        juvenile__juvenile__foreign_country__name='Russia').distinct().count(), header_merge_format)
    #
    worksheet.write(33, 43, respublika_base_query_2024.filter(
        juvenile__juvenile__foreign_country__name='Kazakhstan').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 43, respublika_base_query_2023.filter(
        juvenile__juvenile__foreign_country__name='Kazakhstan').distinct().count(), header_merge_format)

    worksheet.write(33, 44, respublika_base_query_2024.filter(
        juvenile__juvenile__foreign_country__name='Kyrgyzstan').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 44, respublika_base_query_2023.filter(
        juvenile__juvenile__foreign_country__name='Kyrgyzstan').distinct().count(), header_merge_format)

    worksheet.write(33, 45, respublika_base_query_2024.filter(
        juvenile__juvenile__foreign_country__name='Tajikistan').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 45, respublika_base_query_2023.filter(
        juvenile__juvenile__foreign_country__name='Tajikistan').distinct().count(), header_merge_format)

    worksheet.write(33, 46, respublika_base_query_2024.filter(
        juvenile__juvenile__foreign_country__name='Turkmenistan').distinct().count(), header_merge_format_bold)
    worksheet.write(34, 46, respublika_base_query_2023.filter(
        juvenile__juvenile__foreign_country__name='Turkmenistan').distinct().count(), header_merge_format)

    worksheet.write(33, 47, respublika_base_query_2024.filter(
        juvenile__juvenile__foreign_country__isnull=False).exclude(
        juvenile__juvenile__foreign_country__name__in=['Russia', 'Kazakhstan', 'Kyrgyzstan', 'Tajikistan',
                                                       'Turkmenistan', ]).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 47, respublika_base_query_2023.filter(
        juvenile__juvenile__foreign_country__isnull=False).exclude(
        juvenile__juvenile__foreign_country__name__in=['Russia', 'Kazakhstan', 'Kyrgyzstan', 'Tajikistan',
                                                       'Turkmenistan', ]).distinct().count(), header_merge_format)

    # kimlarga topshirilgan
    # boshqa markazga yuborilgan
    worksheet.write(33, 48, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2024) & Q(
            status='8')).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 48, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2023) & Q(
            status='8')).distinct().count(), header_merge_format)

    # ota-ona yoki ornini bosuvchi
    worksheet.write(33, 49, query_taqsimlangan.filter(
        accept_center_info__arrived_date__year=2024).filter(
        Q(distributed_info__distribution_type='1') | Q(distributed_info__distribution_type='8')).distinct().count(),
                    header_merge_format_bold)
    worksheet.write(34, 49, query_taqsimlangan.filter(
        accept_center_info__arrived_date__year=2023).filter(
        Q(distributed_info__distribution_type='1') | Q(distributed_info__distribution_type='8')).distinct().count(),
                    header_merge_format)

    # rotm ogil bola
    worksheet.write(33, 50, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2024) & Q(distributed_info__rotm_type='2')).distinct().count(),
                    header_merge_format_bold)
    worksheet.write(34, 50, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2023) & Q(distributed_info__rotm_type='2')).distinct().count(),
                    header_merge_format)
    # qiz ogil bola
    worksheet.write(33, 51, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2024)  & Q(distributed_info__rotm_type='1')).distinct().count(),
                    header_merge_format_bold)
    worksheet.write(34, 51, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2023) & Q(distributed_info__rotm_type='1')).distinct().count(),
                    header_merge_format)

    # itm
    worksheet.write(33, 52, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2024)  & Q(
            distributed_info__distribution_type='3')).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 52, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2023) & Q(
            distributed_info__distribution_type='3')).distinct().count(), header_merge_format)

    # mehribonlik uyi
    worksheet.write(33, 53, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2024) & Q(
            distributed_info__type_guardianship='5')).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 53, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2023) & Q(
            distributed_info__type_guardianship='5')).distinct().count(), header_merge_format)

    # sos bolalar
    worksheet.write(33, 54, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2024)  & Q(
            distributed_info__type_guardianship='7')).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 54, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2023) & Q(
            distributed_info__type_guardianship='7')).distinct().count(), header_merge_format)

    # oilaviy bolalar uyi
    worksheet.write(33, 55, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2024) & Q(
            distributed_info__type_guardianship='6')).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 55, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2023) & Q(
            distributed_info__type_guardianship='6')).distinct().count(), header_merge_format)

    # patronat
    worksheet.write(33, 56, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2024) & Q(
            distributed_info__type_guardianship='3')).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 56, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2023)  & Q(
            distributed_info__type_guardianship='3')).distinct().count(), header_merge_format)

    # farzandlik
    worksheet.write(33, 57, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2024) & Q(
            distributed_info__type_guardianship='4')).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 57, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2023) & Q(
            distributed_info__type_guardianship='4')).distinct().count(), header_merge_format)

    # vasiy homiy
    worksheet.write(33, 58, query_taqsimlangan.filter(
        accept_center_info__arrived_date__year=2024).filter(
        Q(distributed_info__type_guardianship='1') | Q(distributed_info__type_guardianship='2')).exclude(distributed_info__distribution_type='1').distinct().count(),
                    header_merge_format_bold)
    worksheet.write(34, 58, query_taqsimlangan.filter(
        accept_center_info__arrived_date__year=2023).filter(
        Q(distributed_info__type_guardianship='1') | Q(distributed_info__type_guardianship='2')).exclude(distributed_info__distribution_type='1').distinct().count(),
                    header_merge_format)

    # sogliqni saqlash
    worksheet.write(33, 59, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2024) & Q(
            distributed_info__distribution_type='5')).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 59, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2023)  & Q(
            distributed_info__distribution_type='5')).distinct().count(), header_merge_format)

    # boshqa davlatga yuborish
    worksheet.write(33, 60, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2024) & Q(
            distributed_info__distribution_type='7')).distinct().count(), header_merge_format_bold)
    worksheet.write(34, 60, query_taqsimlangan.filter(
        Q(accept_center_info__arrived_date__year=2023)  & Q(
            distributed_info__distribution_type='7')).distinct().count(), header_merge_format)

    #Бошка давлатларда яшовчи фуқаролар фарзандлари
    worksheet.write(33, 61, 0, header_merge_format_bold)
    worksheet.write(34, 61, 0, header_merge_format)

    worksheet.write(33, 62, 0, header_merge_format_bold)
    worksheet.write(34, 62, 0, header_merge_format)

    worksheet.write(33, 63, 0, header_merge_format_bold)
    worksheet.write(34, 63, 0, header_merge_format)

    worksheet.write(33, 64, 0, header_merge_format_bold)
    worksheet.write(34, 64, 0, header_merge_format)

    worksheet.write(33, 65, 0, header_merge_format_bold)
    worksheet.write(34, 65, 0, header_merge_format)

    worksheet.write(33, 66, 0, header_merge_format_bold)
    worksheet.write(34, 66, 0, header_merge_format)


    workbook.close()
    return file_path








             ####  center_9_to_excel ########

def apparat_to_excel_7_1(request):
    date_from = request.GET.get('date_from')

    date_to = request.GET.get('date_to')
    time_date_to = datetime.strptime(date_to,'%Y-%m-%d').date()

    date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

    last_year = int(format(datetime.now(), '%Y'))
    if date_from and date_to:
        base_query = models.Juvenile_Markaz.objects.filter(
        status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], accept_center_info__arrived_date__range=[date_from,date_to])
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13'],accept_center_info__arrived_date__range=[date_from,date_to])

    else:
        base_query = models.Juvenile_Markaz.objects.filter(
            status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], accept_center_info__arrived_date__year=last_year)
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13'],accept_center_info__arrived_date__year=last_year)

    local_time = datetime.now(pytz.timezone('Asia/Tashkent'))
    download_time = format(local_time, '%Y-%m-%d-%H-%M-%S')

    workbook = xlsxwriter.Workbook(f"media/apparat_statistics_7_1___{download_time}.xlsx")
    worksheet = workbook.add_worksheet("Statistics")
    # domain_name = 'http://127.0.0.1:8000/'
    domain_name = env('DOMAIN_NAME')

    file_path = f'{domain_name}/{workbook.filename}'

    header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        # 'fg_color': '#F0F4FF'
    })
    header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        'fg_color': '#F0F4FF'
    })

    header_merge_format.set_border_color("#1d588b")

    header_merge_format_bold.set_border_color("#1d588b")
    # wrap_format_horizontal = workbook.add_format({'text_wrap': True,
    #                                    'bold': 1,
    #                                    'border': 1,
    #                                    'align': 'center',
    #                                    'valign': 'vcenter',
    #                                    })

    vertical_header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14
        # 'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14,
        'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format.set_rotation(90)
    vertical_header_merge_format.set_border_color("#1d588b")
    vertical_header_merge_format_bold.set_rotation(90)
    vertical_header_merge_format_bold.set_border_color("#1d588b")

    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    merge_format.set_border_color("#1d588b")

    file_name_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
    })

    bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'
    })
    bold.set_rotation(90)
    bold.set_border_color("#1d588b")

    worksheet.set_column(0,0, 1)
    worksheet.set_column(1, 1, 20)
    worksheet.set_column(2,2,30)
    worksheet.set_column(3, 69, 20)
    # worksheet.set_column(4, 5, 30)
    # worksheet.set_column(6, 32, 12)
    # worksheet.set_column(33, 33, 12)
    # worksheet.set_column(34, 69, 8)
    # worksheet.set_column(10, 16, 40)

    worksheet.merge_range(2, 1, 3, 1, '№', header_merge_format_bold)
    worksheet.merge_range(2, 2, 3, 2, headers[1], header_merge_format_bold)
    # worksheet.merge_range(2, 2, 3, 2, headers_2[0], header_merge_format_bold)
    worksheet.merge_range(2, 3, 3, 3, headers_2[1], header_merge_format_bold)

    worksheet.merge_range(2, 4, 2 ,5, headers_2[2], header_merge_format_bold)
    worksheet.write(3,4, subheaders_2[headers_2[2]][0],header_merge_format)
    worksheet.write(3,5, subheaders_2[headers_2[2]][1],header_merge_format)


    worksheet.merge_range(2, 6, 2, 9, headers_2[3], header_merge_format_bold)
    # worksheet.write(4, 5, subheaders[headers[6]][0], header_merge_format_bold)
    worksheet.write(3, 6, subheaders_2[headers_2[3]][0], header_merge_format)
    worksheet.write(3, 7, subheaders_2[headers_2[3]][1], header_merge_format)
    worksheet.write(3, 8, subheaders_2[headers_2[3]][2], header_merge_format)
    worksheet.write(3, 9, subheaders_2[headers_2[3]][3], header_merge_format)

    worksheet.merge_range(2, 10, 2, 19, headers_2[4], header_merge_format_bold)
    worksheet.write(3,10,subheaders_2[headers_2[4]][0],header_merge_format)
    worksheet.write(3,11,subheaders_2[headers_2[4]][1],header_merge_format)
    worksheet.write(3,12,subheaders_2[headers_2[4]][2],header_merge_format)
    worksheet.write(3,13,subheaders_2[headers_2[4]][3],header_merge_format)
    worksheet.write(3,14,subheaders_2[headers_2[4]][4],header_merge_format)
    worksheet.write(3,15,subheaders_2[headers_2[4]][5],header_merge_format)
    worksheet.write(3,16,subheaders_2[headers_2[4]][6],header_merge_format)
    worksheet.write(3,17,subheaders_2[headers_2[4]][7],header_merge_format)
    worksheet.write(3,18,subheaders_2[headers_2[4]][8],header_merge_format)
    worksheet.write(3,19,subheaders_2[headers_2[4]][9],header_merge_format)


    worksheet.merge_range(2, 20, 2, 22, headers_2[5], header_merge_format_bold)
    worksheet.write(3,20,subheaders_2[headers_2[5]][0],header_merge_format)
    worksheet.write(3,21,subheaders_2[headers_2[5]][1],header_merge_format)
    worksheet.write(3,22,subheaders_2[headers_2[5]][2],header_merge_format)

    worksheet.merge_range(2, 23, 2, 24, headers_2[6], header_merge_format_bold)
    worksheet.write(3,23,subheaders_2[headers_2[6]][0],header_merge_format)
    worksheet.write(3,24,subheaders_2[headers_2[6]][1],header_merge_format)

    worksheet.merge_range(2, 25, 2, 29, headers_2[7], header_merge_format_bold)
    worksheet.write(3,25,subheaders_2[headers_2[7]][0],header_merge_format)
    worksheet.write(3,26,subheaders_2[headers_2[7]][1],header_merge_format)
    worksheet.write(3,27,subheaders_2[headers_2[7]][2],header_merge_format)
    worksheet.write(3,28,subheaders_2[headers_2[7]][3],header_merge_format)
    worksheet.write(3,29,subheaders_2[headers_2[7]][4],header_merge_format)


    regions = Region.objects.all()
    i = 0
    j = 0
    while j < regions.count():
        worksheet.write(i + 4, 1,  j + 1, header_merge_format)
        worksheet.write(i + 4, 2,  regions[j].name, header_merge_format)

        # jami joylashtirilganla
        worksheet.write(i + 4, 3, base_query.filter(markaz__region=regions[j]).distinct().count(), header_merge_format)

        #shundan
        #boshqa davlatdan olib kelingan
        worksheet.write(i+4, 4, base_query.filter(markaz__region=regions[j]).filter(accept_center_info__determined_location='5').distinct().count(),header_merge_format)
        worksheet.write(i+4, 5, base_query.filter(markaz__region=regions[j]).filter(juvenile__juvenile__passport_type='5').distinct().count(),header_merge_format)

        #kimlar tomonidan olib kelingan
        worksheet.write(i+4, 6, base_query.filter(markaz__region=regions[j]).filter(accept_center_info__inspector__inspector_type='1').distinct().count(),header_merge_format)
        worksheet.write(i+4, 7, base_query.filter(markaz__region=regions[j]).filter(accept_center_info__inspector__inspector_type='2').distinct().count(),header_merge_format)
        worksheet.write(i+4, 8, base_query.filter(markaz__region=regions[j]).filter(accept_center_info__inspector__inspector_type='3').distinct().count(),header_merge_format)
        worksheet.write(i+4, 9, base_query.filter(markaz__region=regions[j]).filter(Q(accept_center_info__inspector__inspector_type='4')|Q(accept_center_info__inspector__inspector_type=None)).distinct().count(),header_merge_format)


        #talim turi
        worksheet.write(i+4 ,10 ,base_query.filter(markaz__region=regions[j]).filter(juvenile__educationinfojuvenile__school_type='1').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,11 ,base_query.filter(markaz__region=regions[j]).filter(juvenile__educationinfojuvenile__school_type='2').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,12 ,base_query.filter(markaz__region=regions[j]).filter(juvenile__educationinfojuvenile__school_type='3').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,13 ,base_query.filter(markaz__region=regions[j]).filter(juvenile__educationinfojuvenile__school_type='4').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,14 ,base_query.filter(markaz__region=regions[j]).filter(juvenile__educationinfojuvenile__school_type='5').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,15 ,base_query.filter(markaz__region=regions[j]).filter(juvenile__educationinfojuvenile__school_type='6').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,16 ,base_query.filter(markaz__region=regions[j]).filter(juvenile__educationinfojuvenile__school_type='7').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,17 ,base_query.filter(markaz__region=regions[j]).filter(juvenile__educationinfojuvenile__school_type='8').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,18 ,base_query.filter(markaz__region=regions[j]).filter(Q(juvenile__educationinfojuvenile__school_type='9')|Q(juvenile__juvenile__passport_type=5)).distinct().count(),header_merge_format)
        worksheet.write(i+4 ,19 ,base_query.filter(markaz__region=regions[j]).filter(juvenile__educationinfojuvenile__school_type='10').distinct().count(),header_merge_format)

        # yoshi
        # 3 yosh 6 yosh

        today = date.today()
        end_date = today - timedelta(days=3 * 365)  #2023
        start_date = today - timedelta(days=6 * 365)  #2017
        worksheet.write(i + 4, 20, base_query.filter(markaz__region=regions[j]).filter(juvenile__juvenile__birth_date__gte=start_date,
             juvenile__juvenile__birth_date__lte=end_date).distinct().count(),header_merge_format)

        # 7 yosh 13 yosh
        today = date.today()
        end_date = today - timedelta(days=6 * 365)  #2016
        start_date = today - timedelta(days=13 * 365) #2010
        worksheet.write(i + 4, 21, base_query.filter(markaz__region=regions[j]).filter(
            juvenile__juvenile__birth_date__gte=start_date,
            juvenile__juvenile__birth_date__lt=end_date).distinct().count(), header_merge_format)

        # 14 yosh 18 yosh
        today = date.today()
        end_date = today - timedelta(days=13 * 365)
        start_date = today - timedelta(days=20 * 365)
        worksheet.write(i + 4, 22, base_query.filter(markaz__region=regions[j]).filter(
            juvenile__juvenile__birth_date__gte=start_date,
            juvenile__juvenile__birth_date__lt=end_date).distinct().count(), header_merge_format)


        #jinsi
        worksheet.write(i + 4, 23, base_query.filter(markaz__region=regions[j]).filter(juvenile__juvenile__gender='M').distinct().count(),header_merge_format)
        worksheet.write(i + 4, 24, base_query.filter(markaz__region=regions[j]).filter(juvenile__juvenile__gender='F').distinct().count(),header_merge_format)

        #saqlangan muddatlar
        # 2 kungacha
        worksheet.write(i + 4, 25, query_taqsimlangan.filter(markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=2)
        ).distinct().count(), header_merge_format)


        # 10 kun
        worksheet.write(i + 4, 26, query_taqsimlangan.filter(markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=2),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=10)

        ).distinct().count(), header_merge_format)

        # 20 kun
        worksheet.write(i + 4, 27, query_taqsimlangan.filter(markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=10),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=20)

        ).distinct().count(), header_merge_format)

        # 30 kun
        worksheet.write(i + 4, 28, query_taqsimlangan.filter(markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=20),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=30)

        ).distinct().count(), header_merge_format)

        # 45 kun
        worksheet.write(i + 4, 29, query_taqsimlangan.filter(markaz__region=regions[j]).filter(
            # time_departure_center__isnull=False,
            # accept_center_info__arrived_date__lte=F('time_arrival_center') + timedelta(days=45),
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=30),

        ).distinct().count(), header_merge_format)

        j+=1
        i+=1


        ### JAMI ####



    worksheet.merge_range(18,1,18,2, 'Жами:',header_merge_format_bold)
    # jami joylashtirilganla
    worksheet.write(18, 3, base_query.count(), header_merge_format)

    # shundan
    # boshqa davlatdan olib kelingan
    worksheet.write(18, 4, base_query.filter(
        accept_center_info__determined_location='5').distinct().count(), header_merge_format)
    worksheet.write(18, 5, base_query.filter(
        juvenile__juvenile__passport_type='5').distinct().count(), header_merge_format)

    # kimlar tomonidan olib kelingan
    worksheet.write(18, 6, base_query.filter(
        accept_center_info__inspector__inspector_type='1').distinct().count(), header_merge_format)
    worksheet.write(18, 7, base_query.filter(
        accept_center_info__inspector__inspector_type='2').distinct().count(), header_merge_format)
    worksheet.write(18, 8, base_query.filter(
        accept_center_info__inspector__inspector_type='3').distinct().count(), header_merge_format)
    worksheet.write(18, 9, base_query.filter(
        Q(accept_center_info__inspector__inspector_type='4')|Q(accept_center_info__inspector__inspector_type=None)).distinct().count(), header_merge_format)

    # talim turi
    worksheet.write(18, 10, base_query.filter(
        juvenile__educationinfojuvenile__school_type='1').distinct().count(), header_merge_format)
    worksheet.write(18, 11, base_query.filter(
        juvenile__educationinfojuvenile__school_type='2').distinct().count(), header_merge_format)
    worksheet.write(18, 12, base_query.filter(
        juvenile__educationinfojuvenile__school_type='3').distinct().count(), header_merge_format)
    worksheet.write(18, 13, base_query.filter(
        juvenile__educationinfojuvenile__school_type='4').distinct().count(), header_merge_format)
    worksheet.write(18, 14, base_query.filter(
        juvenile__educationinfojuvenile__school_type='5').distinct().count(), header_merge_format)
    worksheet.write(18, 15, base_query.filter(
        juvenile__educationinfojuvenile__school_type='6').distinct().count(), header_merge_format)
    worksheet.write(18, 16, base_query.filter(
        juvenile__educationinfojuvenile__school_type='7').distinct().count(), header_merge_format)
    worksheet.write(18, 17, base_query.filter(
        juvenile__educationinfojuvenile__school_type='8').distinct().count(), header_merge_format)
    worksheet.write(18, 18, base_query.filter(
        Q(juvenile__educationinfojuvenile__school_type='9')|Q(juvenile__juvenile__passport_type=5)).distinct().count(), header_merge_format)
    worksheet.write(18, 19, base_query.filter(
        juvenile__educationinfojuvenile__school_type='10').distinct().count(), header_merge_format)

    # yoshi
    # 3 yosh 6 yosh

    today = date.today()
    end_date = today - timedelta(days=3 * 365)
    start_date = today - timedelta(days=6 * 365)
    worksheet.write(18, 20, base_query.filter(
        juvenile__juvenile__birth_date__gte=start_date,
        juvenile__juvenile__birth_date__lte=end_date).distinct().count(), header_merge_format)

    # 7 yosh 13 yosh
    today = date.today()
    end_date = today - timedelta(days=6 * 365)
    start_date = today - timedelta(days=13 * 365)
    worksheet.write(18, 21, base_query.filter(
        juvenile__juvenile__birth_date__gte=start_date,
        juvenile__juvenile__birth_date__lt=end_date).distinct().count(), header_merge_format)

    # 14 yosh 18 yosh
    today = date.today()
    end_date = today - timedelta(days=13 * 365)
    start_date = today - timedelta(days=20 * 365)
    worksheet.write(18, 22, base_query.filter(
        juvenile__juvenile__birth_date__gte=start_date,
        juvenile__juvenile__birth_date__lt=end_date).distinct().count(), header_merge_format)

    # jinsi
    worksheet.write(18, 23,
                    base_query.filter(juvenile__juvenile__gender='M').distinct().count(),
                    header_merge_format)
    worksheet.write(18, 24,
                    base_query.filter(juvenile__juvenile__gender='F').distinct().count(),
                    header_merge_format)

    # saqlangan muddatlar
    # 2 kungacha
    worksheet.write(18, 25, query_taqsimlangan.filter(
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=2)
    ).distinct().count(), header_merge_format)

    # 10 kun
    worksheet.write(18, 26, query_taqsimlangan.filter(
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=2),
        accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=10)

    ).distinct().count(), header_merge_format)

    # 20 kun
    worksheet.write(18, 27, query_taqsimlangan.filter(
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=10),
        accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=20)

    ).distinct().count(), header_merge_format)

    # 30 kun
    worksheet.write(18, 28, query_taqsimlangan.filter(
        # time_departure_center__isnull=False,
        accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=20),
        accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=30)

    ).distinct().count(), header_merge_format)

    # 45 kun
    worksheet.write(18, 29, query_taqsimlangan.filter(
        # time_departure_center__isnull=False,
        # accept_center_info__arrived_date__lte=F('time_arrival_center') + timedelta(days=45),
        accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=30),

    ).distinct().count(), header_merge_format)
    workbook.close()
    return file_path


def apparat_to_excel_7_2(request):
    date_from = request.GET.get('date_from')

    date_to = request.GET.get('date_to')
    time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
    date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

    last_year = int(format(datetime.now(), '%Y'))

    if date_from and date_to:
        base_query = models.Juvenile_Markaz.objects.filter(
        status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], accept_center_info__arrived_date__range=[date_from,date_to])
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13'],accept_center_info__arrived_date__range=[date_from,date_to])

    else:
        base_query = models.Juvenile_Markaz.objects.filter(
            status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'],accept_center_info__arrived_date__year=last_year)
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13'],accept_center_info__arrived_date__year=last_year)

    local_time = datetime.now(pytz.timezone('Asia/Tashkent'))
    download_time = format(local_time, '%Y-%m-%d-%H-%M-%S')

    workbook = xlsxwriter.Workbook(f"media/apparat_statistics_7_2___{download_time}.xlsx")
    worksheet = workbook.add_worksheet("Statistics")
    # domain_name = 'http://127.0.0.1:8000/'
    domain_name = env('DOMAIN_NAME')

    file_path = f'{domain_name}/{workbook.filename}'

    header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        # 'fg_color': '#F0F4FF'
    })
    header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        'fg_color': '#F0F4FF'
    })

    header_merge_format.set_border_color("#1d588b")

    header_merge_format_bold.set_border_color("#1d588b")
    # wrap_format_horizontal = workbook.add_format({'text_wrap': True,
    #                                    'bold': 1,
    #                                    'border': 1,
    #                                    'align': 'center',
    #                                    'valign': 'vcenter',
    #                                    })

    vertical_header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14
        # 'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14,
        'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format.set_rotation(90)
    vertical_header_merge_format.set_border_color("#1d588b")
    vertical_header_merge_format_bold.set_rotation(90)
    vertical_header_merge_format_bold.set_border_color("#1d588b")

    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    merge_format.set_border_color("#1d588b")

    file_name_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
    })

    bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'
    })
    bold.set_rotation(90)
    bold.set_border_color("#1d588b")

    worksheet.set_column(0,0, 1)
    worksheet.set_column(1, 1, 20)
    worksheet.set_column(2,2,30)
    worksheet.set_column(3, 69, 20)
    # worksheet.set_column(4, 5, 30)
    # worksheet.set_column(6, 32, 12)
    # worksheet.set_column(33, 33, 12)
    # worksheet.set_column(34, 69, 8)
    # worksheet.set_column(10, 16, 40)

    worksheet.merge_range(2, 1, 3, 1, 'Т/Р', header_merge_format_bold)
    worksheet.merge_range(2, 2, 3, 2, headers[1], header_merge_format_bold)
    # worksheet.merge_range(2, 2, 3, 2, headers_2[0], header_merge_format_bold)
    worksheet.merge_range(2, 3, 3, 3, "Жами олиб келинганлар", header_merge_format_bold)

    worksheet.merge_range(2, 4, 2 ,16, "Олиб келинганлар кимга топширилган ", header_merge_format_bold)
    worksheet.write(3,4, "Бошқа марказга юборилган",header_merge_format_bold)
    worksheet.write(3,5, "Ота-онаси ёки яқин қариндошлари",header_merge_format)
    worksheet.write(3,6, "РЎТМ (ўғил)",header_merge_format)
    worksheet.write(3,7, "РЎТМ (қиз)",header_merge_format)
    worksheet.write(3,8, "ИТМ",header_merge_format)
    worksheet.write(3,9, "Меҳри-бонлик уйлари",header_merge_format)
    worksheet.write(3,10, "'SOS' болалар шаҳарчаси",header_merge_format)
    worksheet.write(3,11, "Оилавий болалар уйи",header_merge_format)
    worksheet.write(3,12, "Потранат",header_merge_format)
    worksheet.write(3,13, "Фарзандлик",header_merge_format)
    worksheet.write(3,14, "Васий ва ҳомий",header_merge_format)
    worksheet.write(3,15, "ССМга юборилган",header_merge_format)
    worksheet.write(3,16, "Бошқа давлатга юборилган",header_merge_format)

    worksheet.merge_range(2, 17, 3 ,17, "Ҳозирда Марказларда сақланётган болалар сони ", header_merge_format_bold)

    worksheet.merge_range(2, 18, 2 ,19, "Жинси", header_merge_format_bold)
    worksheet.write(3,18, "Ўғил бола",header_merge_format)
    worksheet.write(3,19, "Қиз бола",header_merge_format)





    regions = Region.objects.all()
    i = 0
    j = 0
    while j < regions.count():
        worksheet.write(i + 4, 1,  j + 1, header_merge_format)
        worksheet.write(i + 4, 2,  regions[j].name, header_merge_format)

        # jami olib kelinganlar
        worksheet.write(i + 4, 3, base_query.filter(markaz__region = regions[j]).count(),header_merge_format)
                        # models.Juvenile_Markaz.objects.filter(juvenile__educationinfojuvenile__isnull=False,juvenile__addressinfojuvenile__isnull=False,
                        #                     juvenile__juvenile__isnull=False,juvenile__parentinfojuvenile__isnull=False).
                        #                     filter(markaz__region = regions[j]).distinct().count(), header_merge_format)
        # kimlarga topshirilgan
        #boshqa markazga yuborilgan
        worksheet.write(i+4,4, query_taqsimlangan.filter(markaz__region=regions[j],status='8').distinct().count(),header_merge_format)

        # ota-ona yoki ornini bosuvchi
        worksheet.write(i + 4, 5,
                        query_taqsimlangan.filter(markaz__region=regions[j]).filter(
                            Q(distributed_info__distribution_type='1') | Q(
                                distributed_info__distribution_type='8')).distinct().count(), header_merge_format)

        # rotm ogil bola
        worksheet.write(i + 4, 6, query_taqsimlangan.filter(
            markaz__region=regions[j], distributed_info__rotm_type='2').distinct().count(),
                        header_merge_format)
        # rotm qiz  bola
        worksheet.write(i + 4, 7, query_taqsimlangan.filter(
            markaz__region=regions[j], distributed_info__rotm_type='1').distinct().count(),
                        header_merge_format)

        # itm
        worksheet.write(i + 4, 8, query_taqsimlangan.filter(
            markaz__region=regions[j],distributed_info__distribution_type='3').distinct().count(), header_merge_format)


        # mehribonlik uyi
        worksheet.write(i + 4, 9, query_taqsimlangan.filter(
           markaz__region=regions[j],distributed_info__type_guardianship='5').distinct().count(), header_merge_format)



        # sos bolalar
        worksheet.write(i + 4, 10, query_taqsimlangan.filter(
           markaz__region=regions[j],distributed_info__type_guardianship='7').distinct().count(), header_merge_format)


        # oilaviy bolalar uyi
        worksheet.write(i + 4, 11, query_taqsimlangan.filter(
            markaz__region=regions[j],distributed_info__type_guardianship='6').distinct().count(), header_merge_format)


        # patronat
        worksheet.write(i + 4, 12, query_taqsimlangan.filter(
            markaz__region=regions[j],distributed_info__type_guardianship='3').distinct().count(), header_merge_format)


        # farzandlik
        worksheet.write(i + 4, 13, query_taqsimlangan.filter(
            markaz__region=regions[j],distributed_info__type_guardianship='4').distinct().count(), header_merge_format)


        # vasiy homiy
        worksheet.write(i + 4, 14,
                        query_taqsimlangan.filter(markaz__region=regions[j]).filter(
                            Q(distributed_info__type_guardianship='1') | Q(
                                distributed_info__type_guardianship='2')).exclude(distributed_info__distribution_type='1').distinct().count(), header_merge_format)

        # sogliqni saqlash
        worksheet.write(i + 4, 15, query_taqsimlangan.filter(
            markaz__region=regions[j],distributed_info__distribution_type='5').distinct().count(), header_merge_format)


        # boshqa davlatga yuborish
        worksheet.write(i + 4, 16, query_taqsimlangan.filter(
            markaz__region=regions[j],distributed_info__distribution_type='7').distinct().count(), header_merge_format)


        #hozirda markazda saqlanayotgan
        if date_from and date_to:
            query = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],accept_center_info__arrived_date__range=[date_from,date_to],markaz__region=regions[j])
        else:
            query = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],markaz__region=regions[j],accept_center_info__arrived_date__year=last_year)

        worksheet.write(i+4, 17,query.distinct().count(),header_merge_format)
        worksheet.write(i+4, 18,query.filter(juvenile__juvenile__gender='M').distinct().count(),header_merge_format)
        worksheet.write(i+4, 19,query.filter(juvenile__juvenile__gender='F').distinct().count(),header_merge_format)

        j += 1
        i += 1

        #JAMI

        # jami olib kelinganlar
    worksheet.write(18, 3, base_query.count(), header_merge_format)
    # kimlarga topshirilgan
    #boshqa markazga yuborilgan
    worksheet.write(18,4, query_taqsimlangan.filter(status='8').distinct().count(),header_merge_format)

    # ota-ona yoki ornini bosuvchi
    worksheet.write(18, 5,
                    query_taqsimlangan.filter(
                        Q(distributed_info__distribution_type='1') | Q(
                            distributed_info__distribution_type='8')).distinct().count(), header_merge_format)

    # rotm ogil bola
    worksheet.write(18, 6, query_taqsimlangan.filter(
        distributed_info__rotm_type='2').distinct().count(),
                    header_merge_format)
    # rotm qiz  bola
    worksheet.write(18, 7, query_taqsimlangan.filter(
        distributed_info__rotm_type='1').distinct().count(),
                    header_merge_format)

    # itm
    worksheet.write(18, 8, query_taqsimlangan.filter(
        distributed_info__distribution_type='3').distinct().count(), header_merge_format)


    # mehribonlik uyi
    worksheet.write(18, 9, query_taqsimlangan.filter(
       distributed_info__type_guardianship='5').distinct().count(), header_merge_format)



    # sos bolalar
    worksheet.write(18, 10, query_taqsimlangan.filter(
       distributed_info__type_guardianship='7').distinct().count(), header_merge_format)


    # oilaviy bolalar uyi
    worksheet.write(18, 11, query_taqsimlangan.filter(
        distributed_info__type_guardianship='6').distinct().count(), header_merge_format)


    # patronat
    worksheet.write(18, 12, query_taqsimlangan.filter(
        distributed_info__type_guardianship='3').distinct().count(), header_merge_format)


    # farzandlik
    worksheet.write(18, 13, query_taqsimlangan.filter(
        distributed_info__type_guardianship='4').distinct().count(), header_merge_format)


    # vasiy homiy
    worksheet.write(18, 14,
                    query_taqsimlangan.filter(
                        Q(distributed_info__type_guardianship='1') | Q(
                            distributed_info__type_guardianship='2')).exclude(distributed_info__distribution_type='1').distinct().count(), header_merge_format)

    # sogliqni saqlash
    worksheet.write(18, 15, query_taqsimlangan.filter(
        distributed_info__distribution_type='5').distinct().count(), header_merge_format)


    # boshqa davlatga yuborish
    worksheet.write(18, 16, query_taqsimlangan.filter(
        distributed_info__distribution_type='7').distinct().count(), header_merge_format)


    #hozirda markazda saqlanayotgan
    if date_from and date_to:
        query = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],accept_center_info__arrived_date__range=[date_from,date_to])
    else:
        query = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],accept_center_info__arrived_date__year=last_year)

    worksheet.write(18, 17,query.distinct().count(),header_merge_format)
    worksheet.write(18, 18,query.filter(juvenile__juvenile__gender='M').distinct().count(),header_merge_format)
    worksheet.write(18, 19,query.filter(juvenile__juvenile__gender='F').distinct().count(),header_merge_format)
    worksheet.merge_range(18, 1, 18, 2, 'Жами:', header_merge_format_bold)


    workbook.close()
    return file_path


def apparat_to_excel_7_3(request):
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
    date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')

    last_year = int(format(datetime.now(), '%Y'))

    if date_from and date_to:
        base_query = models.Juvenile_Markaz.objects.filter(
        status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], accept_center_info__arrived_date__range=[date_from,date_to])
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13'],accept_center_info__arrived_date__range=[date_from,date_to])

    else:
        base_query = models.Juvenile_Markaz.objects.filter(
            status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'],accept_center_info__arrived_date__year=last_year)
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9','11', '12', '13'],accept_center_info__arrived_date__year=last_year)

    local_time = datetime.now(pytz.timezone('Asia/Tashkent'))
    download_time = format(local_time, '%Y-%m-%d-%H-%M-%S')

    workbook = xlsxwriter.Workbook(f"media/apparat_statistics_7_3___{download_time}.xlsx")
    worksheet = workbook.add_worksheet("Statistics")
    # domain_name = 'http://127.0.0.1:8000/'
    domain_name = env('DOMAIN_NAME')

    file_path = f'{domain_name}/{workbook.filename}'

    header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        # 'fg_color': '#F0F4FF'
    })
    header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        'fg_color': '#F0F4FF'
    })

    header_merge_format.set_border_color("#1d588b")

    header_merge_format_bold.set_border_color("#1d588b")
    # wrap_format_horizontal = workbook.add_format({'text_wrap': True,
    #                                    'bold': 1,
    #                                    'border': 1,
    #                                    'align': 'center',
    #                                    'valign': 'vcenter',
    #                                    })

    vertical_header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14
        # 'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14,
        'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format.set_rotation(90)
    vertical_header_merge_format.set_border_color("#1d588b")
    vertical_header_merge_format_bold.set_rotation(90)
    vertical_header_merge_format_bold.set_border_color("#1d588b")

    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    merge_format.set_border_color("#1d588b")

    file_name_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
    })

    bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'
    })
    bold.set_rotation(90)
    bold.set_border_color("#1d588b")

    worksheet.set_column(0,0, 1)
    worksheet.set_column(1, 1, 20)
    worksheet.set_column(2,2,30)
    worksheet.set_column(3, 69, 20)
    # worksheet.set_column(4, 5, 30)
    # worksheet.set_column(6, 32, 12)
    # worksheet.set_column(33, 33, 12)
    # worksheet.set_column(34, 69, 8)
    # worksheet.set_column(10, 16, 40)

    worksheet.merge_range(2, 1, 3, 1, 'Т/Р', header_merge_format_bold)
    worksheet.merge_range(2, 2, 3, 2, headers[1], header_merge_format_bold)
    # worksheet.merge_range(2, 2, 3, 2, headers_2[0], header_merge_format_bold)
    worksheet.merge_range(2, 3, 3, 3, "Жами масъулларга топширилган  вояга етмаганлар сони", header_merge_format_bold)
    worksheet.merge_range(2, 4, 3, 4, 'Хар ойда, Мониторинг қилинганлари сони ', header_merge_format_bold)
    worksheet.merge_range(2, 5, 3, 5, 'Фоизи ', header_merge_format_bold)
    worksheet.merge_range(2, 6, 3, 6, 'МЖтКнинг 47-моддасига асосан кўрилган чоралар сони ', header_merge_format_bold)
    worksheet.merge_range(2, 7, 3, 7, 'Психологлар томонидан ота-оналарга ўтказилган тренинглар сони ', header_merge_format_bold)
    worksheet.merge_range(2, 8, 3, 8, 'Мониторинг жараёнида ота-онасидан марказга қайтарилганлар  ', header_merge_format_bold)
    worksheet.merge_range(2, 9, 3, 9, 'Марказ томонидан ИТМга жойлаштирилганлар  ', header_merge_format_bold)
    worksheet.merge_range(2, 10, 3, 10, 'ИТМдан қочганлар ', header_merge_format_bold)
    worksheet.merge_range(2, 11, 3, 11, 'ИТМни тугатганлар ', header_merge_format_bold)

    worksheet.merge_range(2,12, 2,15,'Ихтисослаштирилган таълим муассасасини тугатгандан сўнг бандлиги таъминланганлар',header_merge_format_bold)
    worksheet.write(3,12, 'Олий таълим муассасасига кирганлар',header_merge_format_bold)
    worksheet.write(3,13, 'Касб-ҳунарга ўқитилганлар',header_merge_format_bold)
    worksheet.write(3,14, 'Муддатли ҳарбий хизматга юборилганлдар',header_merge_format_bold)
    worksheet.write(3,15, 'Меҳнат органлари томонидан ишга жойлаштирилганлар',header_merge_format_bold)

    worksheet.merge_range(2,16, 3,16,'Бандлиги таъминланмаган',header_merge_format_bold)







    regions = Region.objects.all()
    i = 0
    j = 0
    while j < regions.count():
        worksheet.write(i + 4, 1,  j + 1, header_merge_format)
        worksheet.write(i + 4, 2,  regions[j].name, header_merge_format)

        # Жами масъулларга топширилган  вояга етмаганлар сони
        worksheet.write(i + 4, 3, query_taqsimlangan.filter(markaz__region=regions[j]).count(), header_merge_format_bold)

        #Хар ойда, Мониторинг қилинганлари сони
        worksheet.write(i + 4, 4, query_taqsimlangan.filter(markaz__region=regions[j]).filter(monitoring_info__isnull=False).distinct().count(), header_merge_format)

        #Фоизи
        if query_taqsimlangan.filter(markaz__region=regions[j]).count() == 0:
            result = 0
        else:
            result = 100*(query_taqsimlangan.filter(markaz__region=regions[j]).filter(monitoring_info__isnull=False).distinct().count()/query_taqsimlangan.filter(markaz__region=regions[j]).distinct().count())
        print('RESULT',round(result, 1))
        worksheet.write(i + 4, 5, round(result, 1), header_merge_format_bold)

        #МЖтКнинг 47-моддасига асосан кўрилган чоралар сони
        worksheet.write(i + 4, 6, query_taqsimlangan.filter(markaz__region=regions[j]).filter(monitoring_info__isnull=False,monitoring_info__is_action_been_taken=True).distinct().count(), header_merge_format)

        #Психологлар томонидан ота-оналарга ўтказилган тренинглар сони
        worksheet.write(i+4,7,query_taqsimlangan.filter(markaz__region=regions[j],distributed_info__isnull=False).exclude(distributed_info__psyhology_condition='').distinct().count(),header_merge_format)

        #Мониторинг жараёнида ота-онасидан марказга қайтарилганлар
        worksheet.write(i+4,8,query_taqsimlangan.filter(markaz__region=regions[j],monitoring_info__monitoring_status='3').distinct().count(),header_merge_format)

        #Марказ томонидан ИТМга жойлаштирилганлар
        worksheet.write(i+4,9,query_taqsimlangan.filter(markaz__region=regions[j],distributed_info__distribution_type='3').distinct().count(),header_merge_format)

        #ИТМдан қочганлар
        worksheet.write(i+4,10,query_taqsimlangan.filter(markaz__region=regions[j],status='12').distinct().count(),header_merge_format)

        #ИТМни тугатганлар
        worksheet.write(i+4,11,query_taqsimlangan.filter(markaz__region=regions[j],monitoring_info__monitoring_status='2').distinct().count(),header_merge_format)


        #Ихтисослаштирилган таълим муассасасини тугатгандан сўнг бандлиги таъминланганлар
        # worksheet.write(i+4,12,'QQQ',header_merge_format)
        worksheet.write(i+4,12,query_taqsimlangan.filter(markaz__region=regions[j]).filter(employment_info__employment_education_type='1',employment_info__is_accepted_to_school=True).distinct().count(),header_merge_format)
        worksheet.write(i+4,13,query_taqsimlangan.filter(markaz__region=regions[j]).filter(employment_info__employment_education_type='2',employment_info__is_accepted_to_school=True).distinct().count(),header_merge_format)
        worksheet.write(i+4,14,query_taqsimlangan.filter(markaz__region=regions[j]).filter(employment_info__is_military=True).distinct().count(),header_merge_format)
        worksheet.write(i+4,15,0,header_merge_format)
        worksheet.write(i+4,16,query_taqsimlangan.filter(markaz__region=regions[j]).filter(employment_info__isnull=False,employment_info__employment_file = '').distinct().count(),header_merge_format)




        j += 1
        i += 1

        #JAMI
    worksheet.merge_range(18, 1, 18, 2, 'Жами:', header_merge_format_bold)

    # Жами масъулларга топширилган  вояга етмаганлар сони
    worksheet.write(18, 3, query_taqsimlangan.count(), header_merge_format_bold)

    # Хар ойда, Мониторинг қилинганлари сони
    worksheet.write(18, 4,
                    query_taqsimlangan.filter(monitoring_info__isnull=False).count(),
                    header_merge_format)

    # Фоизи
    if query_taqsimlangan.count() == 0:
        result = 0
    else:
        result = 100*(query_taqsimlangan.filter(monitoring_info__isnull=False).count() / query_taqsimlangan.count())

    print('RESULT', round(result, 1))
    worksheet.write(18, 5, round(result, 1), header_merge_format_bold)

    # МЖтКнинг 47-моддасига асосан кўрилган чоралар сони
    worksheet.write(18, 6, query_taqsimlangan.filter(monitoring_info__isnull=False,
                                                     monitoring_info__is_action_been_taken=True).distinct().count(),
                                                    header_merge_format)

    # Психологлар томонидан ота-оналарга ўтказилган тренинглар сони
    worksheet.write(18, 7, query_taqsimlangan.filter(distributed_info__isnull=False,
                                                        distributed_info__psyhology_condition__isnull=False).distinct().count(),
                    header_merge_format)

    # Мониторинг жараёнида ота-онасидан марказга қайтарилганлар
    worksheet.write(18, 8, query_taqsimlangan.filter(
                                                        monitoring_info__monitoring_status='3').distinct().count(),
                    header_merge_format)

    # Марказ томонидан ИТМга жойлаштирилганлар
    worksheet.write(18, 9, query_taqsimlangan.filter(
                                                        distributed_info__distribution_type='3').distinct().count(),
                    header_merge_format)

    # ИТМдан қочганлар
    worksheet.write(18, 10, query_taqsimlangan.filter(status='12').distinct().count(),
                    header_merge_format)

    # ИТМни тугатганлар
    worksheet.write(18, 11, query_taqsimlangan.filter(
                                                         monitoring_info__monitoring_status='2').distinct().count(),
                    header_merge_format)

    # Ихтисослаштирилган таълим муассасасини тугатгандан сўнг бандлиги таъминланганлар
    # worksheet.write(i+4,12,'QQQ',header_merge_format)
    worksheet.write(18, 12, query_taqsimlangan.filter(
        employment_info__employment_education_type='1', employment_info__is_accepted_to_school=True).distinct().count(),
                    header_merge_format)
    worksheet.write(18, 13, query_taqsimlangan.filter(
        employment_info__employment_education_type='2', employment_info__is_accepted_to_school=True).distinct().count(),
                    header_merge_format)
    worksheet.write(18, 14, query_taqsimlangan.filter(
        employment_info__is_military=True).distinct().count(), header_merge_format)
    worksheet.write(18, 15, 0, header_merge_format)
    worksheet.write(18, 16, query_taqsimlangan.filter(
        employment_info__employment_file='').distinct().count(), header_merge_format)

    #     # jami olib kelinganlar
    # worksheet.write(18, 3, models.Juvenile_Markaz.objects.filter(juvenile__educationinfojuvenile__isnull=False,juvenile__addressinfojuvenile__isnull=False,
    #                                     juvenile__juvenile__isnull=False,juvenile__parentinfojuvenile__isnull=False).
    #                                     distinct().count(), header_merge_format)
    # # kimlarga topshirilgan
    # #boshqa markazga yuborilgan
    # worksheet.write(18,4, query_taqsimlangan.filter(status='8').count(),header_merge_format)
    #
    # # ota-ona yoki ornini bosuvchi
    # worksheet.write(18, 5,
    #                 query_taqsimlangan.filter(
    #                     Q(distributed_info__distribution_type='1') | Q(
    #                         distributed_info__distribution_type='8')).count(), header_merge_format)
    #
    # # rotm ogil bola
    # worksheet.write(18, 6, query_taqsimlangan.filter(
    #     distributed_info__rotm_type='2').count(),
    #                 header_merge_format)
    # # rotm qiz  bola
    # worksheet.write(18, 7, query_taqsimlangan.filter(
    #     distributed_info__rotm_type='1').count(),
    #                 header_merge_format)
    #
    # # itm
    # worksheet.write(18, 8, query_taqsimlangan.filter(
    #     distributed_info__distribution_type='3').count(), header_merge_format)
    #
    #
    # # mehribonlik uyi
    # worksheet.write(18, 9, query_taqsimlangan.filter(
    #    distributed_info__type_guardianship='5').count(), header_merge_format)
    #
    #
    #
    # # sos bolalar
    # worksheet.write(18, 10, query_taqsimlangan.filter(
    #    distributed_info__type_guardianship='7').count(), header_merge_format)
    #
    #
    # # oilaviy bolalar uyi
    # worksheet.write(18, 11, query_taqsimlangan.filter(
    #     distributed_info__type_guardianship='6').count(), header_merge_format)
    #
    #
    # # patronat
    # worksheet.write(18, 12, query_taqsimlangan.filter(
    #     distributed_info__type_guardianship='3').count(), header_merge_format)
    #
    #
    # # farzandlik
    # worksheet.write(18, 13, query_taqsimlangan.filter(
    #     distributed_info__type_guardianship='4').count(), header_merge_format)
    #
    #
    # # vasiy homiy
    # worksheet.write(18, 14,
    #                 query_taqsimlangan.filter(
    #                     Q(distributed_info__type_guardianship='1') | Q(
    #                         distributed_info__type_guardianship='2')).count(), header_merge_format)
    #
    # # sogliqni saqlash
    # worksheet.write(18, 15, query_taqsimlangan.filter(
    #     distributed_info__distribution_type='5').count(), header_merge_format)
    #
    #
    # # boshqa davlatga yuborish
    # worksheet.write(18, 16, query_taqsimlangan.filter(
    #     distributed_info__distribution_type='7').count(), header_merge_format)
    #
    #
    # #hozirda markazda saqlanayotgan
    # if date_from and date_to:
    #     query = models.Juvenile_Markaz.objects.filter(status='2',accept_center_info__arrived_date__range=[date_from,date_to])
    # else:
    #     query = models.Juvenile_Markaz.objects.filter(status='2')
    #
    # worksheet.write(18, 17,query.count(),header_merge_format)
    # worksheet.write(18, 18,query.filter(juvenile__juvenile__gender='M').count(),header_merge_format)
    # worksheet.write(18, 19,query.filter(juvenile__juvenile__gender='F').count(),header_merge_format)
    # worksheet.merge_range(18, 1, 18, 2, 'Жами:', header_merge_format_bold)


    workbook.close()
    return file_path






def center_to_excel_9(request):


    local_time = datetime.now(pytz.timezone('Asia/Tashkent'))
    download_time = format(local_time, '%Y-%m-%d-%H-%M-%S')
    markaz_id = request.GET.get('markaz_id')

    if markaz_id:
        markaz = Markaz.objects.get(id=markaz_id)
    else:
        markaz = request.user.markaz
    workbook = xlsxwriter.Workbook(f"media/markaz_statistics_9__{download_time}.xlsx")
    worksheet = workbook.add_worksheet("Statistics")
    # domain_name = 'http://127.0.0.1:8000/'
    domain_name = env('DOMAIN_NAME')

    file_path = f'{domain_name}/{workbook.filename}'

    header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size':14
        # 'fg_color': '#F0F4FF'
    })
    header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size':14
        # 'fg_color': '#F0F4FF'
    })

    header_merge_format.set_border_color("#1d588b")
    header_merge_format_bold.set_border_color("#1d588b")
    # wrap_format_horizontal = workbook.add_format({'text_wrap': True,
    #                                    'bold': 1,
    #                                    'border': 1,
    #                                    'align': 'center',
    #                                    'valign': 'vcenter',
    #                                    })

    vertical_header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size':14
        # 'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size':14
        # 'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format.set_rotation(90)
    vertical_header_merge_format.set_border_color("#1d588b")
    vertical_header_merge_format_bold.set_rotation(90)
    vertical_header_merge_format_bold.set_border_color("#1d588b")

    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    merge_format.set_border_color("#1d588b")

    file_name_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
    })

    bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'
    })
    bold.set_rotation(90)
    bold.set_border_color("#1d588b")

    worksheet.set_column(0, 2, 1)
    # worksheet.set_column(2,2,20)
    worksheet.set_column(2,3,15)
    worksheet.set_column(4,5,15)
    worksheet.set_column(5, 32, 8)
    worksheet.set_column(33, 33, 12)
    worksheet.set_column(34, 69, 8)
    # worksheet.set_column(10, 16, 40)



    # worksheet.merge_range(3, 0, 4, 0, headers[0], header_merge_format_bold)
    # worksheet.merge_range(3, 1, 4, 1, headers[0], header_merge_format_bold)
    worksheet.merge_range(3, 2, 4, 2, headers[2], header_merge_format_bold)
    worksheet.merge_range(3, 3, 4, 3, headers[3], header_merge_format_bold)

    worksheet.write(3, 4,  headers[4], header_merge_format_bold)
    worksheet.write(4, 4, headers[5], vertical_header_merge_format)

    worksheet.merge_range(3, 5, 3, 9, headers[6], header_merge_format_bold)
    worksheet.write(4, 5, subheaders[headers[6]][0], vertical_header_merge_format)
    worksheet.write(4, 6, subheaders[headers[6]][1], vertical_header_merge_format)
    worksheet.write(4, 7, subheaders[headers[6]][2], vertical_header_merge_format)
    worksheet.write(4, 8, subheaders[headers[6]][3], vertical_header_merge_format)
    worksheet.write(4, 9, subheaders[headers[6]][4], vertical_header_merge_format)

    worksheet.merge_range(3, 10, 3, 14, headers[7], header_merge_format_bold)
    worksheet.write(4, 10, subheaders[headers[7]][0], vertical_header_merge_format)
    worksheet.write(4, 11,  subheaders[headers[7]][1], vertical_header_merge_format)
    worksheet.write(4, 12, subheaders[headers[7]][2], vertical_header_merge_format)
    worksheet.write(4, 13, subheaders[headers[7]][3], vertical_header_merge_format)
    worksheet.write(4, 14,  subheaders[headers[7]][4], vertical_header_merge_format)

    worksheet.merge_range(3, 15, 3, 18, headers[8], header_merge_format_bold)
    worksheet.write(4, 15, subheaders[headers[8]][0], vertical_header_merge_format)
    worksheet.write(4, 16,  subheaders[headers[8]][1], vertical_header_merge_format)
    worksheet.write(4, 17,  subheaders[headers[8]][2], vertical_header_merge_format)
    worksheet.write(4, 18,  subheaders[headers[8]][3], vertical_header_merge_format)

    worksheet.merge_range(3, 19, 3, 28, headers[9], header_merge_format_bold)
    worksheet.write(4, 19,  subheaders[headers[9]][0], vertical_header_merge_format)
    worksheet.write(4, 20,  subheaders[headers[9]][1], vertical_header_merge_format)
    worksheet.write(4, 21, subheaders[headers[9]][2], vertical_header_merge_format)
    worksheet.write(4, 22,  subheaders[headers[9]][3], vertical_header_merge_format)
    worksheet.write(4, 23,  subheaders[headers[9]][4], vertical_header_merge_format)
    worksheet.write(4, 24,  subheaders[headers[9]][5], vertical_header_merge_format)
    worksheet.write(4, 25,  subheaders[headers[9]][6], vertical_header_merge_format)
    worksheet.write(4, 26,  subheaders[headers[9]][7], vertical_header_merge_format)
    worksheet.write(4, 27,  subheaders[headers[9]][8], vertical_header_merge_format)
    worksheet.write(4, 28,  subheaders[headers[9]][9], vertical_header_merge_format)

    worksheet.merge_range(3, 29, 3, 32, headers[10], header_merge_format_bold)
    worksheet.write(4, 29,  subheaders[headers[10]][0], vertical_header_merge_format)
    worksheet.write(4, 30,  subheaders[headers[10]][1], vertical_header_merge_format)
    worksheet.write(4, 31, subheaders[headers[10]][2], vertical_header_merge_format)
    worksheet.write(4, 32,  subheaders[headers[10]][3], vertical_header_merge_format)

    worksheet.merge_range(3, 33, 4, 33, headers[11], vertical_header_merge_format_bold)

    worksheet.merge_range(3, 34, 3, 35, headers[12], header_merge_format_bold)
    worksheet.write(4, 34,  subheaders[headers[12]][0], vertical_header_merge_format)
    worksheet.write(4, 35,  subheaders[headers[12]][1], vertical_header_merge_format)

    worksheet.merge_range(3, 36, 3, 41, headers[13], header_merge_format_bold)
    worksheet.write(4, 36,  subheaders[headers[13]][0], vertical_header_merge_format)
    worksheet.write(4, 37,  subheaders[headers[13]][1], vertical_header_merge_format)
    worksheet.write(4, 38,  subheaders[headers[13]][2], vertical_header_merge_format)
    worksheet.write(4, 39,  subheaders[headers[13]][3], vertical_header_merge_format)
    worksheet.write(4, 40,  subheaders[headers[13]][4], vertical_header_merge_format)
    worksheet.write(4, 41,  subheaders[headers[13]][5], vertical_header_merge_format)


    worksheet.merge_range(3, 42, 3, 47, headers[15], header_merge_format_bold)
    worksheet.write(4, 42,  subheaders[headers[15]][0], vertical_header_merge_format)
    worksheet.write(4, 43, subheaders[headers[15]][1], vertical_header_merge_format)
    worksheet.write(4, 44, subheaders[headers[15]][2], vertical_header_merge_format)
    worksheet.write(4, 45,  subheaders[headers[15]][3], vertical_header_merge_format)
    worksheet.write(4, 46,  subheaders[headers[15]][4], vertical_header_merge_format)
    worksheet.write(4, 47, subheaders[headers[15]][5], vertical_header_merge_format)

    # worksheet.merge_range(3, 48, 3, 53, headers[15], header_merge_format_bold)
    # worksheet.write(4, 48,  subheaders[headers[15]][0], vertical_header_merge_format)
    # worksheet.write(4, 49,  subheaders[headers[15]][1], vertical_header_merge_format)
    # worksheet.write(4, 50,  subheaders[headers[15]][2], vertical_header_merge_format)
    # worksheet.write(4, 51,  subheaders[headers[15]][3], vertical_header_merge_format)
    # worksheet.write(4, 52,  subheaders[headers[15]][4], vertical_header_merge_format)
    # worksheet.write(4, 53,  subheaders[headers[15]][5], vertical_header_merge_format)


    worksheet.merge_range(3, 48, 3, 60, headers[17], header_merge_format_bold)
    worksheet.write(4, 48,  subheaders[headers[17]][0], vertical_header_merge_format)
    worksheet.write(4, 49,  subheaders[headers[17]][1], vertical_header_merge_format)
    worksheet.write(4, 50,  subheaders[headers[17]][2], vertical_header_merge_format)
    worksheet.write(4, 51,  subheaders[headers[17]][3], vertical_header_merge_format)
    worksheet.write(4, 52, subheaders[headers[17]][4], vertical_header_merge_format)
    worksheet.write(4, 53,  subheaders[headers[17]][5], vertical_header_merge_format)
    worksheet.write(4, 54,  subheaders[headers[17]][6], vertical_header_merge_format)
    worksheet.write(4, 55,  subheaders[headers[17]][7], vertical_header_merge_format)
    worksheet.write(4, 56, subheaders[headers[17]][8], vertical_header_merge_format)
    worksheet.write(4, 57, subheaders[headers[17]][9], vertical_header_merge_format)
    worksheet.write(4, 58,  subheaders[headers[17]][10], vertical_header_merge_format)
    worksheet.write(4, 59, subheaders[headers[17]][11], vertical_header_merge_format)
    worksheet.write(4, 60,  subheaders[headers[17]][12], vertical_header_merge_format)

    #Бошка давлатларда яшовчи фуқаролар фарзандлари
    worksheet.merge_range(3, 61, 3, 66, headers[14], header_merge_format_bold)
    worksheet.write(4,61,subheaders[headers[14]][0],vertical_header_merge_format)
    worksheet.write(4,62,subheaders[headers[14]][1],vertical_header_merge_format)
    worksheet.write(4,63,subheaders[headers[14]][2],vertical_header_merge_format)
    worksheet.write(4,64,subheaders[headers[14]][3],vertical_header_merge_format)
    worksheet.write(4,65,subheaders[headers[14]][4],vertical_header_merge_format)
    worksheet.write(4,66,subheaders[headers[14]][5],vertical_header_merge_format)


    # worksheet.merge_range(3, 61, 3,62, headers[16], header_merge_format_bold)
    # worksheet.write(4, 61,  subheaders[headers[16]][0], vertical_header_merge_format)
    # worksheet.write(4, 62, subheaders[headers[16]][2], vertical_header_merge_format)
    # worksheet.write(4, 63,  subheaders[headers[16]][2], vertical_header_merge_format)

    # juvenile_markaz_2024 = models.Juvenile_Markaz.objects.filter(accept_center_info__arrived_date__year=2024).exclude(status='1')
    # juvenile_markaz_2023 = models.Juvenile_Markaz.objects.filter(accept_center_info__arrived_date__year=2023).exclude(status='1')
    # juveniles_2024 = models.Juvenile.objects.filter(juvenile_markaz__in=juvenile_markaz_2024).distinct()
    # juveniles_2023 = models.Juvenile.objects.filter(juvenile_markaz__in=juvenile_markaz_2023).distinct()
    regions = Region.objects.all()

    i=0
    j=0
    print('YYT 1',markaz,markaz.id)
    print('GGH 1',base_query_2023.count())
    print('YYT 2',base_query_2023.filter(markaz = markaz).distinct().count())
    while j < 1:
        # worksheet.merge_range(i+5, 1, i+6, 1,  j+1,header_merge_format)
        # worksheet.merge_range(i+5, 1, i+6, 1,  regions[j].name,header_merge_format)
        worksheet.write(i+5, 2,  2024,header_merge_format_bold)
        worksheet.write(i+6, 2,  2023,header_merge_format)
        #Жами қабул қилинганлар сони
        worksheet.write(i+5,3, base_query_2024.filter(markaz = markaz).distinct().count(),header_merge_format )
        worksheet.write(i+6,3, base_query_2023.filter(markaz = markaz).distinct().count(),header_merge_format )

        #қиз болалар
        worksheet.write(i+5,4, base_query_2024.filter(markaz = markaz).filter(juvenile__juvenile__gender='F').distinct().count(),header_merge_format)
        worksheet.write(i+6,4, base_query_2023.filter(markaz = markaz).filter(juvenile__juvenile__gender='F').distinct().count(),header_merge_format)

        #Қабул қилинганларни сақлаш муддатлари
        # 48 soat
        worksheet.write(i+5,5, query_taqsimlangan.filter(markaz = markaz,accept_center_info__arrived_date__year=2024).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=2)
        ).distinct().count(),header_merge_format)

        worksheet.write(i+6,5, query_taqsimlangan.filter(markaz = markaz,accept_center_info__arrived_date__year=2023).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=2)
        ).distinct().count(),header_merge_format)

        #10 kun
        worksheet.write(i+5,6, query_taqsimlangan.filter(markaz = markaz,accept_center_info__arrived_date__year=2024).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=2),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=10)

        ).distinct().count(),header_merge_format)

        worksheet.write(i+6,6, query_taqsimlangan.filter(markaz = markaz,accept_center_info__arrived_date__year=2023).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=2),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=10)
        ).distinct().count(),header_merge_format)

        #20 kun
        worksheet.write(i+5,7, query_taqsimlangan.filter(markaz = markaz,accept_center_info__arrived_date__year=2024).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=10),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=20)
        ).distinct().count(),header_merge_format)

        worksheet.write(i+6,7, query_taqsimlangan.filter(markaz = markaz,accept_center_info__arrived_date__year=2023).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=2),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=10)
        ).distinct().count(),header_merge_format)

        #30 kun
        worksheet.write(i+5,8, query_taqsimlangan.filter(markaz = markaz,accept_center_info__arrived_date__year=2024).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=20),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=30)
        ).distinct().count(),header_merge_format)

        worksheet.write(i+6,8, query_taqsimlangan.filter(markaz = markaz,accept_center_info__arrived_date__year=2023).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=20),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=30)
        ).distinct().count(),header_merge_format)

        #45 kun
        worksheet.write(i+5,9, query_taqsimlangan.filter(markaz = markaz,accept_center_info__arrived_date__year=2024).filter(
            # time_departure_center__isnull=False,
            # accept_center_info__arrived_date__lte=F('time_arrival_center') + timedelta(days=45),
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=30),
        ).distinct().count(),header_merge_format)

        worksheet.write(i+6,9, query_taqsimlangan.filter(markaz = markaz,accept_center_info__arrived_date__year=2023).filter(
            # time_departure_center__isnull=False,
            # accept_center_info__arrived_date__lte=F('time_arrival_center') + timedelta(days=45),
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=30),
        ).distinct().count(),header_merge_format)

        #Олиб келинган жойлари

        #bozor
        worksheet.write(i+5,10, base_query_2024.filter(markaz = markaz).filter(accept_center_info__determined_location='1').distinct().count(),header_merge_format )
        worksheet.write(i+6,10, base_query_2023.filter(markaz = markaz).filter(accept_center_info__determined_location='1').distinct().count(),header_merge_format )

        #kocha
        worksheet.write(i+5,11, base_query_2024.filter(markaz = markaz).filter(accept_center_info__determined_location='3').distinct().count(),header_merge_format )
        worksheet.write(i+6,11, base_query_2023.filter(markaz = markaz).filter(accept_center_info__determined_location='3').distinct().count(),header_merge_format )

        #yer tola
        worksheet.write(i+5,12, base_query_2024.filter(markaz = markaz).filter(accept_center_info__determined_location='2').distinct().count(),header_merge_format )
        worksheet.write(i+6,12, base_query_2023.filter(markaz = markaz).filter(accept_center_info__determined_location='2').distinct().count(),header_merge_format )

        #boshqa joy
        worksheet.write(i+5,13, base_query_2024.filter(markaz = markaz).filter(accept_center_info__determined_location='4').distinct().count(),header_merge_format )
        worksheet.write(i+6,13, base_query_2023.filter(markaz = markaz).filter(accept_center_info__determined_location='4').distinct().count(),header_merge_format )

        #boshqa davlat
        worksheet.write(i+5,14, base_query_2024.filter(markaz = markaz).filter(accept_center_info__determined_location='5').distinct().count(),header_merge_format )
        worksheet.write(i+6,14, base_query_2023.filter(markaz = markaz).filter(accept_center_info__determined_location='5').distinct().count(),header_merge_format )

        #yoshi
        today = date.today()
        #3 yosh 6 yosh
        end_date = today - timedelta(days=3 * 365)
        start_date = today - timedelta(days=6 * 365)
        worksheet.write(i+5,15, base_query_2024.filter(markaz = markaz).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lte=end_date).distinct().count(),header_merge_format )
        worksheet.write(i+6,15, base_query_2023.filter(markaz = markaz).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lte=end_date).distinct().count(),header_merge_format )

        #7-13 yosh
        end_date = today - timedelta(days=6 * 365)
        start_date = today - timedelta(days=13 * 365)
        worksheet.write(i+5,16, base_query_2024.filter(markaz = markaz).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lt=end_date).distinct().count(),header_merge_format )
        worksheet.write(i+6,16, base_query_2023.filter(markaz = markaz).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lt=end_date).distinct().count(),header_merge_format )

        # 14-18 yosh
        end_date = today - timedelta(days=13 * 365)
        start_date = today - timedelta(days=20 * 365)
        worksheet.write(i+5,17, base_query_2024.filter(markaz = markaz).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lt=end_date).distinct().count(),header_merge_format )
        worksheet.write(i+6,17, base_query_2023.filter(markaz = markaz).filter(juvenile__juvenile__birth_date__gte=start_date,juvenile__juvenile__birth_date__lt=end_date).distinct().count(),header_merge_format )
        #yoshi nomalum
        worksheet.write(i+5,18, base_query_2024.filter(markaz = markaz).filter(juvenile__juvenile__birth_date__isnull=True).distinct().count(),header_merge_format )
        worksheet.write(i+6,18, base_query_2023.filter(markaz = markaz).filter(juvenile__juvenile__birth_date__isnull=True).distinct().count(),header_merge_format )

        #Олиб келинганлардан

        #maktabgacha talim
        worksheet.write(i+5,19, base_query_2024.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='1').distinct().count(),header_merge_format )
        worksheet.write(i+6,19, base_query_2023.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='1').distinct().count(),header_merge_format )

        worksheet.write(i+5,20, base_query_2024.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='2').distinct().count(),header_merge_format )
        worksheet.write(i+6,20, base_query_2023.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='2').distinct().count(),header_merge_format )

        worksheet.write(i+5,21, base_query_2024.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='3').distinct().count(),header_merge_format )
        worksheet.write(i+6,21, base_query_2023.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='3').distinct().count(),header_merge_format )

        worksheet.write(i+5,22, base_query_2024.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='4').distinct().count(),header_merge_format )
        worksheet.write(i+6,22, base_query_2023.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='4').distinct().count(),header_merge_format )

        worksheet.write(i+5,23, base_query_2024.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='5').distinct().count(),header_merge_format )
        worksheet.write(i+6,23, base_query_2023.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='5').distinct().count(),header_merge_format )

        worksheet.write(i+5,24, base_query_2024.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='6').distinct().count(),header_merge_format )
        worksheet.write(i+6,24, base_query_2023.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='6').distinct().count(),header_merge_format )

        worksheet.write(i+5,25, base_query_2024.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='7').distinct().count(),header_merge_format )
        worksheet.write(i+6,25, base_query_2023.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='7').distinct().count(),header_merge_format )

        worksheet.write(i+5,26, base_query_2024.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='8').distinct().count(),header_merge_format )
        worksheet.write(i+6,26, base_query_2023.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='8').distinct().count(),header_merge_format )

        worksheet.write(i+5,27, base_query_2024.filter(markaz = markaz).filter(Q(juvenile__educationinfojuvenile__school_type='9')|Q(juvenile__juvenile__passport_type=5)).distinct().count(),header_merge_format )
        worksheet.write(i+6,27, base_query_2023.filter(markaz = markaz).filter(Q(juvenile__educationinfojuvenile__school_type='9')|Q(juvenile__juvenile__passport_type=5)).distinct().count(),header_merge_format )

        worksheet.write(i+5,28, base_query_2024.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='10').distinct().count(),header_merge_format )
        worksheet.write(i+6,28, base_query_2023.filter(markaz = markaz).filter(juvenile__educationinfojuvenile__school_type='10').distinct().count(),header_merge_format )


        #oilaviy ahvoli ParentInfoJuvenile

        worksheet.write(i+5,29, base_query_2024.filter(markaz = markaz).filter(juvenile__parentinfojuvenile__marital_status='1').distinct().count(),header_merge_format )
        worksheet.write(i+6,29, base_query_2023.filter(markaz = markaz).filter(juvenile__parentinfojuvenile__marital_status='1').distinct().count(),header_merge_format )

        worksheet.write(i+5,30, base_query_2024.filter(markaz = markaz).filter(juvenile__parentinfojuvenile__marital_status='2').distinct().count(),header_merge_format )
        worksheet.write(i+6,30, base_query_2023.filter(markaz = markaz).filter(juvenile__parentinfojuvenile__marital_status='2').distinct().count(),header_merge_format )

        worksheet.write(i+5,31, base_query_2024.filter(markaz = markaz).filter(juvenile__parentinfojuvenile__marital_status='3').distinct().count(),header_merge_format )
        worksheet.write(i+6,31, base_query_2023.filter(markaz = markaz).filter(juvenile__parentinfojuvenile__marital_status='3').distinct().count(),header_merge_format )

        worksheet.write(i+5,32, base_query_2024.filter(markaz = markaz).filter(juvenile__parentinfojuvenile__marital_status='4').distinct().count(),header_merge_format )
        worksheet.write(i+6,32, base_query_2023.filter(markaz = markaz).filter(juvenile__parentinfojuvenile__marital_status='4').distinct().count(),header_merge_format )

        #profilaktik hisobda
        worksheet.write(i+5,33, base_query_2024.filter(markaz = markaz).filter(accept_center_info__prophylactic_list=True).distinct().count(),header_merge_format )
        worksheet.write(i+6,33, base_query_2023.filter(markaz = markaz).filter(accept_center_info__prophylactic_list=True).distinct().count(),header_merge_format )
        #
        # qayta joylashtirilaganlar
        two_times_2024 = base_query_2024.filter(markaz = markaz).values('juvenile','markaz').annotate(markaz_count=Count('id')).filter(markaz_count=2)
        two_times_2023 = base_query_2023.filter(markaz = markaz).values('juvenile','markaz').annotate(markaz_count=Count('id')).filter(markaz_count=2)
        two_more_times_2024 = base_query_2024.filter(markaz = markaz).values('juvenile','markaz').annotate(markaz_count=Count('id')).filter(markaz_count__gt=2)
        two_more_times_2023 = base_query_2024.filter(markaz = markaz).values('juvenile','markaz').annotate(markaz_count=Count('id')).filter(markaz_count__gt=2)

        worksheet.write(i+5,34, two_times_2024.count() ,header_merge_format )
        worksheet.write(i+6,34, two_times_2023.count(),header_merge_format )
        worksheet.write(i+5,35, two_more_times_2024.count(),header_merge_format )
        worksheet.write(i+6,35, two_more_times_2023.count(),header_merge_format )

        # #olib kelish sababi
        worksheet.write(i+5,36, base_query_2024.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='1').distinct().count(),header_merge_format )
        worksheet.write(i+6,36, base_query_2023.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='1').distinct().count(),header_merge_format )

        worksheet.write(i+5,37, base_query_2024.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='2').distinct().count(),header_merge_format )
        worksheet.write(i+6,37, base_query_2023.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='2').distinct().count(),header_merge_format )

        worksheet.write(i+5,38, base_query_2024.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='3').distinct().count(),header_merge_format )
        worksheet.write(i+6,38, base_query_2023.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='3').distinct().count(),header_merge_format )

        worksheet.write(i+5,39, base_query_2024.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='4').distinct().count(),header_merge_format )
        worksheet.write(i+6,39, base_query_2023.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='4').distinct().count(),header_merge_format )

        worksheet.write(i+5,40, base_query_2024.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='5').distinct().count(),header_merge_format )
        worksheet.write(i+6,40, base_query_2023.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='5').distinct().count(),header_merge_format )

        worksheet.write(i+5,41, base_query_2024.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='6').distinct().count(),header_merge_format )
        worksheet.write(i+6,41, base_query_2023.filter(markaz = markaz).filter(accept_center_info__sub_reason_bringing_child__parent__order='6').distinct().count(),header_merge_format )
        # worksheet.write(i+6,41, 'AAAA',header_merge_format )

        # #Бошка давлатларда яшовчи фуқаролар фарзандлари
        # worksheet.write(i+5,42, base_query_2024.filter(markaz = markaz).filter(juvenile__parentinfojuvenile__relationship__parent__is_abroad=True).distinct().count(),header_merge_format )
        # worksheet.write(i+6,42, base_query_2023.filter(markaz = markaz).filter(juvenile__parentinfojuvenile__relationship__parent__is_abroad=True).distinct().count(),header_merge_format )


        #Бошка давлатлардан олиб келинган қаровсиз қолган вояга етмаганлар
        worksheet.write(i+5,42, base_query_2024.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__name='Russia').distinct().count(),header_merge_format )
        worksheet.write(i+6,42, base_query_2023.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__name='Russia').distinct().count(),header_merge_format )
        #
        worksheet.write(i+5,43, base_query_2024.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__name='Kazakhstan').distinct().count(),header_merge_format )
        worksheet.write(i+6,43, base_query_2023.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__name='Kazakhstan').distinct().count(),header_merge_format )

        worksheet.write(i+5,44, base_query_2024.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__name='Kyrgyzstan').distinct().count(),header_merge_format )
        worksheet.write(i+6,44, base_query_2023.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__name='Kyrgyzstan').distinct().count(),header_merge_format )

        worksheet.write(i+5,45, base_query_2024.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__name='Tajikistan').distinct().count(),header_merge_format )
        worksheet.write(i+6,45, base_query_2023.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__name='Tajikistan').distinct().count(),header_merge_format )


        worksheet.write(i+5,46, base_query_2024.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__name='Turkmenistan').distinct().count(),header_merge_format )
        worksheet.write(i+6,46, base_query_2023.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__name='Turkmenistan').distinct().count(),header_merge_format )

        worksheet.write(i+5,47, base_query_2024.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__isnull=False).exclude(juvenile__juvenile__foreign_country__name__in=['Russia','Kazakhstan','Kyrgyzstan','Tajikistan','Turkmenistan',]).distinct().count(),header_merge_format )
        worksheet.write(i+6,47, base_query_2023.filter(markaz = markaz).filter(juvenile__juvenile__foreign_country__isnull=False).exclude(juvenile__juvenile__foreign_country__name__in=['Russia','Kazakhstan','Kyrgyzstan','Tajikistan','Turkmenistan',]).distinct().count(),header_merge_format )


        #kimlarga topshirilgan
        # boshqa markazga yuborilgan
        worksheet.write(i+5,48, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz) & Q(status='8') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,48, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz) & Q(status='8') ).distinct().count(),header_merge_format )

        # ota-ona yoki ornini bosuvchi
        worksheet.write(i+5,49, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz)).filter(Q(distributed_info__distribution_type='1')| Q(distributed_info__distribution_type='8')).distinct().count(),header_merge_format )
        worksheet.write(i+6,49, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz)).filter(Q(distributed_info__distribution_type='1')| Q(distributed_info__distribution_type='8')).distinct().count(),header_merge_format )

        #rotm ogil bola
        worksheet.write(i+5,50, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz) & Q(distributed_info__rotm_type='2') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,50, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz) & Q(distributed_info__rotm_type='2') ).distinct().count(),header_merge_format )
        #qiz ogil bola
        worksheet.write(i+5,51, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz) & Q(distributed_info__rotm_type='1') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,51, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz) & Q(distributed_info__rotm_type='1') ).distinct().count(),header_merge_format )

        #itm
        worksheet.write(i+5,52, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz) & Q(distributed_info__distribution_type='3') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,52, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz) & Q(distributed_info__distribution_type='3') ).distinct().count(),header_merge_format )

        #mehribonlik uyi
        worksheet.write(i+5,53, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz) & Q(distributed_info__type_guardianship='5') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,53, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz) & Q(distributed_info__type_guardianship='5') ).distinct().count(),header_merge_format )

        #sos bolalar
        worksheet.write(i+5,54, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz) & Q(distributed_info__type_guardianship='7') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,54, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz) & Q(distributed_info__type_guardianship='7') ).distinct().count(),header_merge_format )

        #oilaviy bolalar uyi
        worksheet.write(i+5,55, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz) & Q(distributed_info__type_guardianship='6') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,55, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz) & Q(distributed_info__type_guardianship='6') ).distinct().count(),header_merge_format )

        #patronat
        worksheet.write(i+5,56, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz) & Q(distributed_info__type_guardianship='3') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,56, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz) & Q(distributed_info__type_guardianship='3') ).distinct().count(),header_merge_format )

        #farzandlik
        worksheet.write(i+5,57, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz) & Q(distributed_info__type_guardianship='4') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,57, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz) & Q(distributed_info__type_guardianship='4') ).distinct().count(),header_merge_format )

        #vasiy homiy
        worksheet.write(i+5,58, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz)).filter(Q(distributed_info__type_guardianship='1') | Q(distributed_info__type_guardianship='2')).exclude(distributed_info__distribution_type='1').distinct().count(),header_merge_format )
        worksheet.write(i+6,58, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz)).filter(Q(distributed_info__type_guardianship='1') | Q(distributed_info__type_guardianship='2')).exclude(distributed_info__distribution_type='1').distinct().count(),header_merge_format )

        #sogliqni saqlash
        worksheet.write(i+5,59, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz) & Q(distributed_info__distribution_type='5') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,59, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz) & Q(distributed_info__distribution_type='5') ).distinct().count(),header_merge_format )

        #boshqa davlatga yuborish
        worksheet.write(i+5,60, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2024) & Q(markaz = markaz) & Q(distributed_info__distribution_type='7') ).distinct().count(),header_merge_format )
        worksheet.write(i+6,60, query_taqsimlangan.filter(Q(accept_center_info__arrived_date__year = 2023) & Q(markaz = markaz) & Q(distributed_info__distribution_type='7') ).distinct().count(),header_merge_format )

        #Бошка давлатларда яшовчи фуқаролар фарзандлари

        worksheet.write(i + 5, 61, 0, header_merge_format)
        worksheet.write(i + 6, 61, 0, header_merge_format)

        worksheet.write(i + 5, 62, 0, header_merge_format)
        worksheet.write(i + 6, 62, 0, header_merge_format)

        worksheet.write(i + 5, 63, 0, header_merge_format)
        worksheet.write(i + 6, 63, 0, header_merge_format)

        worksheet.write(i + 5, 64, 0, header_merge_format)
        worksheet.write(i + 6, 64, 0, header_merge_format)

        worksheet.write(i + 5, 65, 0, header_merge_format)
        worksheet.write(i + 6, 65, 0, header_merge_format)

        worksheet.write(i + 5, 66, 0, header_merge_format)
        worksheet.write(i + 6, 66, 0, header_merge_format)


        j+=1
        i+=2

    workbook.close()
    return file_path


def center_to_excel_8_1(request):
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
    date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
    markaz_id = request.GET.get('markaz_id')
    last_year = int(format(datetime.now(), '%Y'))
    print('YYY',request.user)
    if markaz_id:
        markaz = Markaz.objects.get(id=markaz_id)
    else:
        markaz = request.user.markaz


    if date_from and date_to:
        base_query = models.Juvenile_Markaz.objects.filter(
        status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], accept_center_info__arrived_date__range=[date_from,date_to])
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13'],accept_center_info__arrived_date__range=[date_from,date_to])

    else:
        base_query = models.Juvenile_Markaz.objects.filter(
            status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], accept_center_info__arrived_date__year=last_year)
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13'],accept_center_info__arrived_date__year=last_year)

    local_time = datetime.now(pytz.timezone('Asia/Tashkent'))
    download_time = format(local_time, '%Y-%m-%d-%H-%M-%S')

    workbook = xlsxwriter.Workbook(f"media/center_statistics_8_1___{download_time}.xlsx")
    worksheet = workbook.add_worksheet("Statistics")
    # domain_name = 'http://127.0.0.1:8000/'
    domain_name = env('DOMAIN_NAME')

    file_path = f'{domain_name}/{workbook.filename}'

    header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        # 'fg_color': '#F0F4FF'
    })
    header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        'fg_color': '#F0F4FF'
    })

    header_merge_format.set_border_color("#1d588b")

    header_merge_format_bold.set_border_color("#1d588b")
    # wrap_format_horizontal = workbook.add_format({'text_wrap': True,
    #                                    'bold': 1,
    #                                    'border': 1,
    #                                    'align': 'center',
    #                                    'valign': 'vcenter',
    #                                    })

    vertical_header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14
        # 'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14,
        'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format.set_rotation(90)
    vertical_header_merge_format.set_border_color("#1d588b")
    vertical_header_merge_format_bold.set_rotation(90)
    vertical_header_merge_format_bold.set_border_color("#1d588b")

    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    merge_format.set_border_color("#1d588b")

    file_name_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
    })

    bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'
    })
    bold.set_rotation(90)
    bold.set_border_color("#1d588b")

    worksheet.set_column(0,2, 1)
    # worksheet.set_column(2,2,30)
    worksheet.set_column(3, 69, 20)
    # worksheet.set_column(4, 5, 30)
    # worksheet.set_column(6, 32, 12)
    # worksheet.set_column(33, 33, 12)
    # worksheet.set_column(34, 69, 8)
    # worksheet.set_column(10, 16, 40)

    # worksheet.merge_range(2, 2, 3, 2, headers[1], header_merge_format_bold)
    # worksheet.merge_range(2, 2, 3, 2, headers_2[0], header_merge_format_bold)
    worksheet.merge_range(2, 3, 3, 3, headers_2[1], header_merge_format_bold)

    worksheet.merge_range(2, 4, 2 ,5, headers_2[2], header_merge_format_bold)
    worksheet.write(3,4, subheaders_2[headers_2[2]][0],header_merge_format)
    worksheet.write(3,5, subheaders_2[headers_2[2]][1],header_merge_format)


    worksheet.merge_range(2, 6, 2, 9, headers_2[3], header_merge_format_bold)
    # worksheet.write(4, 5, subheaders[headers[6]][0], header_merge_format_bold)
    worksheet.write(3, 6, subheaders_2[headers_2[3]][0], header_merge_format)
    worksheet.write(3, 7, subheaders_2[headers_2[3]][1], header_merge_format)
    worksheet.write(3, 8, subheaders_2[headers_2[3]][2], header_merge_format)
    worksheet.write(3, 9, subheaders_2[headers_2[3]][3], header_merge_format)

    worksheet.merge_range(2, 10, 2, 19, headers_2[4], header_merge_format_bold)
    worksheet.write(3,10,subheaders_2[headers_2[4]][0],header_merge_format)
    worksheet.write(3,11,subheaders_2[headers_2[4]][1],header_merge_format)
    worksheet.write(3,12,subheaders_2[headers_2[4]][2],header_merge_format)
    worksheet.write(3,13,subheaders_2[headers_2[4]][3],header_merge_format)
    worksheet.write(3,14,subheaders_2[headers_2[4]][4],header_merge_format)
    worksheet.write(3,15,subheaders_2[headers_2[4]][5],header_merge_format)
    worksheet.write(3,16,subheaders_2[headers_2[4]][6],header_merge_format)
    worksheet.write(3,17,subheaders_2[headers_2[4]][7],header_merge_format)
    worksheet.write(3,18,subheaders_2[headers_2[4]][8],header_merge_format)
    worksheet.write(3,19,subheaders_2[headers_2[4]][9],header_merge_format)


    worksheet.merge_range(2, 20, 2, 22, headers_2[5], header_merge_format_bold)
    worksheet.write(3,20,subheaders_2[headers_2[5]][0],header_merge_format)
    worksheet.write(3,21,subheaders_2[headers_2[5]][1],header_merge_format)
    worksheet.write(3,22,subheaders_2[headers_2[5]][2],header_merge_format)

    worksheet.merge_range(2, 23, 2, 24, headers_2[6], header_merge_format_bold)
    worksheet.write(3,23,subheaders_2[headers_2[6]][0],header_merge_format)
    worksheet.write(3,24,subheaders_2[headers_2[6]][1],header_merge_format)

    worksheet.merge_range(2, 25, 2, 29, headers_2[7], header_merge_format_bold)
    worksheet.write(3,25,subheaders_2[headers_2[7]][0],header_merge_format)
    worksheet.write(3,26,subheaders_2[headers_2[7]][1],header_merge_format)
    worksheet.write(3,27,subheaders_2[headers_2[7]][2],header_merge_format)
    worksheet.write(3,28,subheaders_2[headers_2[7]][3],header_merge_format)
    worksheet.write(3,29,subheaders_2[headers_2[7]][4],header_merge_format)


    regions = Region.objects.all()
    i = 0
    j = 0
    while j < 1:
        # worksheet.write(i + 4, 2,  j + 1, header_merge_format)
        # worksheet.write(i + 4, 2,  regions[j].name, header_merge_format)

        # jami joylashtirilganla
        worksheet.write(i + 4, 3, base_query.filter(markaz=markaz).distinct().count(), header_merge_format)

        #shundan
        #boshqa davlatdan olib kelingan
        worksheet.write(i+4, 4, base_query.filter(markaz=markaz).filter(accept_center_info__determined_location='5').distinct().count(),header_merge_format)
        worksheet.write(i+4, 5, base_query.filter(markaz=markaz).filter(juvenile__juvenile__passport_type='5').distinct().count(),header_merge_format)

        #kimlar tomonidan olib kelingan
        worksheet.write(i+4, 6, base_query.filter(markaz=markaz).filter(accept_center_info__inspector__inspector_type='1').distinct().count(),header_merge_format)
        worksheet.write(i+4, 7, base_query.filter(markaz=markaz).filter(accept_center_info__inspector__inspector_type='2').distinct().count(),header_merge_format)
        worksheet.write(i+4, 8, base_query.filter(markaz=markaz).filter(accept_center_info__inspector__inspector_type='3').distinct().count(),header_merge_format)
        worksheet.write(i+4, 9, base_query.filter(markaz=markaz).filter(Q(accept_center_info__inspector__inspector_type='4')|Q(accept_center_info__inspector__inspector_type=None)).distinct().count(),header_merge_format)


        #talim turi
        worksheet.write(i+4 ,10 ,base_query.filter(markaz=markaz).filter(juvenile__educationinfojuvenile__school_type='1').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,11 ,base_query.filter(markaz=markaz).filter(juvenile__educationinfojuvenile__school_type='2').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,12 ,base_query.filter(markaz=markaz).filter(juvenile__educationinfojuvenile__school_type='3').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,13 ,base_query.filter(markaz=markaz).filter(juvenile__educationinfojuvenile__school_type='4').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,14 ,base_query.filter(markaz=markaz).filter(juvenile__educationinfojuvenile__school_type='5').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,15 ,base_query.filter(markaz=markaz).filter(juvenile__educationinfojuvenile__school_type='6').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,16 ,base_query.filter(markaz=markaz).filter(juvenile__educationinfojuvenile__school_type='7').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,17 ,base_query.filter(markaz=markaz).filter(juvenile__educationinfojuvenile__school_type='8').distinct().count(),header_merge_format)
        worksheet.write(i+4 ,18 ,base_query.filter(markaz=markaz).filter(Q(juvenile__educationinfojuvenile__school_type='9')|Q(juvenile__juvenile__passport_type=5)).distinct().count(),header_merge_format)
        worksheet.write(i+4 ,19 ,base_query.filter(markaz=markaz).filter(juvenile__educationinfojuvenile__school_type='10').distinct().count(),header_merge_format)

        # yoshi
        # 3 yosh 6 yosh

        today = date.today()
        end_date = today - timedelta(days=3 * 365)
        start_date = today - timedelta(days=6 * 365)
        worksheet.write(i + 4, 20, base_query.filter(markaz=markaz).filter(juvenile__juvenile__birth_date__gte=start_date,
             juvenile__juvenile__birth_date__lte=end_date).distinct().count(),header_merge_format)

        # 7 yosh 13 yosh
        today = date.today()
        end_date = today - timedelta(days=6 * 365)
        start_date = today - timedelta(days=13 * 365)
        worksheet.write(i + 4, 21, base_query.filter(markaz=markaz).filter(
            juvenile__juvenile__birth_date__gte=start_date,
            juvenile__juvenile__birth_date__lt=end_date).distinct().count(), header_merge_format)

        # 14 yosh 18 yosh
        today = date.today()
        end_date = today - timedelta(days=13 * 365)
        start_date = today - timedelta(days=20 * 365)
        worksheet.write(i + 4, 22, base_query.filter(markaz=markaz).filter(
            juvenile__juvenile__birth_date__gte=start_date,
            juvenile__juvenile__birth_date__lt=end_date).distinct().count(), header_merge_format)


        #jinsi
        worksheet.write(i + 4, 23, base_query.filter(markaz=markaz).filter(juvenile__juvenile__gender='M').distinct().count(),header_merge_format)
        worksheet.write(i + 4, 24, base_query.filter(markaz=markaz).filter(juvenile__juvenile__gender='F').distinct().count(),header_merge_format)

        #saqlangan muddatlar
        # 2 kungacha
        worksheet.write(i + 4, 25, query_taqsimlangan.filter(markaz=markaz).filter(

            # time_departure_center__isnull=False,
        #time_departure_center-accept_center_info.arrived_date<=2
            accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(days=2)

        ).distinct().count(), header_merge_format)


        # 10 kun
        worksheet.write(i + 4, 26, query_taqsimlangan.filter(markaz=markaz).filter(
        # F('time_departure_center') - accept_center_info__arrived_date > 2, <=10
        accept_center_info__arrived_date__lt = F('time_departure_center') - timedelta(days=2),
        accept_center_info__arrived_date__gte = F('time_departure_center') - timedelta(days=10)
        ).distinct().count(), header_merge_format)

        # 20 kun
        worksheet.write(i + 4, 27, query_taqsimlangan.filter(markaz=markaz).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=10),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=20)

        ).distinct().count(), header_merge_format)

        # 30 kun
        worksheet.write(i + 4, 28, query_taqsimlangan.filter(markaz=markaz).filter(
            # time_departure_center__isnull=False,
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=20),
            accept_center_info__arrived_date__gte=F('time_departure_center') - timedelta(days=30)

        ).distinct().count(), header_merge_format)

        # 45 kun
        worksheet.write(i + 4, 29, query_taqsimlangan.filter(markaz=markaz).filter(
            # time_departure_center__isnull=False,
            # accept_center_info__arrived_date__lte=F('time_arrival_center') + timedelta(days=45),
            accept_center_info__arrived_date__lt=F('time_departure_center') - timedelta(days=30),

        ).distinct().count(), header_merge_format)

        j+=1
        i+=1



    workbook.close()
    return file_path


def center_to_excel_8_2(request):
    date_from = request.GET.get('date_from')

    date_to = request.GET.get('date_to')
    time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()

    date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
    markaz_id = request.GET.get('markaz_id')

    last_year = int(format(datetime.now(), '%Y'))

    if markaz_id:
        markaz = Markaz.objects.get(id=markaz_id)
    else:
        markaz = request.user.markaz

    if date_from and date_to:
        base_query = models.Juvenile_Markaz.objects.filter(
        status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], accept_center_info__arrived_date__range=[date_from,date_to])
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13'],accept_center_info__arrived_date__range=[date_from,date_to])

    else:
        base_query = models.Juvenile_Markaz.objects.filter(
            status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'],accept_center_info__arrived_date__year=last_year)
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13'],accept_center_info__arrived_date__year=last_year)

    local_time = datetime.now(pytz.timezone('Asia/Tashkent'))
    download_time = format(local_time, '%Y-%m-%d-%H-%M-%S')

    workbook = xlsxwriter.Workbook(f"media/center_statistics_8_2___{download_time}.xlsx")
    worksheet = workbook.add_worksheet("Statistics")
    # domain_name = 'http://127.0.0.1:8000/'
    domain_name = env('DOMAIN_NAME')

    file_path = f'{domain_name}/{workbook.filename}'

    header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        # 'fg_color': '#F0F4FF'
    })
    header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        'fg_color': '#F0F4FF'
    })

    header_merge_format.set_border_color("#1d588b")

    header_merge_format_bold.set_border_color("#1d588b")
    # wrap_format_horizontal = workbook.add_format({'text_wrap': True,
    #                                    'bold': 1,
    #                                    'border': 1,
    #                                    'align': 'center',
    #                                    'valign': 'vcenter',
    #                                    })

    vertical_header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14
        # 'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14,
        'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format.set_rotation(90)
    vertical_header_merge_format.set_border_color("#1d588b")
    vertical_header_merge_format_bold.set_rotation(90)
    vertical_header_merge_format_bold.set_border_color("#1d588b")

    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    merge_format.set_border_color("#1d588b")

    file_name_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
    })

    bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'
    })
    bold.set_rotation(90)
    bold.set_border_color("#1d588b")

    worksheet.set_column(0,2, 1)
    worksheet.set_column(3, 69, 20)
    # worksheet.set_column(4, 5, 30)
    # worksheet.set_column(6, 32, 12)
    # worksheet.set_column(33, 33, 12)
    # worksheet.set_column(34, 69, 8)
    # worksheet.set_column(10, 16, 40)

    # worksheet.merge_range(2, 1, 3, 1, 'Т/Р', header_merge_format_bold)
    # worksheet.merge_range(2, 2, 3, 2, headers_2[0], header_merge_format_bold)
    worksheet.merge_range(2, 3, 3, 3, "Жами олиб келинганлар", header_merge_format_bold)

    worksheet.merge_range(2, 4, 2 ,16, "Олиб келинганлар кимга топширилган ", header_merge_format_bold)
    worksheet.write(3,4, "Бошқа марказга юборилган",header_merge_format_bold)
    worksheet.write(3,5, "Ота-онаси ёки яқин қариндошлари",header_merge_format)
    worksheet.write(3,6, "РЎТМ (ўғил)",header_merge_format)
    worksheet.write(3,7, "РЎТМ (қиз)",header_merge_format)
    worksheet.write(3,8, "ИТМ",header_merge_format)
    worksheet.write(3,9, "Меҳри-бонлик уйлари",header_merge_format)
    worksheet.write(3,10, "'SOS' болалар шаҳарчаси",header_merge_format)
    worksheet.write(3,11, "Оилавий болалар уйи",header_merge_format)
    worksheet.write(3,12, "Потранат",header_merge_format)
    worksheet.write(3,13, "Фарзандлик",header_merge_format)
    worksheet.write(3,14, "Васий ва ҳомий",header_merge_format)
    worksheet.write(3,15, "ССМга юборилган",header_merge_format)
    worksheet.write(3,16, "Бошқа давлатга юборилган",header_merge_format)

    worksheet.merge_range(2, 17, 3 ,17, "Ҳозирда Марказларда сақланётган болалар сони ", header_merge_format_bold)

    worksheet.merge_range(2, 18, 2 ,19, "Жинси", header_merge_format_bold)
    worksheet.write(3,18, "Ўғил бола",header_merge_format)
    worksheet.write(3,19, "Қиз бола",header_merge_format)





    regions = Region.objects.all()
    i = 0
    j = 0
    while j < 1:

        # jami olib kelinganlar
        worksheet.write(i + 4, 3, base_query.filter(markaz = markaz).distinct().count(),header_merge_format)
                        # models.Juvenile_Markaz.objects.filter(juvenile__educationinfojuvenile__isnull=False,juvenile__addressinfojuvenile__isnull=False,
                        #                     juvenile__juvenile__isnull=False,juvenile__parentinfojuvenile__isnull=False).
                        #                     filter(markaz=markaz).distinct().count(), header_merge_format)
        # kimlarga topshirilgan
        #boshqa markazga yuborilgan
        worksheet.write(i+4,4, query_taqsimlangan.filter(markaz=markaz,status='8').distinct().count(),header_merge_format)

        # ota-ona yoki ornini bosuvchi
        worksheet.write(i + 4, 5,
                        query_taqsimlangan.filter(markaz=markaz).filter(
                            Q(distributed_info__distribution_type='1') | Q(
                                distributed_info__distribution_type='8')).distinct().count(), header_merge_format)

        # rotm ogil bola
        worksheet.write(i + 4, 6, query_taqsimlangan.filter(
            markaz=markaz, distributed_info__rotm_type='2').distinct().count(),
                        header_merge_format)
        # rotm qiz  bola
        worksheet.write(i + 4, 7, query_taqsimlangan.filter(
            markaz=markaz, distributed_info__rotm_type='1').distinct().count(),
                        header_merge_format)

        # itm
        worksheet.write(i + 4, 8, query_taqsimlangan.filter(
            markaz=markaz,distributed_info__distribution_type='3').distinct().count(), header_merge_format)


        # mehribonlik uyi
        worksheet.write(i + 4, 9, query_taqsimlangan.filter(
           markaz=markaz,distributed_info__type_guardianship='5').distinct().count(), header_merge_format)



        # sos bolalar
        worksheet.write(i + 4, 10, query_taqsimlangan.filter(
           markaz=markaz,distributed_info__type_guardianship='7').distinct().count(), header_merge_format)


        # oilaviy bolalar uyi
        worksheet.write(i + 4, 11, query_taqsimlangan.filter(
            markaz=markaz,distributed_info__type_guardianship='6').distinct().count(), header_merge_format)


        # patronat
        worksheet.write(i + 4, 12, query_taqsimlangan.filter(
            markaz=markaz,distributed_info__type_guardianship='3').distinct().count(), header_merge_format)


        # farzandlik
        worksheet.write(i + 4, 13, query_taqsimlangan.filter(
            markaz=markaz,distributed_info__type_guardianship='4').distinct().count(), header_merge_format)


        # vasiy homiy
        worksheet.write(i + 4, 14,
                        query_taqsimlangan.filter(markaz=markaz).filter(
                            Q(distributed_info__type_guardianship='1') | Q(
                                distributed_info__type_guardianship='2')).exclude(distributed_info__distribution_type='1').distinct().count(), header_merge_format)

        # sogliqni saqlash
        worksheet.write(i + 4, 15, query_taqsimlangan.filter(
            markaz=markaz,distributed_info__distribution_type='5').distinct().count(), header_merge_format)


        # boshqa davlatga yuborish
        worksheet.write(i + 4, 16, query_taqsimlangan.filter(
            markaz=markaz,distributed_info__distribution_type='7').distinct().count(), header_merge_format)


        #hozirda markazda saqlanayotgan
        if date_from and date_to:
            query = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],accept_center_info__arrived_date__range=[date_from,date_to],markaz=markaz)
        else:
            query = models.Juvenile_Markaz.objects.filter(status__in=['2','10'],markaz=markaz,accept_center_info__arrived_date__year=last_year)

        worksheet.write(i+4, 17,query.distinct().count(),header_merge_format)
        worksheet.write(i+4, 18,query.filter(juvenile__juvenile__gender='M').distinct().count(),header_merge_format)
        worksheet.write(i+4, 19,query.filter(juvenile__juvenile__gender='F').distinct().count(),header_merge_format)

        j += 1
        i += 1



    workbook.close()
    return file_path


def center_to_excel_8_3(request):
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    time_date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
    date_to = (time_date_to + timedelta(days=1)).strftime('%Y-%m-%d')
    markaz_id = request.GET.get('markaz_id')
    last_year = int(format(datetime.now(), '%Y'))


    if markaz_id:
        markaz = Markaz.objects.get(id=markaz_id)
    else:
        markaz = request.user.markaz
    if date_from and date_to:
        base_query = models.Juvenile_Markaz.objects.filter(
        status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], accept_center_info__arrived_date__range=[date_from,date_to])
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9', '11', '12', '13'],accept_center_info__arrived_date__range=[date_from,date_to])

    else:
        base_query = models.Juvenile_Markaz.objects.filter(
            status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'],accept_center_info__arrived_date__year=last_year)
        query_taqsimlangan = models.Juvenile_Markaz.objects.filter(
            status__in=['3', '4', '5', '6', '7', '8', '9','11', '12', '13'],accept_center_info__arrived_date__year=last_year)

    local_time = datetime.now(pytz.timezone('Asia/Tashkent'))
    download_time = format(local_time, '%Y-%m-%d-%H-%M-%S')

    workbook = xlsxwriter.Workbook(f"media/center_statistics_8_3___{download_time}.xlsx")
    worksheet = workbook.add_worksheet("Statistics")
    # domain_name = 'http://127.0.0.1:8000/'
    domain_name = env('DOMAIN_NAME')

    file_path = f'{domain_name}/{workbook.filename}'

    header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        # 'fg_color': '#F0F4FF'
    })
    header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'text_wrap': True,
        'font_size': 15,
        'fg_color': '#F0F4FF'
    })

    header_merge_format.set_border_color("#1d588b")

    header_merge_format_bold.set_border_color("#1d588b")
    # wrap_format_horizontal = workbook.add_format({'text_wrap': True,
    #                                    'bold': 1,
    #                                    'border': 1,
    #                                    'align': 'center',
    #                                    'valign': 'vcenter',
    #                                    })

    vertical_header_merge_format = workbook.add_format({
        # 'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14
        # 'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format_bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_size': 14,
        'fg_color': '#F0F4FF'
    })
    vertical_header_merge_format.set_rotation(90)
    vertical_header_merge_format.set_border_color("#1d588b")
    vertical_header_merge_format_bold.set_rotation(90)
    vertical_header_merge_format_bold.set_border_color("#1d588b")

    merge_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'})

    merge_format.set_border_color("#1d588b")

    file_name_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
    })

    bold = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': 'white'
    })
    bold.set_rotation(90)
    bold.set_border_color("#1d588b")

    worksheet.set_column(0,2, 1)
    worksheet.set_column(3, 69, 20)
    # worksheet.set_column(4, 5, 30)
    # worksheet.set_column(6, 32, 12)
    # worksheet.set_column(33, 33, 12)
    # worksheet.set_column(34, 69, 8)
    # worksheet.set_column(10, 16, 40)

    # worksheet.merge_range(2, 2, 3, 2, headers_2[0], header_merge_format_bold)
    worksheet.merge_range(2, 3, 3, 3, "Жами масъулларга топширилган  вояга етмаганлар сони", header_merge_format_bold)
    worksheet.merge_range(2, 4, 3, 4, 'Хар ойда, Мониторинг қилинганлари сони ', header_merge_format_bold)
    worksheet.merge_range(2, 5, 3, 5, 'Фоизи ', header_merge_format_bold)
    worksheet.merge_range(2, 6, 3, 6, 'МЖтКнинг 47-моддасига асосан кўрилган чоралар сони ', header_merge_format_bold)
    worksheet.merge_range(2, 7, 3, 7, 'Психологлар томонидан ота-оналарга ўтказилган тренинглар сони ', header_merge_format_bold)
    worksheet.merge_range(2, 8, 3, 8, 'Мониторинг жараёнида ота-онасидан марказга қайтарилганлар  ', header_merge_format_bold)
    worksheet.merge_range(2, 9, 3, 9, 'Марказ томонидан ИТМга жойлаштирилганлар  ', header_merge_format_bold)
    worksheet.merge_range(2, 10, 3, 10, 'ИТМдан қочганлар ', header_merge_format_bold)
    worksheet.merge_range(2, 11, 3, 11, 'ИТМни тугатганлар ', header_merge_format_bold)

    worksheet.merge_range(2,12, 2,15,'Ихтисослаштирилган таълим муассасасини тугатгандан сўнг бандлиги таъминланганлар',header_merge_format_bold)
    worksheet.write(3,12, 'Олий таълим муассасасига кирганлар',header_merge_format_bold)
    worksheet.write(3,13, 'Касб-ҳунарга ўқитилганлар',header_merge_format_bold)
    worksheet.write(3,14, 'Муддатли ҳарбий хизматга юборилганлдар',header_merge_format_bold)
    worksheet.write(3,15, 'Меҳнат органлари томонидан ишга жойлаштирилганлар',header_merge_format_bold)

    worksheet.merge_range(2,16, 3,16,'Бандлиги таъминланмаган',header_merge_format_bold)







    regions = Region.objects.all()
    i = 0
    j = 0
    while j < 1:

        # Жами масъулларга топширилган  вояга етмаганлар сони
        worksheet.write(i + 4, 3, query_taqsimlangan.filter(markaz=markaz).count(), header_merge_format_bold)

        #Хар ойда, Мониторинг қилинганлари сони
        worksheet.write(i + 4, 4, query_taqsimlangan.filter(markaz=markaz).filter(monitoring_info__isnull=False).distinct().count(), header_merge_format)

        #Фоизи
        if query_taqsimlangan.filter(markaz=markaz).count() == 0:
            result = 0
        else:
            result = 100*(query_taqsimlangan.filter(markaz=markaz).filter(monitoring_info__isnull=False).distinct().count()/query_taqsimlangan.filter(markaz=markaz).distinct().count())
        print('RESULT',round(result, 1))
        worksheet.write(i + 4, 5, round(result, 1), header_merge_format_bold)

        #МЖтКнинг 47-моддасига асосан кўрилган чоралар сони
        worksheet.write(i + 4, 6, query_taqsimlangan.filter(markaz=markaz).filter(monitoring_info__isnull=False,monitoring_info__is_action_been_taken=True).distinct().count(), header_merge_format)

        #Психологлар томонидан ота-оналарга ўтказилган тренинглар сони
        worksheet.write(i+4,7,query_taqsimlangan.filter(markaz=markaz,distributed_info__isnull=False, distributed_info__psyhology_condition__isnull=False).distinct().count(),header_merge_format)

        #Мониторинг жараёнида ота-онасидан марказга қайтарилганлар
        worksheet.write(i+4,8,query_taqsimlangan.filter(markaz=markaz,monitoring_info__monitoring_status='3').distinct().count(),header_merge_format)

        #Марказ томонидан ИТМга жойлаштирилганлар
        worksheet.write(i+4,9,query_taqsimlangan.filter(markaz=markaz,distributed_info__distribution_type='3').distinct().count(),header_merge_format)

        #ИТМдан қочганлар
        worksheet.write(i+4,10,query_taqsimlangan.filter(markaz=markaz,status='12').distinct().count(),header_merge_format)

        #ИТМни тугатганлар
        worksheet.write(i+4,11,query_taqsimlangan.filter(markaz=markaz,monitoring_info__monitoring_status='2').distinct().count(),header_merge_format)


        #Ихтисослаштирилган таълим муассасасини тугатгандан сўнг бандлиги таъминланганлар
        # worksheet.write(i+4,12,'QQQ',header_merge_format)
        worksheet.write(i+4,12,query_taqsimlangan.filter(markaz=markaz).filter(employment_info__employment_education_type='1',employment_info__is_accepted_to_school=True).distinct().count(),header_merge_format)
        worksheet.write(i+4,13,query_taqsimlangan.filter(markaz=markaz).filter(employment_info__employment_education_type='2',employment_info__is_accepted_to_school=True).distinct().count(),header_merge_format)
        worksheet.write(i+4,14,query_taqsimlangan.filter(markaz=markaz).filter(employment_info__is_military=True).distinct().count(),header_merge_format)
        worksheet.write(i+4,15,0,header_merge_format)
        worksheet.write(i+4,16,query_taqsimlangan.filter(markaz=markaz).filter(employment_info__isnull=False,employment_info__employment_file = '').distinct().count(),header_merge_format)




        j += 1
        i += 1



    workbook.close()
    return file_path

