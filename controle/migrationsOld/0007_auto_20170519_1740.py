# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0006_auto_20170519_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpod',
            old_name='data_des_fim',
            new_name='data_d_fim',
        ),
        migrations.RenameField(
            model_name='cpod',
            old_name='data_des_ini',
            new_name='data_d_ini',
        ),
    ]
