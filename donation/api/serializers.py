from donation.models import Donation
from rest_framework.serializers import ModelSerializer


# Donation Serializer
class DonationListSerializer(ModelSerializer):
    class Meta:
        model = Donation
        exclude = ('created_by', 'updated_by',)


class DonationDetailSerializer(ModelSerializer):
    class Meta:
        model = Donation
        exclude = ('created_by', 'updated_by')


class DonationUpdateSerializer(ModelSerializer):
    class Meta:
        model = Donation
        exclude = ('created_by', 'updated_by')


class DonationCreateSerializer(ModelSerializer):
    class Meta:
        model = Donation
        exclude = ('created_by', 'updated_by')
