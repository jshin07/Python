# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 14:37
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='users',
            managers=[
                ('usersManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
