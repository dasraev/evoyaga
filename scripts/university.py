from info.models import University

from pandas import *


xls = ExcelFile('scripts/excel_data/universities.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()

universities = []
for n in df['id']:
    universities.append({
        'id': df['id'][n],
        'name': df['name'][n],
        'region_id': df['region_id'][n]
    })

count = 0
for university in universities:
    count += 1
    item = University(
        id=university['id'],
        name=university['name'],
        region_id_id=university['region_id'],
    )
    item.save()
    print(f'University successfully added - ({count})')

