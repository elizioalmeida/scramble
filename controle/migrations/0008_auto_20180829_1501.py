# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-29 18:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0007_auto_20180828_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdesenvolvimento',
            name='participacao',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)], verbose_name=b'%'),
        ),
        migrations.AlterField(
            model_name='cpod',
            name='participacao',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name=b'Participa\xc3\xa7\xc3\xa3o(%)'),
        ),
        migrations.AlterField(
            model_name='cpod',
            name='status',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name=b'Progresso (%)'),
        ),
    ]
