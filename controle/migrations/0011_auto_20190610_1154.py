# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-06-10 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0010_auto_20181020_2305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarefas',
            options={'verbose_name': 'Tarefa', 'verbose_name_plural': 'Tarefas'},
        ),
    ]