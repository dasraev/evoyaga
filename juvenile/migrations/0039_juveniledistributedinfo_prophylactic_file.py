# Generated by Django 3.2.9 on 2024-12-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juvenile', '0038_auto_20240728_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='juveniledistributedinfo',
            name='prophylactic_file',
            field=models.FileField(blank=True, null=True, upload_to='prophylactic_file'),
        ),
    ]
