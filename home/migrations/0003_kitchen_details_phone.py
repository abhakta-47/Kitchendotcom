# Generated by Django 3.2.7 on 2021-10-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_kitchen_details_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen_details',
            name='Phone',
            field=models.CharField(default='NA', max_length=12),
        ),
    ]
