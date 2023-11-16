from info.models import ReasonBringingChild

reason_bringning_children = [
    {
        "id": "1",
        "title": "Nаzorаtsiz qolgаn",
        "order": "1"
    },
    {
        "id": "2",
        "title": "Qаrovsiz qolgаn",
        "order": "2"
    },
    {
        "id": "3",
        "title": "Dаvlаt vа jаmoаtchilik yordаmigа muxtoj boʼlgаn",
        "order": "3"
    },
    {
        "id": "4",
        "title": "Ijtimoiy jixаtdаn xаvfli аhvoldаgi oilаlаrdа yashаyotgаn",
        "order": "4"
    },
    {
        "id": "5",
        "title": "Tаrbiyasi ogʼir boʼlgаn bolа",
        "order": "5"
    },
    {
        "id": "6",
        "title": "Bedаrаk yoʼqolgаn vа qidiruvdа boʼlgаn bolа",
        "order": "6"
    }
    
]

for reason in reason_bringning_children:
    item = ReasonBringingChild(
        id=reason['id'],
        title=reason['title'],
        order=reason['order'],
    )
    item.save()
    print('reason_bringning_child successfully added')