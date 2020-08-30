# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by Django 1.11.21 on 2019-06-18 16:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20160311_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='reps',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(
                0), django.core.validators.MaxValueValidator(600)], verbose_name='Amount'),
        ),
    ]
