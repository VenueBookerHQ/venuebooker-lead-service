# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-31 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_campaign',
            name='image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]