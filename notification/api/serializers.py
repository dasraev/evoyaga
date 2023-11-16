from rest_framework.serializers import ModelSerializer, SerializerMethodField, SlugRelatedField
from notification.models import Notification, DonationNotification
from juvenile import models as juvenile_db
from info import enums


# Notification Serializer
class NotificationListSerializer(ModelSerializer):
    sender_center = SerializerMethodField()
    receiver_markaz = SlugRelatedField(slug_field='name', read_only=True)
    juvenile = SerializerMethodField()
    status = SerializerMethodField()

    class Meta:
        model = Notification
        fields = (
            'id',
            'sender_center',
            'receiver_markaz',
            'juvenile',
            'status',
            'completed',
            'created_at'
            )
    
    def get_sender_center(self, obj):
        return obj.sender.markaz.name

    def get_juvenile(self, obj):
        juvenile = obj.juvenile
        personal_info = juvenile_db.PersonalInfoJuvenile.objects.filter(
            juvenile=juvenile).order_by('-created_at').first()
        data = {
            "first_name": personal_info.first_name,
            "last_name": personal_info.last_name,
            "father_name": personal_info.father_name,
        }
        return data

    def get_status(self, obj):
        if obj.status != None:
            list = enums.NOTIFICATION_STATUS_CHOICE[int(obj.status) - 1]
            data = {
                "id": list[0],
                "text": list[1]
            }
            return data
        return None
        

class NotificationDetailSerializer(ModelSerializer):
    juvenile = SerializerMethodField()
    sender_center = SerializerMethodField()
    status = SerializerMethodField()

    class Meta:
        model = Notification
        fields = (
            'juvenile',
            'rejection_reason',
            'sender_center',
            'status',
        )

    def get_juvenile(self, obj):
        juvenile = obj.juvenile
        personal_info = juvenile_db.PersonalInfoJuvenile.objects.filter(
            juvenile=juvenile).order_by('-created_at').first()
        address_info = juvenile_db.AddressInfoJuvenile.objects.filter(
            juvenile=juvenile).order_by('-created_at').first()
        juvenile_markaz = juvenile_db.Juvenile_Markaz.objects.filter(
            juvenile=juvenile).order_by('-created_at').first()
        distribution_info = juvenile_markaz.distributed_info
        request = self.context.get("request")

        photo = None
        if personal_info.photo is not None:
            photo = request.build_absolute_uri(personal_info.photo.url)
        
        center_opinion_file = None
        if distribution_info is not None:
            if distribution_info.center_opinion_file is not None:
                center_opinion_file = request.build_absolute_uri(
                    distribution_info.center_opinion_file.url)
            

        data = {
            "photo": photo,
            "first_name": personal_info.first_name,
            "last_name": personal_info.last_name,
            "father_name": personal_info.father_name,
            "gender": personal_info.gender,
            "birth_date": personal_info.birth_date,
            "birth_region": personal_info.birth_district.region_id.name,
            "address": address_info.address,
            "center_opinion_file": center_opinion_file,
        }
        return data

    def get_sender_center(self, obj):
        return obj.sender.markaz.name
    
    def get_status(self, obj):
        if obj.status != None:
            list = enums.NOTIFICATION_STATUS_CHOICE[int(obj.status) - 1]
            data = {
                "id": list[0],
                "text": list[1]
            }
            return data


class NotificationUpdateSerializer(ModelSerializer):
    class Meta:
        model = Notification
        exclude = ('created_by', 'updated_by')


class NotificationCreateSerializer(ModelSerializer):
    class Meta:
        model = Notification
        exclude = ('created_by', 'updated_by')


class RejectJuvenileSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('rejection_reason', )


# Donation notification
class DonationNotificationListSerializer(ModelSerializer):
    donation = SerializerMethodField()
    markaz = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = DonationNotification
        fields = (
            'id',
            'donation',
            'markaz',
            'completed',
            'created_at'
        )

    def get_donation(self, obj):
        donation = obj.donation
        return {
            "name": donation.name,
            "amount": donation.amount
        }
