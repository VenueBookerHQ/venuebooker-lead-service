# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-10 14:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0020_auto_20170410_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
