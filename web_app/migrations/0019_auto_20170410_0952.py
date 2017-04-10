# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-10 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0018_auto_20170410_0939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactresponse',
            options={'verbose_name': 'Contact Form Response', 'verbose_name_plural': 'My Contact Form Responses'},
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'User Account', 'verbose_name_plural': 'My User Accounts'},
        ),
        migrations.AlterModelOptions(
            name='enquiry',
            options={'verbose_name': 'Enquiry', 'verbose_name_plural': 'My Enquiries'},
        ),
        migrations.AlterModelOptions(
            name='event_campaign',
            options={'verbose_name': 'Event Campaign', 'verbose_name_plural': 'My Event Campaigns'},
        ),
        migrations.AlterModelOptions(
            name='event_type',
            options={'verbose_name': 'Event Type', 'verbose_name_plural': 'My Event Types'},
        ),
        migrations.AlterModelOptions(
            name='eventimage',
            options={'verbose_name': 'Event Campaign Image', 'verbose_name_plural': "My Event Campaign's Images"},
        ),
        migrations.AlterModelOptions(
            name='organisation',
            options={'verbose_name': 'Event Campaign Image', 'verbose_name_plural': "My Event Campaign's Images"},
        ),
        migrations.AlterModelOptions(
            name='organisationuser',
            options={'verbose_name': 'Organisation User', 'verbose_name_plural': 'My Organisation Users'},
        ),
        migrations.AlterModelOptions(
            name='quote',
            options={'verbose_name': 'Quote', 'verbose_name_plural': 'My Quotes'},
        ),
        migrations.AlterModelOptions(
            name='venue',
            options={'verbose_name': 'Venue', 'verbose_name_plural': 'My Venues'},
        ),
        migrations.AlterModelOptions(
            name='venueimage',
            options={'verbose_name': 'Venue Image', 'verbose_name_plural': "My Venue's Images"},
        ),
        migrations.AlterModelOptions(
            name='venueuser',
            options={'verbose_name': 'Venue User', 'verbose_name_plural': 'My Venue Users'},
        ),
    ]
