# Generated by Django 3.2.9 on 2022-12-20 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0002_rename_is_seen_notification_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='receiver',
        ),
        migrations.CreateModel(
            name='Notification_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='notification.notification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'notification_user',
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_user',
            field=models.ManyToManyField(blank=True, through='notification.Notification_User', to=settings.AUTH_USER_MODEL),
        ),
    ]
