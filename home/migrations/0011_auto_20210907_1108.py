# Generated by Django 3.2.6 on 2021-09-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210906_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen_details',
            name='Name',
            field=models.CharField(default='NA', max_length=122),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='constants',
            name='countertop',
            field=models.CharField(default='NA', max_length=12),
        ),
        migrations.AlterField(
            model_name='constants',
            name='essentials',
            field=models.CharField(default='NA', max_length=12),
        ),
        migrations.AlterField(
            model_name='constants',
            name='luxe',
            field=models.CharField(default='NA', max_length=12),
        ),
        migrations.AlterField(
            model_name='constants',
            name='premium',
            field=models.CharField(default='NA', max_length=12),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Accessories',
            field=models.CharField(default='NA', max_length=12),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Appliances',
            field=models.TextField(default='NA', max_length=32),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Countertop',
            field=models.CharField(default='NA', max_length=12),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Finish',
            field=models.CharField(default='NA', max_length=12),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Loft',
            field=models.CharField(default='NA', max_length=12),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Material',
            field=models.CharField(default='NA', max_length=12),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Price',
            field=models.CharField(default='NA', max_length=12),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Services',
            field=models.TextField(default='NA', max_length=32),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Shape',
            field=models.CharField(default='NA', max_length=12),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Size',
            field=models.CharField(default='NA', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='kitchen_details',
            name='Type',
            field=models.CharField(default='NA', max_length=30),
        ),
    ]
