# Generated by Django 3.2.7 on 2021-10-09 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_city1_kitchen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city10',
            name='kitchen',
        ),
    ]