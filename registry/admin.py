from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.


class EventAdmin(MarkdownModelAdmin):
	list_display = ('name', 'created_date')
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Member)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Partner)
admin.site.register(models.Project)
admin.site.register(models.Feedback)