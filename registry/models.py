from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django_markdown.models import MarkdownField
from unidecode import unidecode

default_url_vk = "https://vk.com/lambdafrela"
default_url_github = "https://github.com/lambdafrela"


def get_image_dir_path(instance, filename):
    if instance.get_type == 'Event':
        return 'events/{0}/{1}/{2}'.format(datetime.today().year, instance.slug, filename)
    else:
        return '{0}/{1}'.format(instance.get_type, instance.slug)


class Entry(models.Model):
    name = models.CharField(max_length=200)
    description = MarkdownField()
    slug = models.SlugField(max_length=300, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=100, default=default_url_vk)
    image = models.ImageField(null=True, upload_to=get_image_dir_path)

    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return reverse('event', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        super(Entry, self).save(*args, **kwargs)

    @property
    def get_type(self):
        return self.__class__.__name__


class Event(Entry):
    date = models.DateTimeField()
    address = models.CharField(max_length=300)
    speaker = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(null=True, blank=True,
                               upload_to=get_image_dir_path)
    calendar = models.URLField(blank=True)

    class Meta:
        ordering = ['-date']

    @property
    def is_future(self):
        tz_info = self.date.tzinfo
        if datetime.now(tz_info) < self.date:
            return True
        return False


class Project(Entry):
    github = models.URLField(max_length=100, default=default_url_github)


class Partner(Entry):
    email = models.EmailField(max_length=100, blank=True)


class Member(Entry):
    email = models.EmailField(max_length=100)
    github = models.URLField(max_length=100, default=default_url_github)


class Feedback(models.Model):
    role = models.CharField(max_length=50)
    text = models.TextField(max_length=100)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
