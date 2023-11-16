from info.models import MedicalList

medical_lists = [
    {
        "extra_id": 1,
        "title": "Ruhiy-asab kasalliklari dispanseri",
    },
    {
        "extra_id": 2,
        "title": "Narkologiya dispanseri",
    },
    {
        "extra_id": 3,
        "title": "Teri-tanosil dispanseri",
    },
    {
        "extra_id": 4,
        "title": "Sil kasaliklari dispanseri",
    }
]

for medical_list in medical_lists:
    item = MedicalList(
        title=medical_list['title'],
        extra_id=medical_list['extra_id'],
    )
    item.save()
    print('medical_list successfully added')