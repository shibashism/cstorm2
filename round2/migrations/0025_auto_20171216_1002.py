# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-16 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('round2', '0024_auto_20171216_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='user',
        ),
        migrations.AddField(
            model_name='score',
            name='user_f',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='round2.User'),
        ),
    ]