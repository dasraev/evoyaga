import xlwt
from juvenile.models import *
from datetime import datetime
from info.enums import *
dict_inspector_type_choice = dict(INSPECTOR_TYPE_CHOICE)
dict_marital_status_type_choice = dict(MARITAL_STATUS_TYPE_CHOICE)


current_year = datetime.now().year
def get_education_info(education_info):
    if education_info is None:
        return "ўқимайди"

    school_type = education_info.school_type
    if school_type == '1' and education_info.kindergarten:
        return f"{education_info.kindergarten.district_id.name} {education_info.kindergarten.name}"
    elif school_type == '2' and education_info.school:
        return f"{education_info.school.district_id.name} {education_info.school.name}"
    elif school_type == '3' and education_info.vocational_school:
        return f"{education_info.vocational_school.region_id.name} {education_info.vocational_school.name}"
    elif school_type == '4' and education_info.college:
        return f"{education_info.college.region_id.name} {education_info.college.name}"
    elif school_type == '5' and education_info.litsey:
        return f"{education_info.litsey.region_id.name} {education_info.litsey.name}"
    elif school_type == '6' and education_info.texnikum:
        return f"{education_info.texnikum.region_id.name} {education_info.texnikum.name}"
    elif school_type == '7' and education_info.special_education:
        return f"{education_info.special_education.region_id.name} {education_info.special_education.name}"
    elif school_type == '8' and education_info.university:
        return f"{education_info.university.region_id.name} {education_info.university.name}"

    return "ўқимайди"

