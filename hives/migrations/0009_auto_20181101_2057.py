# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-01 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0008_auto_20181101_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firsthivedatamodel',
            name='owner',
        ),
        migrations.AddField(
            model_name='firsthivedatamodel',
            name='motherBee',
            field=models.BooleanField(default=False),
        ),
    ]
