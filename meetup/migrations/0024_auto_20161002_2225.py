# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-02 20:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0023_auto_20160824_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 2, 20, 25, 18, 182338, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 2, 22, 25, 18, 182338, tzinfo=utc)),
        ),
    ]