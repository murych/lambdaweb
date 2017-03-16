# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170115_0243'),
        ('lectures', '0003_lecture_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='related_course',
            field=models.ForeignKey(blank=True, null=True, to='courses.Course'),
        ),
    ]
