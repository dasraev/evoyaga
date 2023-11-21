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
import csv
from django.http import HttpResponse



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




class JuvenileNoEducationListView(generics.ListAPIView):
    # permission_classes = [AllowAny]  # Allow any permission for testing

    serializer_class = new_statistics_serializers.JuvenileNoEducationListSerializer

    def get_queryset(self):
        juveniles_no_education = models.PersonalInfoJuvenile.objects.filter(juvenile__educationinfojuvenile__school_type__in=['9','10'])
        return juveniles_no_education


    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Create a response object with CSV content
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="juvenile_no_education.csv"'

        # Create a CSV writer
        csv_writer = csv.writer(response)

        # Write header
        header = JuvenileNoEducationListSerializer().fields.keys()
        csv_writer.writerow(header)

        # Write data
        for juvenile in queryset:
            serializer = JuvenileNoEducationListSerializer(juvenile,context={'request': request})
            row = [serializer.data[field] for field in header]
            csv_writer.writerow(row)

        return response
