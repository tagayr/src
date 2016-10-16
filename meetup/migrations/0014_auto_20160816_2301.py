# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-16 21:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0013_auto_20160816_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 16, 21, 1, 20, 17679, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 16, 23, 1, 20, 17679, tzinfo=utc)),
        ),
    ]