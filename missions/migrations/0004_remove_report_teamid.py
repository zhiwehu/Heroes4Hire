# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-12 18:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0003_auto_20170112_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='teamID',
        ),
    ]
