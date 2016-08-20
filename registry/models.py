from django.db import models
from django.core.urlresolvers import reverse
from unidecode import unidecode
from django.template.defaultfilters import slugify
# from filer.models.foldermodels import Folder
from django_markdown.models import MarkdownField

default_url_vk = "https://vk.com/lambdafrela"
default_url_github = "https://github.com/lambdafrela"


class Entry(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField(max_length=100, default=default_url_vk)
	description = MarkdownField()
	slug = models.SlugField(max_length=300, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(null=True)

	class Meta:
		ordering = ['-created_date']

	def get_absolute_url(self):
		return reverse('event', args=[str(self.slug)])

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name))
		super(Entry, self).save(*args, **kwargs)


class Event(Entry):
	date = models.DateTimeField()
	address = models.CharField(max_length=300)
	future = models.BooleanField(default=False)
	avatar = models.ImageField(null=True, blank=True, upload_to='events/%Y/%m/%d/')
	speaker = models.CharField(max_length=100, blank=True)
	calendar = models.URLField(blank=True)

	class Meta:
		ordering = ['-date']


class Project(Entry):
	github = models.URLField(max_length=100, default=default_url_github)


class Partner(Entry):
	email = models.EmailField(max_length=100, blank=True)


class Member(Entry):
	github = models.URLField(max_length=100, default=default_url_github)
	email = models.EmailField(max_length=100)


class Feedback(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	text = models.TextField(max_length=100)
	author = models.CharField(max_length=50)
	role = models.CharField(max_length=50)

	class Meta:
		ordering = ['-date']
