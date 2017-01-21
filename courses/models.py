from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, Ownable, RichText
from mezzanine.pages.models import Page
from mezzanine.utils.models import AdminThumbMixin, upload_to

"""
lectures/models.py
"""


class Course(Displayable, Ownable, RichText, AdminThumbMixin):
	"""
	A Course entry.
	"""

	# categories = models.ManyToManyField("CourseCategory",
	# 	verbose_name=_("Categories"),
	# 	blank=True, related_name="courses")
	featured_image = FileField(verbose_name=_("Featured Image"),
		upload_to=upload_to("lectured.Course.featured_image", "course"),
		format="Image", max_length=255, null=True, blank=True)

	admin_thumb_field = "featured_image"

	class Meta:
		verbose_name = _("Course")
		verbose_name_plural = _("Courses")
		ordering = ("-publish_date",)

	def get_absolute_url(self):
		"""
		URLs for blog posts can either be just their slug, or prefixed
		with a portion of the post's publish date, controlled by the
		setting ``BLOG_URLS_DATE_FORMAT``, which can contain the value
		``year``, ``month``, or ``day``. Each of these maps to the name
		of the corresponding urlpattern, and if defined, we loop through
		each of these and build up the kwargs for the correct urlpattern.
		The order which we loop through them is important, since the
		order goes from least granular (just year) to most granular
		(year/month/day).
		"""
		url_name = "course_detail"
		kwargs = {"slug": self.slug}
		return reverse(url_name, kwargs=kwargs)


class CoursesPage(Page):
	add_toc = models.BooleanField(_("Add TOC"), default=False,
		help_text=_("Include a list of child links"))

	class Meta:
		verbose_name = _("Courses")
		verbose_name_plural = _("Courses Pages")
