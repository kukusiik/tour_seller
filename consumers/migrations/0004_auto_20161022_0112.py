# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 18:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0003_auto_20161022_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buying',
            name='consumer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
