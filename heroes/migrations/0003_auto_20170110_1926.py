# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-10 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0002_auto_20170110_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='powers',
            field=models.TextField(default='Please add powers'),
        ),
    ]
