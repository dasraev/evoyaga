# Generated by Django 3.2.9 on 2022-12-08 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_litsey'),
        ('juvenile', '0004_educationinfojuvenile_special_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationinfojuvenile',
            name='litsey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.litsey'),
        ),
    ]
