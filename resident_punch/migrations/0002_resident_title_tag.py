# Generated by Django 4.0 on 2021-12-21 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resident_punch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='title_tag',
            field=models.CharField(default='Resident Detail', max_length=100),
        ),
    ]
