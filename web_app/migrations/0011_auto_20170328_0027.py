# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-28 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0010_auto_20170327_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web_app.Contact'),
        ),
    ]
