# Generated by Django 3.2.7 on 2021-10-12 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_kitchen_details_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen_details',
            name='Status',
            field=models.CharField(choices=[('New', 'New'), ('Follow Up', 'Follow Up'), ('Project Started', 'Project Started'), ('Project Completed', 'Project Completed'), ('Declined', 'Declined')], default='New', max_length=50),
        ),
    ]
