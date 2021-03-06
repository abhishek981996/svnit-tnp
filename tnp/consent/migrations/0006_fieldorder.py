# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20170208_1529'),
        ('consent', '0005_auto_20170207_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_order', to='consent.UserDataFields')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_order', to='company.Job')),
            ],
        ),
    ]
