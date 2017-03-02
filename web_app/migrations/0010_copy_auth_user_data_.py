# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-02 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(DataMigration):
    def forwards(self, orm):
        "Write your forwards methods here."
        for old_u in orm['auth.User'].objects.all():
            new_u = orm.CustomUser.objects.create(
                        date_joined=old_u.date_joined,
                        username=old_u.username,
                        email=old_u.email,
                        first_name=old_u.first_name,
                        id=old_u.id,
                        is_active=old_u.is_active,
                        is_staff=old_u.is_staff,
                        is_superuser=old_u.is_superuser,
                        last_login=old_u.last_login,
                        last_name=old_u.last_name,
                        password=old_u.password)
            for perm in old_u.user_permissions.all():
                new_u.user_permissions.add(perm)
            for group in old_u.groups.all():
                new_u.groups.add(group)