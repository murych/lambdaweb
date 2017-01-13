# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='pages.Page', serialize=False, primary_key=True)),
                ('add_toc', models.BooleanField(help_text='Include a list of child links', verbose_name='Add TOC', default=False)),
            ],
            options={
                'verbose_name_plural': 'Courses Pages',
                'verbose_name': 'Course',
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
    ]
