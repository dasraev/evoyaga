# Generated by Django 3.2.9 on 2022-12-16 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juvenile', '0008_educationinfojuvenile_texnikum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juvenile_markaz',
            name='status',
            field=models.CharField(choices=[(1, 'Aniqlangan'), (2, 'Markazga qabul qilingan'), (3, 'Taqsimlangan'), (4, 'Monitoring jarayonida'), (5, 'Bandlik ta’minlanish jarayonida'), (6, 'Bandligi taminlangan'), (7, 'Boshqa davlatga yuborilgan'), (8, 'Boshqa markazga yuborilgan'), (9, 'Arxixda')], default=None, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='juvenileacceptcenterinfo',
            name='arrived_reason',
            field=models.CharField(choices=[(1, 'IIB qarori'), (1, 'Sud ajrimi'), (3, "Markaz buyrug'i")], default=None, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='juveniledistributedinfo',
            name='type_guardianship',
            field=models.CharField(choices=[(1, 'Vasiy'), (2, 'Homiy'), (3, 'Patronat'), (4, 'Farzandlik'), (5, 'Mehribonlik uyi'), (6, 'Oilaviy bolalar uyi'), (7, 'SOS bolalar shaharchasi')], default=None, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfojuvenile',
            name='passport_type',
            field=models.CharField(choices=[(1, 'Biometrik pasport'), (2, 'ID-karta'), (3, "Tug'ilganlik haqida guvohnoma"), (4, 'Kinder pasport'), (5, 'Horijiy davlat hujjatlari'), (6, 'Boshqalar')], max_length=30, null=True),
        ),
    ]
