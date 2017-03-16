from django.db import models
from colorfield.fields import ColorField
from meta.models import ModelMeta
from ckeditor_uploader.fields import RichTextUploadingField
from filebrowser.fields import FileBrowseField
from lambdaweb import settings
# import team.models
from hitcount.models import HitCountMixin


class Article(ModelMeta, models.Model, HitCountMixin):
    title = models.CharField(max_length=300, verbose_name="Название")
    sub_title = models.CharField(max_length=300, verbose_name="Слоган")
    short_description = RichTextUploadingField(verbose_name="Короткое описание")
    description = RichTextUploadingField(verbose_name="Статья")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", null=True, blank=True)
    tags = models.ManyToManyField("team.Tag", verbose_name="Тэги")
    datetime_create = models.DateTimeField(auto_now_add=True)
    type = models.BooleanField(default=False, verbose_name="Главная новость")
    datetime_updated = models.DateTimeField(auto_now=True)
    main_image = FileBrowseField("Главное изображение", max_length=200, directory="images/", blank=True, null=True)
    post_in_vk = models.BooleanField(verbose_name="Постить в вк?", default=False)
    post_in_twitter = models.BooleanField(verbose_name="Постить в твиттер?", default=False)
    project_blog = models.ForeignKey("team.Project", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    metadata = {
        'title': 'name',
        'description': 'abstract',
    }

