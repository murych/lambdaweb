# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields
import mezzanine.utils.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('comments_count', models.IntegerField(editable=False, default=0)),
                ('keywords_string', models.CharField(blank=True, max_length=500, editable=False)),
                ('rating_count', models.IntegerField(editable=False, default=0)),
                ('rating_sum', models.IntegerField(editable=False, default=0)),
                ('rating_average', models.FloatField(editable=False, default=0)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.CharField(blank=True, null=True, verbose_name='URL', help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000)),
                ('_meta_title', models.CharField(blank=True, null=True, verbose_name='Title', help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('gen_description', models.BooleanField(verbose_name='Generate description', help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', default=True)),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('publish_date', models.DateTimeField(blank=True, null=True, verbose_name='Published from', help_text="With Published chosen, won't be shown until this time", db_index=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True, verbose_name='Expires on', help_text="With Published chosen, won't be shown after this time")),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(verbose_name='Show in sitemap', default=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('start', models.DateTimeField(verbose_name='Start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='End')),
                ('facebook_event', models.BigIntegerField(blank=True, null=True, verbose_name='Facebook')),
                ('allow_comments', models.BooleanField(verbose_name='Allow comments', default=True)),
                ('featured_image', mezzanine.core.fields.FileField(blank=True, null=True, verbose_name='Featured Image', max_length=255)),
            ],
            options={
                'ordering': ('-start',),
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.CharField(blank=True, null=True, verbose_name='URL', help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000)),
                ('address', models.TextField()),
                ('mappable_location', models.CharField(blank=True, help_text='This address will be used to calculate latitude and longitude. Leave blank and set Latitude and Longitude to specify the location yourself, or leave all three blank to auto-fill from the Location field.', max_length=128)),
                ('lat', models.DecimalField(null=True, verbose_name='Latitude', help_text='Calculated automatically if mappable location is set.', decimal_places=7, blank=True, max_digits=10)),
                ('lon', models.DecimalField(null=True, verbose_name='Longitude', help_text='Calculated automatically if mappable location is set.', decimal_places=7, blank=True, max_digits=10)),
                ('site', models.ForeignKey(to='sites.Site', editable=False)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Event Location',
                'verbose_name_plural': 'Event Locations',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, blank=True, to='agenda.EventLocation'),
        ),
        migrations.AddField(
            model_name='event',
            name='site',
            field=models.ForeignKey(to='sites.Site', editable=False),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(verbose_name='Author', related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
