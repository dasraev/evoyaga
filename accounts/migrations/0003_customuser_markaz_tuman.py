# Generated by Django 3.2.9 on 2023-02-22 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0013_markaztuman'),
        ('accounts', '0002_customuser_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='markaz_tuman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='markaz_tuman', to='info.markaztuman'),
        ),
    ]
