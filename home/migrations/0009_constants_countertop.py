# Generated by Django 3.2.6 on 2021-09-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210903_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='constants',
            name='countertop',
            field=models.CharField(default='0', max_length=12),
        ),
    ]
