# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20170208_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crpdate',
            name='job',
        ),
        migrations.AddField(
            model_name='company',
            name='crpdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='CRPDate',
        ),
    ]
