# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_remove_job_required_data_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='readable_degree',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='readable_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]