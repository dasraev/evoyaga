# Generated by Django 3.2.9 on 2022-12-20 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_texnikum'),
        ('notification', '0003_auto_20221220_0558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='notification_user',
        ),
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.markaz'),
        ),
        migrations.DeleteModel(
            name='Notification_User',
        ),
    ]
