# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 23:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0006_auto_20160815_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 15, 1, 14, 49, 790277, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 14, 23, 14, 49, 790277, tzinfo=utc)),
        ),
    ]