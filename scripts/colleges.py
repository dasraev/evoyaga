from info.models import College

from pandas import *


xls = ExcelFile('scripts/excel_data/colleges.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()

colleges = []
for n in df['id']:
    colleges.append({
        'id': df['id'][n],
        'name': df['name'][n],
        'region_id': df['region_id'][n]
    })

count = 0
for college in colleges:
    count += 1
    item = College(
        id=college['id'],
        name=college['name'],
        region_id_id=college['region_id'],
    )
    item.save()
    print(f'College successfully added - ({count})')

