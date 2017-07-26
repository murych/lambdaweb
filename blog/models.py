from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from filebrowser.fields import FileBrowseField
from hitcount.models import HitCountMixin
from meta.models import ModelMeta

from lambdaweb import settings


class Article(ModelMeta, models.Model, HitCountMixin):
    """
        ModelMeta - для SEO элементов
        HitCountMixin  - миксин для счетчиков
    """
    title = models.CharField(max_length=300, verbose_name="Название")
    slug = models.SlugField()
    sub_title = models.CharField(max_length=300, verbose_name="Слоган")
    short_description = RichTextUploadingField(verbose_name="Короткое описание")
    description = RichTextUploadingField(verbose_name="Статья")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", null=True, blank=True)
    tags = models.ManyToManyField("team.Tag", verbose_name="Тэги")
    datetime_create = models.DateTimeField(auto_now_add=True)  # Дата создания
    type = models.BooleanField(default=False, verbose_name="Главная новость")
    datetime_updated = models.DateTimeField(auto_now=True)  # Дата обновления
    main_image = FileBrowseField("Главное изображение", max_length=200, directory="images/", blank=True, null=True)
    post_in_vk = models.BooleanField(verbose_name="Постить в вк?", default=False)
    post_in_twitter = models.BooleanField(verbose_name="Постить в твиттер?", default=False)
    project_blog = models.ForeignKey("team.Project", blank=True, null=True)

    _metadata = {
        'title': 'get_seo_title',
        'use_og': 'True',
        'use_title_tag': 'True',
        'image': 'get_seo_image',
        'description': 'get_description',
        'type': 'article',
        'use_twitter': 'True',
        'use_facebook': 'True',
        'use_googleplus': 'True',
        'locale': 'ru_RU',
        'keywords': 'get_keywords',
        'twitter_card': 'summary_large_image',
    }

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ("-datetime_create",)

    def __str__(self):
        return self.title

    def get_seo_title(self):
        return self.title + ' - Lambda'

    def get_seo_image(self):
        return self.main_image.url

    def get_keywords(self):
        return self.articles.key_words.strip().split(',')

    def get_description(self):
        return self.articles.seo_description
