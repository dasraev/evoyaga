# Generated by Django 3.2.9 on 2023-02-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_texnikum'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicallist',
            name='extra_id',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
