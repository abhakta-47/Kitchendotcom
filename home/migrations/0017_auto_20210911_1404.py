# Generated by Django 3.2.6 on 2021-09-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_kitchen_details_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('essentials', models.CharField(default='NA', max_length=12)),
                ('premium', models.CharField(default='NA', max_length=12)),
                ('luxe', models.CharField(default='NA', max_length=12)),
                ('countertop', models.CharField(default='NA', max_length=12)),
                ('HDHMR', models.CharField(default='NA', max_length=12)),
                ('MR_Plywood', models.CharField(default='NA', max_length=12)),
                ('BWR_Plywood', models.CharField(default='NA', max_length=12)),
                ('BWP_Plywood', models.CharField(default='NA', max_length=12)),
                ('Laminate', models.CharField(default='NA', max_length=12)),
                ('PVC_Laminate', models.CharField(default='NA', max_length=12)),
                ('Anti_scratch_Acrylic', models.CharField(default='NA', max_length=12)),
                ('Glossy_PU', models.CharField(default='NA', max_length=12)),
                ('Basic_Acc', models.CharField(default='NA', max_length=12)),
                ('Intermediate_Acc', models.CharField(default='NA', max_length=12)),
                ('Prem_Acc', models.CharField(default='NA', max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='Constants',
        ),
        migrations.AddField(
            model_name='kitchen_details',
            name='Location',
            field=models.CharField(default='NA', max_length=12),
        ),
    ]