def export_juvenile_data():
    juveline_markazs = Juvenile_Markaz.objects.filter(created_at__year=current_year).exclude(accept_center_info=None)
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('juveniles')
    sheet.col(0).width = 256 * 30
    sheet.col(1).width = 256 * 30
    sheet.col(2).width = 256 * 30
    sheet.col(3).width = 256 * 30
    sheet.col(4).width = 256 * 30
    sheet.col(5).width = 256 * 30
    sheet.col(6).width = 256 * 30
    sheet.col(7).width = 256 * 30
    sheet.col(8).width = 256 * 30
    sheet.col(9).width = 256 * 30
    sheet.col(10).width = 256 * 30
    sheet.col(11).width = 256 * 30
    sheet.col(12).width = 256 * 30
    sheet.col(13).width = 256 * 30

    header_style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True  # Make the font bold
    font.height = 20 * 14  # Set the font size (14-point)
    header_style.font = font

    headers = ['Ф.И.Ш','Жинси','Туғилган йили ой куни', 'Яшаш манзили, ҳудуд,туман-шаҳар, маҳалла, кўча ва уй рамқами',
               'Марказга қабул қилинган боланинг ўқиш муассасаси','Олиб келиш сабаби','Келган вақти','Кетган вақти','Кимларга топширилди','қабул қилинган маркази']

    for idx, header in enumerate(headers):
        sheet.write(0, idx, header,header_style)
    data = [
        [
         f"{juveline_markaz.juvenile.juvenile.last().first_name} {juveline_markaz.juvenile.juvenile.last().last_name} {juveline_markaz.juvenile.juvenile.last().father_name}",
         'эркак ' if juveline_markaz.juvenile.juvenile.last().gender == 'M' else 'аёл',
         str(juveline_markaz.juvenile.juvenile.first().birth_date),
         f"{juveline_markaz.juvenile.juvenile.last().birth_district.region_id.name} {juveline_markaz.juvenile.juvenile.last().birth_district.name} {juveline_markaz.juvenile.addressinfojuvenile_set.first().address_mahalla.name} {juveline_markaz.juvenile.addressinfojuvenile_set.first().address}" if juveline_markaz.juvenile.addressinfojuvenile_set.first()  and juveline_markaz.juvenile.juvenile.last().birth_district
         else f"{juveline_markaz.juvenile.juvenile.last().birth_district.region_id.name} {juveline_markaz.juvenile.juvenile.last().birth_district.name}" if juveline_markaz.juvenile.juvenile.last().birth_district
        else "",

        # f"{juveline_markaz.juvenile.juvenile.last().birth_district.region_id.name if juveline_markaz.juvenile.juvenile.last().birth_district else ''} "
        # f"{juveline_markaz.juvenile.juvenile.last().birth_district.name if juveline_markaz.juvenile.juvenile.last().birth_district else ''} "
        # f"{juveline_markaz.juvenile.juvenile.last().birth_district if juveline_markaz.juvenile.juvenile.last().birth_district else ''} "
        # f"{juveline_markaz.juvenile.addressinfojuvenile_set.first().address_mahalla.name if juveline_markaz.juvenile.addressinfojuvenile_set.first() and juveline_markaz.juvenile.addressinfojuvenile_set.first().address_mahalla else ''} "
        # f"{juveline_markaz.juvenile.addressinfojuvenile_set.first().address if juveline_markaz.juvenile.addressinfojuvenile_set.first() else ''}"
            
        # f"{juveline_markaz.juvenile.educationinfojuvenile_set.last().kindergarten.district_id.name} {juveline_markaz.juvenile.educationinfojuvenile_set.last().kindergarten.name}" if juveline_markaz.juvenile.educationinfojuvenile_set.last() and  juveline_markaz.juvenile.educationinfojuvenile_set.last().school_type == '1'
        # else f"{juveline_markaz.juvenile.educationinfojuvenile_set.last().school.district_id.name} {juveline_markaz.juvenile.educationinfojuvenile_set.last().school.name}" if  juveline_markaz.juvenile.educationinfojuvenile_set.last() and  juveline_markaz.juvenile.educationinfojuvenile_set.last().school_type == '2'
        # else f"{juveline_markaz.juvenile.educationinfojuvenile_set.last().vocational_school.region_id.name} {juveline_markaz.juvenile.educationinfojuvenile_set.last().vocational_school.name}" if juveline_markaz.juvenile.educationinfojuvenile_set.last() and  juveline_markaz.juvenile.educationinfojuvenile_set.last().school_type == '3'
        # else f"{juveline_markaz.juvenile.educationinfojuvenile_set.last().college.region_id.name} {juveline_markaz.juvenile.educationinfojuvenile_set.last().college.name}" if juveline_markaz.juvenile.educationinfojuvenile_set.last() and  juveline_markaz.juvenile.educationinfojuvenile_set.last().school_type == '4'
        # else f"{juveline_markaz.juvenile.educationinfojuvenile_set.last().litsey.region_id.name} {juveline_markaz.juvenile.educationinfojuvenile_set.last().litsey.name}" if juveline_markaz.juvenile.educationinfojuvenile_set.last() and  juveline_markaz.juvenile.educationinfojuvenile_set.last().school_type == '5'
        # else f"{juveline_markaz.juvenile.educationinfojuvenile_set.last().texnikum.region_id.name} {juveline_markaz.juvenile.educationinfojuvenile_set.last().texnikum.name}" if juveline_markaz.juvenile.educationinfojuvenile_set.last() and  juveline_markaz.juvenile.educationinfojuvenile_set.last().school_type == '6'
        # else f"{juveline_markaz.juvenile.educationinfojuvenile_set.last().special_education.region_id.name} {juveline_markaz.juvenile.educationinfojuvenile_set.last().special_education.name}" if juveline_markaz.juvenile.educationinfojuvenile_set.last() and  juveline_markaz.juvenile.educationinfojuvenile_set.last().school_type == '7'
        # else f"{juveline_markaz.juvenile.educationinfojuvenile_set.last().university.region_id.name} {juveline_markaz.juvenile.educationinfojuvenile_set.last().university.name}" if juveline_markaz.juvenile.educationinfojuvenile_set.last() and  juveline_markaz.juvenile.educationinfojuvenile_set.last().school_type == '8'
        # else "ўқимайди",
        get_education_info(juveline_markaz.juvenile.educationinfojuvenile_set.last()),


        juveline_markaz.accept_center_info.sub_reason_bringing_child.parent.title,
        str(juveline_markaz.accept_center_info.arrived_date),
        str(juveline_markaz.distributed_info.created_at) if juveline_markaz.distributed_info else "",
        "Oila" if juveline_markaz.distributed_info and  juveline_markaz.distributed_info.distribution_type == '1'
        else "Vasiylik organi orqali" if juveline_markaz.distributed_info and  juveline_markaz.distributed_info.distribution_type == '2'
        else "ITM" if juveline_markaz.distributed_info and  juveline_markaz.distributed_info.distribution_type == '3'
        else "RO'TM" if juveline_markaz.distributed_info and  juveline_markaz.distributed_info.distribution_type == '4'
        else "Sog'liqni saqlash muassasasi" if juveline_markaz.distributed_info and  juveline_markaz.distributed_info.distribution_type == '5'
        else "Boshqa markazga yuborish" if juveline_markaz.distributed_info and  juveline_markaz.distributed_info.distribution_type == '6'
        else "Boshqa davlatga yuborish" if juveline_markaz.distributed_info and  juveline_markaz.distributed_info.distribution_type == '7'
        else "Boshqa davlatga yuborish" if juveline_markaz.distributed_info and  juveline_markaz.distributed_info.distribution_type == '7'
        else "Boshqalar" if juveline_markaz.distributed_info and  juveline_markaz.distributed_info.distribution_type == '8'
        else "",
        juveline_markaz.markaz.name


        ] for juveline_markaz in juveline_markazs
    ]

    for row_num, row_data in enumerate(data, 1):
        for col_num, cell_data in enumerate(row_data):
            sheet.write(row_num, col_num, cell_data)
    filename = f'juvenile_data1_{current_year}.xls'
    wb.save(filename)


# export_juvenile_data()


