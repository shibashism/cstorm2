# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-16 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round2', '0017_remove_user_buyed_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(default='Easy', max_length=10),
        ),
    ]