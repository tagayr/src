# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-02 21:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0026_auto_20161002_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 2, 21, 35, 44, 212429, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 2, 23, 35, 44, 212429, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='participant',
            name='participant_message',
            field=models.CharField(default='', max_length=200),
        ),
    ]