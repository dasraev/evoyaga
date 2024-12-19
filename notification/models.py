from django.db import models
from base.models import BaseModel
from config.settings import AUTH_USER_MODEL
from juvenile.models import Juvenile
from donation.models import Donation
from info.models import Markaz
from info.enums import NOTIFICATION_STATUS_CHOICE
from juvenile.models import PersonalInfoJuvenile

class Notification(BaseModel):
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='sender')
    receiver_markaz = models.ForeignKey(
        Markaz, on_delete=models.CASCADE, null=True, blank=True)
    juvenile = models.ForeignKey(Juvenile, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)
    status = models.CharField(
        max_length=1, choices=NOTIFICATION_STATUS_CHOICE, null=True)
    rejection_reason = models.TextField(
        max_length=10000, blank=True, null=True)

    class Meta:
        db_table = "notification"

    # def __str__(self):
    #     if self.sender and self.receiver_markaz:
    #         sender = f"Yuboruvchi: {self.sender.markaz.name}"
    #         receiver_markaz = f"Qabul qiluvchi: {self.receiver_markaz.name}"
    #         p_info = PersonalInfoJuvenile.objects.get(juvenile_id=self.juvenile_id)
    #         juvenile = f"Bola: { p_info.first_name } { p_info.last_name }"
    #         return f"{ sender } | { receiver_markaz } | { juvenile } | "
    #     return '-'


class DonationNotification(BaseModel):
    donation = models.ForeignKey(
        Donation, on_delete=models.CASCADE, null=True, blank=True)
    markaz = models.ForeignKey(
        Markaz, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'notification_donation'