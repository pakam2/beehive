# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-02 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0014_auto_20181102_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firsthivedatamodel',
            name='owner',
        ),
    ]