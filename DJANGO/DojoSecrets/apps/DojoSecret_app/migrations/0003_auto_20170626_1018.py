# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DojoSecret_app', '0002_auto_20170625_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='secrets',
            old_name='creator',
            new_name='user_id',
        ),
        migrations.RemoveField(
            model_name='secrets',
            name='like',
        ),
        migrations.AddField(
            model_name='likes',
            name='secret_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DojoSecret_app.Secrets'),
        ),
        migrations.AddField(
            model_name='likes',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DojoSecret_app.Users'),
        ),
    ]