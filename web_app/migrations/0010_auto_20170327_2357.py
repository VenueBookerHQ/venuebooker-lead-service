# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-27 23:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0009_auto_20170327_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
