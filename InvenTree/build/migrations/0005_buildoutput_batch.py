# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0004_auto_20180417_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildoutput',
            name='batch',
            field=models.CharField(blank=True, help_text='Batch code for this build output', max_length=100),
        ),
    ]