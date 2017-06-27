# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DojoSecret_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='secrets',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DojoSecret_app.Users'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='secrets',
            name='like',
            field=models.ManyToManyField(related_name='whatisthis', to='DojoSecret_app.Users'),
        ),
    ]