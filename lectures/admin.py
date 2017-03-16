from __future__ import unicode_literals

from copy import deepcopy
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import settings
from mezzanine.core.admin import BaseTranslationModelAdmin, DisplayableAdmin, OwnableAdmin
from mezzanine.twitter.admin import TweetableAdminMixin

from .models import Lecture, LectureCategory, LecturesPage

lecture_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
lecture_fieldsets[0][1]["fields"].insert(1, "categories")
lecture_fieldsets[0][1]["fields"].extend(["content", "allow_comments"])
lecture_list_display = ["title", "user", "status", "admin_link"]
if settings.BLOG_USE_FEATURED_IMAGE:
	lecture_fieldsets[0][1]["fields"].insert(-2, "featured_image")
	lecture_list_display.insert(0, "admin_thumb")
lecture_fieldsets = list(lecture_fieldsets)
lecture_fieldsets.insert(1, (_("Other lectures"), {
	"classes": ("collapse-closed",),
	"fields" : ("related_lectures", "related_course")}))
lecture_list_filter = deepcopy(DisplayableAdmin.list_filter) + ("categories",)


class LectureAdmin(TweetableAdminMixin, DisplayableAdmin, OwnableAdmin):
	"""
	Admin class for blog posts.
	"""

	fieldsets = lecture_fieldsets
	list_display = lecture_list_display
	list_filter = lecture_list_filter
	filter_horizontal = ("categories", "related_lectures")

	def save_form(self, request, form, change):
		"""
		Super class ordering is important here - user must get saved first.
		"""
		OwnableAdmin.save_form(self, request, form, change)
		return DisplayableAdmin.save_form(self, request, form, change)


class LectureCategoryAdmin(BaseTranslationModelAdmin):
	"""
	Admin class for blog categories. Hides itself from the admin menu
	unless explicitly specified.
	"""

	fieldsets = ((None, {"fields": ("title",)}),)

	def has_module_permission(self, request):
		"""
		Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
		"""
		for (name, items) in settings.ADMIN_MENU_ORDER:
			if "lectures.LectureCategory" in items:
				return True
		return False


admin.site.register(Lecture, LectureAdmin)
admin.site.register(LectureCategory, LectureCategoryAdmin)
admin.site.register(LecturesPage)