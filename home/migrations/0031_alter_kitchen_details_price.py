# Generated by Django 3.2.7 on 2021-10-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20210930_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen_details',
            name='Price',
            field=models.CharField(default='NA', max_length=12),
        ),
    ]
