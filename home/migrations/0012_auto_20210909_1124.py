# Generated by Django 3.2.6 on 2021-09-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210907_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen_details',
            name='date',
            field=models.DateField(default='1111-11-11'),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Name',
            field=models.CharField(default='NA', max_length=122),
        ),
    ]