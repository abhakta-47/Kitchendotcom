# Generated by Django 3.2.6 on 2021-09-13 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_city1_city10_city2_city3_city4_city5_city6_city7_city8_city9'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constant',
            old_name='essentials',
            new_name='Essentials',
        ),
        migrations.RenameField(
            model_name='constant',
            old_name='luxe',
            new_name='Luxe',
        ),
        migrations.RenameField(
            model_name='constant',
            old_name='premium',
            new_name='Premium',
        ),
    ]