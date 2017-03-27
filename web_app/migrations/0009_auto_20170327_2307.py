# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-27 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0008_eventimage_venueimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='hi', max_length=30, verbose_name='last name'),
            preserve_default=False,
        ),
    ]