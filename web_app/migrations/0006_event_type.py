# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-28 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_enquiry_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=40)),
                ('description', models.TextField(max_length=500)),
                ('active', models.BooleanField()),
                ('seasonal', models.BooleanField()),
            ],
        ),
    ]