def export_juvenile_excel_data(wb):
    juvenile_markazs = Juvenile_Markaz.objects.exclude(accept_center_info=None)
    sheet = wb.add_sheet('juveniles')
    sheet.col(0).width = 256 * 30
    sheet.col(1).width = 256 * 30
    sheet.col(2).width = 256 * 30
    sheet.col(3).width = 256 * 30
    sheet.col(4).width = 256 * 30
    sheet.col(5).width = 256 * 30
    sheet.col(6).width = 256 * 30
    sheet.col(7).width = 256 * 30
    sheet.col(8).width = 256 * 30
    sheet.col(9).width = 256 * 30
    sheet.col(10).width = 256 * 30
    sheet.col(11).width = 256 * 30
    sheet.col(12).width = 256 * 30
    sheet.col(13).width = 256 * 30

    header_style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True  # Make the font bold
    font.height = 20 * 14  # Set the font size (14-point)
    header_style.font = font

    headers = ['Марказ худдуд номи','Ф.И.Ш', 'Жинси', 'Туғилган йили ой куни',
               'Яшаш манзили, ҳудуд,туман-шаҳар, маҳалла, кўча ва уй рамқами',
               'Марказга қабул қилинган боланинг ўқиш муассасаси', 'Олиб келиш сабаби',
               "Оилавий ахволи","Олиб келинган жойлари","Кимлар томонидан олиб келинган",
               "Кайта жойлаш-тирилганлар (сони)",
                
               'Келган вақти', 'Кетган вақти','Кимларга топширилди']


    for idx, header in enumerate(headers):
        sheet.write(0, idx, header, header_style)
    data = []
    for juvenile_markaz in juvenile_markazs:
        olib_kelingan_joylari = ",".join(tuple(juvenile_markaz.juvenile.juvenile_markaz.values_list('markaz__name',flat=True)))
        juvenile_data = [
            juvenile_markaz.markaz.name,
            f"{juvenile_markaz.juvenile.juvenile.last().first_name} {juvenile_markaz.juvenile.juvenile.last().last_name} {juvenile_markaz.juvenile.juvenile.last().father_name}",
            'эркак ' if juvenile_markaz.juvenile.juvenile.last().gender == 'M' else 'аёл',
            str(juvenile_markaz.juvenile.juvenile.first().birth_date),
            f"{juvenile_markaz.juvenile.juvenile.last().birth_district.region_id.name} {juvenile_markaz.juvenile.juvenile.last().birth_district.name} {juvenile_markaz.juvenile.addressinfojuvenile_set.first().address_mahalla.name} {juvenile_markaz.juvenile.addressinfojuvenile_set.first().address}" if juvenile_markaz.juvenile.addressinfojuvenile_set.first() and juvenile_markaz.juvenile.juvenile.last().birth_district
            else f"{juvenile_markaz.juvenile.juvenile.last().birth_district.region_id.name} {juvenile_markaz.juvenile.juvenile.last().birth_district.name}" if juvenile_markaz.juvenile.juvenile.last().birth_district
            else "",

            get_education_info(juvenile_markaz.juvenile.educationinfojuvenile_set.last()),

            juvenile_markaz.accept_center_info.sub_reason_bringing_child.parent.title,
            #write here
            dict_marital_status_type_choice[int(juvenile_markaz.juvenile.parentinfojuvenile_set.last().marital_status)] if juvenile_markaz.juvenile.parentinfojuvenile_set.last() else "" ,
            olib_kelingan_joylari,
            dict_inspector_type_choice[int(juvenile_markaz.accept_center_info.inspector.inspector_type)],
            juvenile_markaz.juvenile.accepted_center_number,


            str(juvenile_markaz.accept_center_info.arrived_date),
            str(juvenile_markaz.distributed_info.created_at) if juvenile_markaz.distributed_info else "",
            "Oila" if juvenile_markaz.distributed_info and juvenile_markaz.distributed_info.distribution_type == '1'
            else "Vasiylik organi orqali" if juvenile_markaz.distributed_info and juvenile_markaz.distributed_info.distribution_type == '2'
            else "ITM" if juvenile_markaz.distributed_info and juvenile_markaz.distributed_info.distribution_type == '3'
            else "RO'TM" if juvenile_markaz.distributed_info and juvenile_markaz.distributed_info.distribution_type == '4'
            else "Sog'liqni saqlash muassasasi" if juvenile_markaz.distributed_info and juvenile_markaz.distributed_info.distribution_type == '5'
            else "Boshqa markazga yuborish" if juvenile_markaz.distributed_info and juvenile_markaz.distributed_info.distribution_type == '6'
            else "Boshqa davlatga yuborish" if juvenile_markaz.distributed_info and juvenile_markaz.distributed_info.distribution_type == '7'
            else "Boshqa davlatga yuborish" if juvenile_markaz.distributed_info and juvenile_markaz.distributed_info.distribution_type == '7'
            else "Boshqalar" if juvenile_markaz.distributed_info and juvenile_markaz.juvenile_markaz.distributed_info.distribution_type == '8'
            else "",

        ]
        data.append(juvenile_data)


    for row_num, row_data in enumerate(data, 1):
        for col_num, cell_data in enumerate(row_data):
            sheet.write(row_num, col_num, cell_data)
    filename = f'juvenile_data_excell.xls'
    wb.save(filename)

