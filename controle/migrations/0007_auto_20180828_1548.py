# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-28 18:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0006_auto_20180828_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdesenvolvimento',
            name='status',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name=b'Progresso'),
        ),
    ]
