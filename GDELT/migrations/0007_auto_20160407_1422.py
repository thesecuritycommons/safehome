# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GDELT', '0006_auto_20160407_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gkgcounts',
            name='cameoeventids',
            field=models.CommaSeparatedIntegerField(max_length=4096),
        ),
    ]
