from info.models import Mahalla

from pandas import *


xls = ExcelFile('scripts/excel_data/mahalla.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()

mahalla = []
for n in df['id']:
    mahalla.append({
        'id': df['id'][n],
        'name': df['name'][n],
        'district_id': df['district_id'][n]
    })


for item in mahalla:
    item = Mahalla(
        id=item['id'],
        name=item['name'],
        district_id_id=item['district_id'],
    )
    item.save()
    print('Mahalla successfully added')

