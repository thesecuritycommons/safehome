# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GDELT', '0011_gdeltfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='gdeltfiles',
            name='imported',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gdeltfiles',
            name='md5',
            field=models.CharField(default='.', max_length=256),
            preserve_default=False,
        ),
    ]