# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0004_auto_20161022_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='buying',
            name='visibility',
            field=models.BooleanField(default=True),
        ),
    ]
