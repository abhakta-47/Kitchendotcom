# Generated by Django 3.2.7 on 2021-10-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogandnews', '0006_auto_20210930_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='post',
            new_name='blog',
        )
    ]