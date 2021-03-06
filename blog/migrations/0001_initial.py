# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 17:59
from __future__ import unicode_literals

import ckeditor_uploader.fields
import django.db.models.deletion
import filebrowser.fields
import meta.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('sub_title', models.CharField(max_length=300, verbose_name='Слоган')),
                (
                'short_description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Короткое описание')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Статья')),
                ('datetime_create', models.DateTimeField(auto_now_add=True)),
                ('datetime_updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                             to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('type', models.BooleanField(default=False, verbose_name='Главная новость')),
                ('main_image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True,
                                                                  verbose_name='Главное изображение')),
                ('post_in_vk', models.BooleanField(default=False, verbose_name='Постить в вк?')),
                ('post_in_twitter', models.BooleanField(default=False, verbose_name='Постить в твиттер?')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
            bases=(meta.models.ModelMeta, models.Model),
        ),
    ]
