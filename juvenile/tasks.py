# myapp/tasks.py
from celery import shared_task
from juvenile.api import serializers
from . import models
from django.utils import timezone
from django.db.models import Q
import requests



@shared_task
def get_last_juveniles():
    now = timezone.now()
    # start_datetime = timezone.datetime(now.year, now.month, now.day - 2 , 19, 0, 0)
    start_datetime = timezone.datetime(now.year, now.month, now.day - 1)
    # end_datetime = timezone.datetime(now.year, now.month, now.day - 1, 19, 0, 0)
    end_datetime = timezone.datetime(now.year, now.month, now.day)
    juvenile_markazs = models.Juvenile_Markaz.objects.filter(
        Q(status__in=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])
        & Q(accept_center_info__arrived_date__range=[start_datetime, end_datetime])
    ).distinct().order_by('-created_at')
    serializer = serializers.JuvenileMarkazSerializer(juvenile_markazs, many=True)
    serialized_data = serializer.data
    # for item in serialized_data:
    #     for key, value in item.items():
    #         if isinstance(value, timezone.datetime):
    #             item[key] = value.isoformat()
    # url = 'http://10.190.33.186:7277/api/receive_data/test'
    # headers = {'Content-Type': 'application/json'}
    # requests.post(url, json=serialized_data, headers=headers)
    for item in serialized_data:
        for key, value in item.items():
            if isinstance(value, timezone.datetime):
                item[key] = value.isoformat()
    url = 'http://10.190.33.186:7277/api/receive_data/minors'
    headers = {'Content-Type': 'application/json'}
    proxies = [
        {"http": 'http://e-voyagayetmaganlar.iiv.uz:8000'}
    ]
    requests.post(url, json=serialized_data, headers=headers)
