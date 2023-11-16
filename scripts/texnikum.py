from info.models import Texnikum

from pandas import *


xls = ExcelFile('scripts/excel_data/texnikums.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()

texnikums = []
for n in df['id']:
    texnikums.append({
        'id': df['id'][n],
        'name': df['name'][n],
        'region_id': df['region_id'][n]
    })

count = 0
for texnikum in texnikums:
    count += 1
    item = Texnikum(
        id=texnikum['id'],
        name=texnikum['name'],
        region_id_id=texnikum['region_id'],
    )
    item.save()
    print(f'Texnikum successfully added - ({count})')

