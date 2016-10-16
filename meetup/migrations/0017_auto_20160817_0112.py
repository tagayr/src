# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 23:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0016_auto_20160817_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 16, 23, 12, 5, 409928, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 17, 1, 12, 5, 410428, tzinfo=utc)),
        ),
    ]
