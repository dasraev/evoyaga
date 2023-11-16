from info.models import Litsey

from pandas import *

xls = ExcelFile('scripts/excel_data/litsey.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()

litsey = []
for n in df['id']:
    litsey.append({
        'id': df['id'][n],
        'name': df['name'][n],
        'region_id': df['region_id'][n]
    })

count = 0
for item in litsey:
    count += 1
    item = Litsey(
        id=item['id'],
        name=item['name'],
        region_id_id=item['region_id'],
    )
    item.save()
    print(f'Litsey successfully added - ({count})')

