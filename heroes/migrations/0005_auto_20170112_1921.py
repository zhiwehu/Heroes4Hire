# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-12 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0004_auto_20170112_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='missionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='missions.Mission'),
        ),
    ]
