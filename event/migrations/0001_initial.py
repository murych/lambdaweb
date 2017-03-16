# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ckeditor_uploader.fields
import django.db.models.deletion
import filebrowser.fields
from django.conf import settings
from django.db import migrations, models

import django_ymap.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=300, verbose_name='Адрес')),
                ('name', models.CharField(blank=True, max_length=300, verbose_name='Аудитория')),
                ('point', django_ymap.fields.YmapCoord(max_length=200, verbose_name='Выберите место на карте')),
            ],
            options={
                'verbose_name': 'Местоположение',
                'verbose_name_plural': 'Местоположения',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('start', models.DateTimeField(verbose_name='Начало')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Окончание')),
                ('allow_comments', models.BooleanField(default=True, verbose_name='Открыть коменты?')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Статья')),
                ('internet_available', models.BooleanField(default=True, verbose_name='Есть доступ к интернету')),
                ('site', models.URLField(default='', verbose_name='Сайт мероприятия')),
                ('take_computer', models.BooleanField(default=True, verbose_name='Брать компьютер')),
                ('value', models.CharField(default='Бесплатно', max_length=300, verbose_name='Стоимость')),
                ('type', models.BooleanField(default=False, verbose_name='Главная новость')),
                ('sub_title', models.CharField(max_length=500, verbose_name='Слоган')),
                ('slug', models.SlugField()),
                ('featured_image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True,
                                                                      verbose_name='Главное изображение')),
                ('profile_image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True,
                                                                     verbose_name='Изображение профиля')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                             to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                               to='event.EventLocation', verbose_name='Местоположение')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ('-start',),
            },
        ),
    ]
