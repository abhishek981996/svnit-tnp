# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent', '0017_auto_20170416_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetail',
            name='current_pincode',
            field=models.CharField(blank=True, default='395007', max_length=6, null=True),
        ),
    ]
