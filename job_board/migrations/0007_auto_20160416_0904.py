# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0006_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]