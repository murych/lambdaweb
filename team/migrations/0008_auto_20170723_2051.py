# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-23 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_member_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='description',
            field=models.CharField(blank=True, default='', help_text='Используется в описании на странице "участники"', max_length=300, verbose_name='Описание'),
        ),
    ]