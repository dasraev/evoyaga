from info.models import SpecialEducation

from pandas import *

xls = ExcelFile('scripts/excel_data/special_educations.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()

special_educations = []
for n in df['id']:
    special_educations.append({
        'id': df['id'][n],
        'name': df['name'][n],
        'region_id': df['region_id'][n]
    })

count = 0
for education in special_educations:
    count += 1
    item = SpecialEducation(
        id=education['id'],
        name=education['name'],
        region_id_id=education['region_id'],
    )
    item.save()
    print(f'Special education successfully added - ({count})')

