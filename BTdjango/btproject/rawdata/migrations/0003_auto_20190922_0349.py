# Generated by Django 2.2.5 on 2019-09-22 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rawdata', '0002_auto_20190922_0346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Priority',
            new_name='CITY_STATE',
        ),
    ]
