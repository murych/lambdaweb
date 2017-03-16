from __future__ import unicode_literals

from copy import deepcopy
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import settings
from mezzanine.core.admin import BaseTranslationModelAdmin, DisplayableAdmin, OwnableAdmin
from mezzanine.twitter.admin import TweetableAdminMixin

from .models import Course, CoursesPage

course_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
# course_fieldsets[0][1]["fields"].insert(1, "categories")
course_fieldsets[0][1]["fields"].insert(1, "content")
course_list_display = ["title", "user", "status", "admin_link"]
if settings.BLOG_USE_FEATURED_IMAGE:
	course_fieldsets[0][1]["fields"].insert(-2, "featured_image")
	course_list_display.insert(0, "admin_thumb")
course_fieldsets = list(course_fieldsets)
course_list_filter = deepcopy(DisplayableAdmin.list_filter)


class CourseAdmin(TweetableAdminMixin, DisplayableAdmin, OwnableAdmin):
	"""
	Admin class for blog posts.
	"""

	fieldsets = course_fieldsets
	list_display = course_list_display
	list_filter = course_list_filter

	# filter_horizontal = ("categories", "related_lectures")

	def save_form(self, request, form, change):
		"""
		Super class ordering is important here - user must get saved first.
		"""
		OwnableAdmin.save_form(self, request, form, change)
		return DisplayableAdmin.save_form(self, request, form, change)


admin.site.register(Course, CourseAdmin)
admin.site.register(CoursesPage)