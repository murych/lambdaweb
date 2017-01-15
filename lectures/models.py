from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from future.builtins import str
from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, Ownable, RichText, Slugged
from mezzanine.generic.fields import CommentsField, RatingField
from mezzanine.utils.models import AdminThumbMixin, upload_to
from mezzanine.pages.models import Page
from embed_video.fields import EmbedVideoField

"""
lectures/models.py
"""


class Lecture(Displayable, Ownable, RichText, AdminThumbMixin):
	"""
	A lecture entry.
	In theory, it should be inherited from Course class, which acts
	like category. but lol no.
	Also takes a lot of propetries from mezzanine.blog, as they are pretty
	similiar in destination.
	"""

	allow_comments = models.BooleanField(verbose_name=_("Allow comments"),
		default=True)
	categories = models.ManyToManyField("LectureCategory",
		verbose_name=_("Categories"),
		blank=True, related_name="lecture")
	comments = CommentsField(verbose_name=_("Comments"))
	featured_image = FileField(verbose_name=_("Featured Image"),
		upload_to=upload_to("lectures.Lecture.featured_image", "lecture"),
		format="Image", max_length=255, null=True, blank=True)
	rating = RatingField(verbose_name=_("Rating"))
	# related_course = models.ForeignKey('Course')
	related_lectures = models.ManyToManyField("self",
		verbose_name=_("Related lectures"), blank=True)
	video = EmbedVideoField(blank=True)

	admin_thumb_field = "featured_image"

	class Meta:
		verbose_name = _("Lecture")
		verbose_name_plural = _("Lectures")
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
		url_name = "lecture_detail"
		kwargs = {"slug": self.slug}
		date_parts = ("year", "month", "day")
		if settings.BLOG_URLS_DATE_FORMAT in date_parts:
			url_name = "lecture_detail_%s" % settings.BLOG_URLS_DATE_FORMAT
			for date_part in date_parts:
				date_value = str(getattr(self.publish_date, date_part))
				if len(date_value) == 1:
					date_value = "0%s" % date_value
				kwargs[date_part] = date_value
				if date_part == settings.BLOG_URLS_DATE_FORMAT:
					break
		return reverse(url_name, kwargs=kwargs)


class LectureCategory(Slugged):
	"""
	A category for grouping blog posts into a series.
	"""

	class Meta:
		verbose_name = _("Lecture Category")
		verbose_name_plural = _("Lecture Categories")
		ordering = ("title",)

	@models.permalink
	def get_absolute_url(self):
		return "lecture_list_category", (), {"category": self.slug}


class LecturesPage(Page):
	add_toc = models.BooleanField(_("Add TOC"), default=False,
		help_text=_("Include a list of child links"))

	class Meta:
		verbose_name = _("Lectures")
		verbose_name_plural = _("Lectures Pages")