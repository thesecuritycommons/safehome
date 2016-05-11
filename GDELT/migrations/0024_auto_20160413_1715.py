# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GDELT', '0023_auto_20160413_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geo',
            name='Lat',
        ),
        migrations.RemoveField(
            model_name='geo',
            name='Long',
        ),
        migrations.AlterField(
            model_name='geo',
            name='FullName',
            field=models.CharField(default='', max_length=512, unique=True),
            preserve_default=False,
        ),
    ]