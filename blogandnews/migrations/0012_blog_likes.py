# Generated by Django 3.2.8 on 2021-10-15 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogandnews', '0011_auto_20211010_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]