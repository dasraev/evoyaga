from info.models import VocationalSchool

from pandas import *

xls = ExcelFile('scripts/excel_data/vocational_schools.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()

vocational_schools = []
for n in df['id']:
    vocational_schools.append({
        'id': df['id'][n],
        'name': df['name'][n],
        'region_id': df['region_id'][n]
    })

count = 0
for item in vocational_schools:
    count += 1
    item = VocationalSchool(
        id=item['id'],
        name=item['name'],
        region_id_id=item['region_id'],
    )
    item.save()
    print(f'Vocational schools successfully added - ({count})')

