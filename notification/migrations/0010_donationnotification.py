# Generated by Django 3.2.9 on 2023-01-26 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0003_donation_markaz'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info', '0009_texnikum'),
        ('notification', '0009_notification_rejection_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationNotification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notification_donationnotification_created_by', to=settings.AUTH_USER_MODEL)),
                ('juvenile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='donation.donation')),
                ('markaz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.markaz')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notification_donationnotification_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'notification_donation',
            },
        ),
    ]
