from info.models import SubReasonBringingChild

sub_reason_bringning_children = [
    {
        "id": 1,
        "parent": 1,
        "title": "Koʼngil ochar maskanda aniqlangan",
        "order": "1"
    },
    {
        "id": 2,
        "parent": 1,
        "title": "Oilasidan oʼz boshimchalik bilan ketgan",
        "order": "2"
    },
    {
        "id": 3,
        "parent": 1,
        "title": "Taʼlim muassasalaridan oʼzboshimchalik bilan ketgan",
        "order": "3"
    },
    {
        "id": 4,
        "parent": 1,
        "title": "Mayishiy xizmat koʼrsatish joylarida aniqlangan",
        "order": "4"
    },
    {
        "id": 5,
        "parent": 1,
        "title": "Noqonuniy diniy taʼlim muassasalarida aniqlangan",
        "order": "5"
    },
    {
        "id": 6,
        "parent": 2,
        "title": "Yetim bola",
        "order": "1"
    },
    {
        "id": 7,
        "parent": 2,
        "title": "Tashlab ketilgan",
        "order": "2"
    },
    {
        "id": 8,
        "parent": 3,
        "title": "Muayyan yashash joyiga ega boʼlmagan",
        "order": "1"
    },
    {
        "id": 9,
        "parent": 3,
        "title": "Tilanchilik bilan shugʼulanayotgan",
        "order": "2"
    },
    {
        "id": 10,
        "parent": 3,
        "title": "Boshqa davlatdan olib kelingan",
        "order": "3"
    },
    {
        "id": 11,
        "parent": 3,
        "title": "Boshqa davlat bolasi",
        "order": "4"
    },
    {
        "id": 12,
        "parent": 3,
        "title": "Yashash sharoiti ogʼir",
        "order": "5"
    },
    {
        "id": 13,
        "parent": 3,
        "title": "Monitoring davomida Markazga qaytarilgan",
        "order": "6"
    },
    {
        "id": 14,
        "parent": 4,
        "title": "Boquvchisi spirtli ichimlikga ruju qoʼygan",
        "order": "1"
    },
    {
        "id": 15,
        "parent": 4,
        "title": "Boquvchisi giyohvand",
        "order": "2"
    },
    {
        "id": 16,
        "parent": 4,
        "title": "Boquvchisi yengil tabiatli",
        "order": "3"
    },
    {
        "id": 17,
        "parent": 4,
        "title": "Boquvchisi ruhiy kasal",
        "order": "4"
    },
    {
        "id": 18,
        "parent": 4,
        "title": "Boquvchisi DEO aʼzosi",
        "order": "5"
    },
    {
        "id": 19,
        "parent": 4,
        "title": "Boquvchisi shavqatsiz muomilada boʼlgan",
        "order": "6"
    },
    {
        "id": 20,
        "parent": 5,
        "title": "ROʼTM (Baxt)ga xujjati rasmiylashtirilayotgan",
        "order": "1"
    },    
    {
        "id": 21,
        "parent": 5,
        "title": "ROʼTM(Chinoz)ga xujjati rasmiylashtirilayotgan",
        "order": "2"
    },
    {
        "id": 22,
        "parent": 5,
        "title": "Profilaktik xisobda turgan",
        "order": "3"
    },
    {
        "id": 23,
        "parent": 6,
        "title": "Qidiruvda bo'lgan",
        "order": "1"
    },
]

for reason in sub_reason_bringning_children:
    item = SubReasonBringingChild(
        pk=reason['id'],
        parent_id=reason['parent'],
        title=reason['title'],
        order=reason['order'],
    )
    item.save()
    print('sub_reason_bringning_child successfully added')