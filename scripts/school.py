from info.models import School

from pandas import *


xls = ExcelFile('scripts/excel_data/schools.xlsx')
df = xls.parse(xls.sheet_names[0]).to_dict()

schools = []
for n in df['id']:
    schools.append({
        'id': df['id'][n],
        'name': df['name'][n],
        'district_id': df['district_id'][n]
    })

count = 0
for school in schools:
    count += 1
    item = School(
        id=school['id'],
        name=school['name'],
        district_id_id=school['district_id'],
    )
    item.save()
    print(f'School successfully added - ({count})')

