from info.models import Kindergarten

from pandas import *


xls = ExcelFile('scripts/excel_data/kindergartens.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()

kindergartens = []
for n in df['id']:
    kindergartens.append({
        'id': df['id'][n],
        'name': df['name'][n],
        'district_id': df['district_id'][n]
    })

count = 0
for kindergarten in kindergartens:
    count += 1
    item = Kindergarten(
        id=kindergarten['id'],
        name=kindergarten['name'],
        district_id_id=kindergarten['district_id'],
    )
    item.save()
    print(f'Kindergarten successfully added - ({count})')

