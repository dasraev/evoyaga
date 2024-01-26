from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
from notification.models import Notification, DonationNotification
from rest_framework.viewsets import ModelViewSet
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from juvenile import models as juvenile_db
from rest_framework import status, generics
from rest_framework.generics import RetrieveAPIView


class NotificationViewset(ModelViewSet):
    def get_queryset(self):
        user_markaz = self.request.user.markaz

        notifications = Notification.objects.filter(receiver_markaz=user_markaz).filter(completed=False).order_by(
            '-created_at')
        # notifications = Notification.objects.filter(receiver_markaz=user_markaz).order_by(
        #     '-created_at')
        return notifications

    def get_serializer_class(self):
        if self.action in ['create']:
            serializer_class = serializers.NotificationCreateSerializer
        if self.action in ['update', 'partial_update']:
            serializer_class = serializers.NotificationUpdateSerializer
        elif self.action in ['list']:
            serializer_class = serializers.NotificationListSerializer
        elif self.action in ['retrieve', 'delete']:
            serializer_class = serializers.NotificationDetailSerializer
        return serializer_class

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        notification = get_object_or_404(queryset, pk=pk)
        serializer = serializers.NotificationDetailSerializer(
            notification, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def complete_notification(self, request, pk=None):
        notification = Notification.objects.get(pk=pk)
        notification.completed = True
        notification.save()

        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)(
        #     'notification_group', {
        #         'type': 'send_notification'
        #     }
        # )

        return Response({'message': 'Bildirishnoma yakunlandi!'})

    @action(detail=True, methods=['post'])
    def accept_juvenile(self, request, pk=None):
        notification = Notification.objects.get(pk=pk)
        user = request.user
        personal_info = juvenile_db.PersonalInfoJuvenile.objects.filter(
            juvenile=notification.juvenile).order_by('-created_at').first()

        juvenile_markaz = juvenile_db.Juvenile_Markaz.objects.filter(
            markaz=notification.sender.markaz).filter(
            juvenile=notification.juvenile).order_by('-created_at').first()


        juvenile_markaz.status = 8
        notification.juvenile.current_markaz = user.markaz
        notification.juvenile.save()
        juvenile_markaz.save()

        

        juvenile_db.Juvenile_Markaz.objects.create(juvenile=notification.juvenile, markaz=user.markaz, status=1)
        notification.juvenile.current_markaz = user.markaz

        Notification.objects.create(
            sender=user, 
            receiver_markaz=notification.sender.markaz,
            juvenile=notification.juvenile, 
            status=2,
        )

        notification.completed = True
        notification.save()

        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)(
        #     'notification_group', {
        #         'type': 'send_notification'
        #     }
        # )
        juvenile_name = f'{personal_info.last_name} {personal_info.first_name} {personal_info.father_name}'
        return Response({'message': f'{juvenile_name} muvaffaqqiyatli qabul qilindi!'})

    @action(detail=True, methods=['post'])
    def reject_juvenile(self, request, pk=None):
        serializer = serializers.RejectJuvenileSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            rejection_reason = serializer._validated_data.get('rejection_reason')
            user = request.user
            notification = Notification.objects.get(pk=pk)

            personal_info = juvenile_db.PersonalInfoJuvenile.objects.filter(
                juvenile=notification.juvenile).order_by('-created_at').first()
            
            juvenile_markaz = juvenile_db.Juvenile_Markaz.objects.filter(
                markaz=notification.sender.markaz).filter(
                juvenile=notification.juvenile).order_by('-created_at').first()

            juvenile_markaz.distributed_info = None
            juvenile_markaz.status = 2
            juvenile_markaz.save()

            Notification.objects.create(
                sender=user, 
                receiver_markaz=notification.sender.markaz,
                juvenile=notification.juvenile, 
                status=3,
                rejection_reason=rejection_reason
            )

            notification.completed = True
            notification.save()

            # channel_layer = get_channel_layer()
            # async_to_sync(channel_layer.group_send)(
            #     'notification_group', {
            #         'type': 'send_notification'
            #     }
            # )

            juvenile_name = f'{personal_info.last_name} {personal_info.first_name} {personal_info.father_name}'
            return Response({'message': f'{juvenile_name} rad etildi va yuboruvchi markazga qaytarildi!'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

#Taqsimot asosida taqsimot turi boshqa markazga yuborish tanlansa shu method ishlatiladi
def send_notification_other_center(juvenile, user, reciever_center):
    Notification.objects.create(
        sender=user, receiver_markaz=reciever_center, juvenile=juvenile, status=1)

    # channel_layer = get_channel_layer()
    # async_to_sync(channel_layer.group_send)(
    #     'notification_group', {
    #         'type': 'send_notification'
    #     } 
    # )


class DonationNotificationListAPIView(generics.ListCreateAPIView):
    def get_queryset(self):

        donation_notification = DonationNotification.objects.filter(markaz=self.request.user.markaz).filter(completed=False).order_by(
            '-created_at')
        return donation_notification
    serializer_class = serializers.DonationNotificationListSerializer


class DonationNotificationDetailAPIView(RetrieveAPIView):
    queryset = DonationNotification.objects.all()
    serializer_class = serializers.DonationNotificationListSerializer
    def retrieve(self, request, pk=None):
        instance = DonationNotification.objects.get(pk=pk)
        instance.completed = True
        instance.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notification_group', {
                'type': 'send_donation_notification'
            }
        )
        return Response({'message': 'Bildirishnoma yakunlandi'})
        
#Xayriya qo'shilganda chiqadigan xabarnoma
def send_donation_notification(donation, user):
    DonationNotification.objects.create(markaz=user.markaz, donation=donation, created_by=user)

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'notification_group', {
            'type': 'send_donation_notification'
        }
    )
