from pprint import pprint
from info.models import District

from pandas import *


xls = ExcelFile('scripts/excel_data/districts.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()

districts = []
for n in df['id']:
    districts.append({
        'id': df['id'][n],
        'name': df['name'][n],
        'region_id': df['region_id'][n],
        'extra_id': df['extra_id'][n]
    })


#pprint(districts)

for district in districts:
    item = District(
        id=district['id'],
        name=district['name'],
        region_id_id=district['region_id'],
        extra_id=district['extra_id'],
    )
    item.save()
    print('District successfully added')

