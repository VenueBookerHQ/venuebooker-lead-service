# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-03 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0013_auto_20170403_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='venue',
            name='quoteImage',
            field=models.ImageField(blank=True, default='/static/images/vblogo.jpg', upload_to=b''),
        ),
    ]
