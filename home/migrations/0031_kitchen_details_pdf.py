# Generated by Django 3.2.7 on 2021-10-02 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20210930_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen_details',
            name='pdf',
            field=models.FileField(default='NA', upload_to='detaispdf'),
        ),
    ]