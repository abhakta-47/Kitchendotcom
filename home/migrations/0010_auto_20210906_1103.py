# Generated by Django 3.2.6 on 2021-09-06 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_constants_countertop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kitchen_details',
            old_name='layout',
            new_name='Type',
        ),
        migrations.RemoveField(
            model_name='constants',
            name='asacrylic',
        ),
        migrations.RemoveField(
            model_name='constants',
            name='basic_accessories',
        ),
        migrations.RemoveField(
            model_name='constants',
            name='bwpply',
        ),
        migrations.RemoveField(
            model_name='constants',
            name='bwrply',
        ),
        migrations.RemoveField(
            model_name='constants',
            name='glossypu',
        ),
        migrations.RemoveField(
            model_name='constants',
            name='hdhmr',
        ),
        migrations.RemoveField(
            model_name='constants',
            name='intermediate_accessories',
        ),
        migrations.RemoveField(
            model_name='constants',
            name='laminate',
        ),
        migrations.RemoveField(
            model_name='constants',
            name='mrply',
        ),
        migrations.RemoveField(
            model_name='constants',
            name='premium_accessories',
        ),
        migrations.RemoveField(
            model_name='constants',
            name='pvclaminate',
        ),
        migrations.RemoveField(
            model_name='kitchen_details',
            name='cal',
        ),
        migrations.RemoveField(
            model_name='kitchen_details',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='kitchen_details',
            name='loft',
        ),
        migrations.AddField(
            model_name='kitchen_details',
            name='Appliances',
            field=models.TextField(default='0', max_length=32),
        ),
        migrations.AddField(
            model_name='kitchen_details',
            name='Loft',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AddField(
            model_name='kitchen_details',
            name='Price',
            field=models.CharField(default='0', max_length=12),
        ),
        migrations.AddField(
            model_name='kitchen_details',
            name='Services',
            field=models.TextField(default='0', max_length=32),
        ),
        migrations.AddField(
            model_name='kitchen_details',
            name='Size',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='calculation',
        ),
    ]