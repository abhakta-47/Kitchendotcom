# Generated by Django 3.2.6 on 2021-08-28 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210828_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kitchen_details',
            old_name='calculation',
            new_name='cal',
        ),
    ]