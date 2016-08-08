from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Member)
admin.site.register(models.Event)
admin.site.register(models.Partner)
admin.site.register(models.Project)
admin.site.register(models.Feedback)
