# Generated by Django 3.2.9 on 2022-12-21 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_auto_20221220_0613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='receiver',
            new_name='receiver_markaz',
        ),
    ]
