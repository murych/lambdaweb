# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mezzanine.core.fields
import mezzanine.utils.models
from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('sites', '0001_initial'),
		('pages', '0004_auto_20170114_0014'),
	]

	operations = [
		migrations.CreateModel(
			name='PeoplePage',
			fields=[
				('page_ptr', models.OneToOneField(to='pages.Page', auto_created=True, parent_link=True, serialize=False,
					primary_key=True)),
				('add_toc',
				models.BooleanField(default=False, help_text='Include a list of child links', verbose_name='Add TOC')),
			],
			options={
				'verbose_name_plural': 'About Pages',
				'verbose_name'       : 'About',
				'ordering'           : ('_order',),
			},
			bases=('pages.page',),
		),
		migrations.CreateModel(
			name='Person',
			fields=[
				('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
				('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
				('title', models.CharField(max_length=500, verbose_name='Title')),
				('slug', models.CharField(max_length=2000, blank=True,
					help_text='Leave blank to have the URL auto-generated from the title.', verbose_name='URL',
					null=True)),
				('_meta_title', models.CharField(max_length=500, blank=True,
					help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.',
					verbose_name='Title', null=True)),
				('description', models.TextField(blank=True, verbose_name='Description')),
				('gen_description', models.BooleanField(default=True,
					help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.',
					verbose_name='Generate description')),
				('created', models.DateTimeField(editable=False, null=True)),
				('updated', models.DateTimeField(editable=False, null=True)),
				('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')],
					help_text='With Draft chosen, will only be shown for admin users on the site.', default=2,
					verbose_name='Status')),
				('publish_date', models.DateTimeField(blank=True, db_index=True,
					help_text="With Published chosen, won't be shown until this time", verbose_name='Published from',
					null=True)),
				('expiry_date',
				models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown after this time",
					verbose_name='Expires on', null=True)),
				('short_url', models.URLField(blank=True, null=True)),
				('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
				('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
				('first_name', models.CharField(max_length=100, blank=True, verbose_name='first name')),
				('last_name', models.CharField(max_length=100, blank=True, verbose_name='last name')),
				('mugshot',
				mezzanine.core.fields.FileField(max_length=255, blank=True, verbose_name='Profile photo', null=True)),
				('mugshot_credit', models.CharField(max_length=200, blank=True, verbose_name='Profile photo credit')),
				('email', models.EmailField(max_length=254, blank=True, verbose_name='e-mail address')),
				('bio', mezzanine.core.fields.RichTextField(blank=True, default='',
					help_text='This field can contain HTML and should contain a few paragraphs describing the background of the person.',
					verbose_name='biography')),
				('job_title', models.CharField(max_length=60, blank=True, help_text='Example: First Grade Teacher',
					verbose_name='job title')),
				('order', models.PositiveSmallIntegerField(default=0)),
			],
			options={
				'verbose_name_plural': 'People',
				'verbose_name'       : 'Person',
				'ordering'           : ('order', 'last_name', 'first_name'),
			},
			bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
		),
		migrations.CreateModel(
			name='PersonCategory',
			fields=[
				('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
				('title', models.CharField(max_length=500, verbose_name='Title')),
				('slug', models.CharField(max_length=2000, blank=True,
					help_text='Leave blank to have the URL auto-generated from the title.', verbose_name='URL',
					null=True)),
				('site', models.ForeignKey(editable=False, to='sites.Site')),
			],
			options={
				'verbose_name_plural': 'Person Categories',
				'verbose_name'       : 'Person Category',
			},
		),
		migrations.CreateModel(
			name='PersonLink',
			fields=[
				('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
				('name', models.CharField(max_length=50, help_text='Friendly name of the link. E.g. Twitter',
					verbose_name='link name')),
				('url', models.URLField(verbose_name='URL')),
				('person', models.ForeignKey(to='mezzanine_people.Person')),
			],
			options={
				'ordering': ('name',),
			},
		),
		migrations.AddField(
			model_name='person',
			name='categories',
			field=models.ManyToManyField(to='mezzanine_people.PersonCategory', blank=True, related_name='people',
				verbose_name='Categories'),
		),
		migrations.AddField(
			model_name='person',
			name='site',
			field=models.ForeignKey(editable=False, to='sites.Site'),
		),
	]
