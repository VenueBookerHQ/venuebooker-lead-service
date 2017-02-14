# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-14 16:29
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_venue_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('organisationID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='event_campaign',
            name='id',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='id',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='type',
        ),
        migrations.AddField(
            model_name='event_campaign',
            name='cost_per_capacity_unit',
            field=models.FloatField(default="0"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event_campaign',
            name='endTime',
            field=models.TimeField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event_campaign',
            name='eventID',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event_campaign',
            name='recurring',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event_campaign',
            name='startTime',
            field=models.TimeField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event_campaign',
            name='venue',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web_app.Venue'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='address',
            field=models.TextField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='socialmedialinks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, max_length=200), default=None, size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='venueID',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venue',
            name='organisation',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web_app.Organisation'),
            preserve_default=False,
        ),
    ]