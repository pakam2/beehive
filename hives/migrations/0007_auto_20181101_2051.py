# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-01 19:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0006_auto_20181101_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firsthivedatamodel',
            name='motherBee',
        ),
        migrations.RemoveField(
            model_name='firsthivedatamodel',
            name='owner',
        ),
    ]
