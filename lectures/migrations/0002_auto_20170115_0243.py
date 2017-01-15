# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields
import mezzanine.utils.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0004_auto_20170114_0014'),
        ('sites', '0001_initial'),
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('comments_count', models.IntegerField(editable=False, default=0)),
                ('keywords_string', models.CharField(editable=False, max_length=500, blank=True)),
                ('rating_count', models.IntegerField(editable=False, default=0)),
                ('rating_sum', models.IntegerField(editable=False, default=0)),
                ('rating_average', models.FloatField(editable=False, default=0)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.CharField(null=True, help_text='Leave blank to have the URL auto-generated from the title.', verbose_name='URL', max_length=2000, blank=True)),
                ('_meta_title', models.CharField(null=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', verbose_name='Title', max_length=500, blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', default=True, verbose_name='Generate description')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('publish_date', models.DateTimeField(null=True, help_text="With Published chosen, won't be shown until this time", db_index=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(null=True, help_text="With Published chosen, won't be shown after this time", verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('allow_comments', models.BooleanField(default=True, verbose_name='Allow comments')),
                ('featured_image', mezzanine.core.fields.FileField(null=True, verbose_name='Featured Image', max_length=255, blank=True)),
            ],
            options={
                'ordering': ('-publish_date',),
                'verbose_name_plural': 'Lectures',
                'verbose_name': 'Lecture',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.CreateModel(
            name='LectureCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.CharField(null=True, help_text='Leave blank to have the URL auto-generated from the title.', verbose_name='URL', max_length=2000, blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name_plural': 'Lecture Categories',
                'verbose_name': 'Lecture Category',
            },
        ),
        migrations.CreateModel(
            name='LecturesPage',
            fields=[
                ('page_ptr', models.OneToOneField(to='pages.Page', serialize=False, parent_link=True, primary_key=True, auto_created=True)),
                ('add_toc', models.BooleanField(help_text='Include a list of child links', default=False, verbose_name='Add TOC')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name_plural': 'Lectures Pages',
                'verbose_name': 'Lectures',
            },
            bases=('pages.page',),
        ),
        migrations.RemoveField(
            model_name='blogcategory',
            name='site',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='related_posts',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='site',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='user',
        ),
        migrations.DeleteModel(
            name='BlogCategory',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.AddField(
            model_name='lecture',
            name='categories',
            field=models.ManyToManyField(to='lectures.LectureCategory', related_name='lecture', verbose_name='Categories', blank=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='related_lectures',
            field=models.ManyToManyField(to='lectures.Lecture', related_name='related_lectures_rel_+', verbose_name='Related lectures', blank=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='site',
            field=models.ForeignKey(editable=False, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='user',
            field=models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL, related_name='lectures'),
        ),
    ]
