# Generated by Django 3.2.9 on 2023-02-27 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_markaztuman'),
        ('juvenile', '0023_alter_juvenile_markaz_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='juvenile_markaz',
            name='monitoring_markaz_tuman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='info.markaztuman'),
        ),
    ]
