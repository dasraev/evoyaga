import django_filters
from rest_framework.viewsets import ModelViewSet
from donation.models import Donation

from . import serializers
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django_filters import DateFilter, CharFilter
from rest_framework import status
from notification.api.views import send_donation_notification
from rest_framework.decorators import action
from juvenile.api.paginations import JuvenilePagination


class DonationFilter(filters.FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr=('gt'))
    end_date = DateFilter(field_name='date', lookup_expr=('lt'))
    name = CharFilter(method='search_by_name')

    class Meta:
        model = Donation
        fields = ['name', 'amount', 'markaz']

    def search_by_name(self, queryset, name, value):
        user_markaz = self.request.user.markaz
        return Donation.objects.filter(name__icontains=value).filter(markaz=user_markaz)


# Donation Viewset
class DonationViewset(ModelViewSet):
    def get_queryset(self):
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]
        user = self.request.user
        if user_code == 1:
            return Donation.objects.all()
        return Donation.objects.filter(markaz=user.markaz)
    filterset_class = DonationFilter
    pagination_class = JuvenilePagination

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.DonationCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.DonationUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.DonationListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.DonationDetailSerializer
        return serializer_class
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            donation = Donation.objects.create(
                created_by=request.user, markaz=request.user.markaz, **serializer.validated_data)
            # send_donation_notification(donation, request.user)
            return Response({'message': f"{donation.amount} so'm miqdorida xayriya qo'shildi"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def total_amount(self, request, *args, **kwargs):
        group_codes = self.request.user.groups.values_list('code', flat=True)
        user_code = list(group_codes)[0]
        if user_code == 1:
            donations = Donation.objects.all()
        else:
            donations = Donation.objects.filter(markaz=request.user.markaz)
        total_amount = 0
        for donation in donations:
            total_amount += donation.amount
        return Response({'total_amount': f"{total_amount} so'm"})