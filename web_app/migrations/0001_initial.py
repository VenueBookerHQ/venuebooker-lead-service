# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-30 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('details', models.TextField(max_length=200)),
                ('name', models.TextField(max_length=200)),
                ('image', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]
