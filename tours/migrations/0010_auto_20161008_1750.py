# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_auto_20161008_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='images/', verbose_name='Изображение тура'),
        ),
    ]