# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0011_auto_20160416_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
