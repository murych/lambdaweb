from django.contrib import admin
from copy import deepcopy

from django.contrib import admin

from .models import CourseMainPage, Course, Lecture, Practise
from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin


# Register your models here.

admin.site.register(CourseMainPage)