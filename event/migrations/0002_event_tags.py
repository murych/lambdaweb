# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('team', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='team.Tag',
                                    verbose_name='Тэги'),
        ),
    ]
