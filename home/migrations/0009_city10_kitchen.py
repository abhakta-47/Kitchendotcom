# Generated by Django 3.2.7 on 2021-10-09 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211009_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='city10',
            name='kitchen',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details'),
        ),
    ]
