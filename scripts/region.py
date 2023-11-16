from pandas import *
from info.models import Region

xls = ExcelFile('scripts/excel_data/regions.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()
regions = []

for n in df['id']:
    regions.append({
        'id': df['id'][n],
        'name': df['region_name'][n],
        'extra_id': df['extra_id'][n]
    })

for region in regions:
    item = Region(
        id=region['id'],
        name=region['name'],
        extra_id=region['extra_id'],
    )
    item.save()
    print('Region successfully added')

