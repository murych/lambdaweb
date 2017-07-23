# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-23 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='description',
            field=models.CharField(blank=True, help_text='Используется в описании на странице "участники"', max_length=300, null=True, verbose_name='Описание'),
        ),
    ]
