# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GDELT', '0020_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='Geo',
        ),
        migrations.RemoveField(
            model_name='event',
            name='FractionDate',
        ),
        migrations.RemoveField(
            model_name='event',
            name='Geo',
        ),
        migrations.RemoveField(
            model_name='event',
            name='MonthYear',
        ),
        migrations.RemoveField(
            model_name='event',
            name='Year',
        ),
        migrations.AddField(
            model_name='event',
            name='ActionGeo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ActionGeo', to='GDELT.Geo'),
        ),
        migrations.AddField(
            model_name='event',
            name='Actor1Geo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Actor1Geo+', to='GDELT.Geo'),
        ),
        migrations.AddField(
            model_name='event',
            name='Actor2Geo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Actor1Geo+', to='GDELT.Geo'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='Code',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.RemoveField(
            model_name='event',
            name='Actor1',
        ),
        migrations.AddField(
            model_name='event',
            name='Actor1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Actor1+', to='GDELT.Actor'),
        ),
        migrations.RemoveField(
            model_name='event',
            name='Actor2',
        ),
        migrations.AddField(
            model_name='event',
            name='Actor2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Actor2+', to='GDELT.Actor'),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventBaseCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EventBaseCode', to='GDELT.EventCode'),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EventCode', to='GDELT.EventCode'),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventRootCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EventRootCode', to='GDELT.EventCode'),
        ),
    ]
