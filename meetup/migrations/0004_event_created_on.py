# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 19:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0003_auto_20160814_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 14, 19, 57, 58, 724600, tzinfo=utc)),
        ),
    ]
