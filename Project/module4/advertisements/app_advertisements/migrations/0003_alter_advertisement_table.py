# Generated by Django 4.2.4 on 2023-08-18 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0002_rename_advertisements_advertisement'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]
