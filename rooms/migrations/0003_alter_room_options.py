# Generated by Django 4.0.4 on 2022-05-04 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20220504_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-pk']},
        ),
    ]
