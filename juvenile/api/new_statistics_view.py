from rest_framework import generics
from . import new_statistics_serializers
from juvenile import models
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework.permissions import AllowAny
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .new_statistics_serializers import *




class LastAcceptedJuvenilesView(generics.ListAPIView):
    serializer_class = new_statistics_serializers.JuvenileMarkazSerializer
    # authentication_classes = []  # Disable authentication
    # permission_classes = [AllowAny]  # Allow any permission for testing

    def get_queryset(self):
        now = timezone.now()
        start_datetime = timezone.datetime(now.year, now.month, now.day - 2 , 19, 0, 0)
        # start_datetime = timezone.datetime(now.year, now.month, now.day - 10 , 19, 0, 0)
        end_datetime = timezone.datetime(now.year, now.month, now.day - 1, 19, 0, 0)
        # end_datetime = timezone.datetime(now.year, now.month, now.day, 19, 0, 0)
        juvenile_markazs = models.Juvenile_Markaz.objects.filter(
            Q(status__in=['2','3','4','5','6','7','8','9','11','12','13'])
            & Q(accept_center_info__created_at__range=[start_datetime, end_datetime])
        ).order_by('-created_at')
        return juvenile_markazs


