# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0012_auto_20161010_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='images/tours/', verbose_name='Изображение тура'),
        ),
    ]