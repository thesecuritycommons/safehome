# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 23:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GDELT', '0018_ethnicgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ethnicgroup',
            name='label',
            field=models.CharField(max_length=256),
        ),
    ]
