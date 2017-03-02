# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-02 20:37
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('surname', models.CharField(max_length=30, verbose_name='surname')),
                ('telephone', models.CharField(blank=True, max_length=15, verbose_name='telephone')),
                ('mobile', models.CharField(blank=True, max_length=15, verbose_name='mobile')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('attendeeNum', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Event_campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=200)),
                ('name', models.TextField(max_length=200)),
                ('startTime', models.TimeField(blank=True)),
                ('endTime', models.TimeField(blank=True)),
                ('recurring', models.BooleanField()),
                ('image', models.FileField(upload_to=b'')),
                ('capacity', models.IntegerField()),
                ('cost_per_capacity_unit', models.FloatField()),
            ],
        ),
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
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('address', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationAdmin',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.Organisation')),
            ],
            options={
                'ordering': ['name'],
                'permissions': (('access_group_list', 'Can access group list'), ('access_group', 'Can access group')),
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='OrganisationUser',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.Organisation')),
            ],
            options={
                'ordering': ['name'],
                'permissions': (('access_group_list', 'Can access group list'), ('access_group', 'Can access group')),
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('cost', models.FloatField()),
                ('accepted', models.BooleanField()),
                ('enquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.Enquiry')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('socialmedialinks', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, max_length=200), size=None)),
                ('description', models.TextField(max_length=200)),
                ('image', models.FileField(upload_to=b'')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='VenueAdmin',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.Venue')),
            ],
            options={
                'ordering': ['name'],
                'permissions': (('access_group_list', 'Can access group list'), ('access_group', 'Can access group')),
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='VenueUser',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.Venue')),
            ],
            options={
                'ordering': ['name'],
                'permissions': (('access_group_list', 'Can access group list'), ('access_group', 'Can access group')),
            },
            bases=('auth.group',),
        ),
        migrations.AddField(
            model_name='event_campaign',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.Event_type'),
        ),
        migrations.AddField(
            model_name='event_campaign',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.Venue'),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='event_campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.Event_campaign'),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, null=True, to='web_app.Contact'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
