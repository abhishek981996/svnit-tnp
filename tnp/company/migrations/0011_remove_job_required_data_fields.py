# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20170211_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='required_data_fields',
        ),
    ]
