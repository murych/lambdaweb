from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from filebrowser.fields import FileBrowseField
from hitcount.models import HitCountMixin

from lambdaweb import settings
from django_ymap.fields import YmapCoord
from meta.models import ModelMeta


class EventLocation(models.Model):
    address = models.CharField("Адрес", max_length=300, blank=True)
    point = YmapCoord(max_length=200, start_query=u'Россия', size_width=500, size_height=500,
                      verbose_name="Выберите место на карте")
    name = models.CharField("Аудитория", max_length=300, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.address

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"


class Event(ModelMeta,models.Model, HitCountMixin):
    title = models.CharField(verbose_name="Название", max_length=300)
    sub_title = models.CharField(verbose_name="Слоган", max_length=500)
    slug = models.SlugField()
    start = models.DateTimeField(verbose_name="Начало")
    end = models.DateTimeField(verbose_name="Окончание", blank=True, null=True)
    allow_comments = models.BooleanField(verbose_name="Открыть коменты?", default=True)
    location = models.ForeignKey('event.EventLocation', verbose_name="Местоположение")
    description = RichTextUploadingField(verbose_name="Статья")
    featured_image = FileBrowseField("Главное изображение", max_length=200, directory="event/", blank=True, null=True)
    profile_image = FileBrowseField("Изображение профиля", max_length=200, directory="event/", blank=True, null=True)
    tags = models.ForeignKey("team.Tag", verbose_name="Тэги", default="")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", null=True, blank=True)
    internet_available = models.BooleanField(verbose_name="Есть доступ к интернету", default=True)
    take_computer = models.BooleanField(verbose_name="Брать компьютер", default=True)
    site = models.URLField(verbose_name="Сайт мероприятия", default="")
    type = models.BooleanField(default=False, verbose_name="Главная новость")
    value = models.CharField(verbose_name="Стоимость", max_length=300, default="Бесплатно")

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ("-start",)

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
        'twitter_card': 'summary_large_image',
        'keywords': 'get_keywords',
    }

    def __str__(self):
        return self.title

    def get_seo_title(self):
        return self.title + ' - Lambda'

    def get_seo_image(self):
        return self.featured_image.url

    def get_keywords(self):
        return self.events.key_words.strip().split(',')

    def get_description(self):
        return self.events.seo_description