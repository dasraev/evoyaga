# Generated by Django 3.2.9 on 2022-12-28 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0007_notification_rejection_reason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='rejection_reason',
        ),
    ]
