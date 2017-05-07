# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-07 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0026_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='nearest_transport_link',
            field=models.CharField(default='1 mile', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='postcode',
            field=models.CharField(default='ABC 123', max_length=10),
            preserve_default=False,
        ),
    ]
