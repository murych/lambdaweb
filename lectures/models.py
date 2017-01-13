from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page


# Create your models here.

class Course():
	pass


class Lecture(Course):
	pass


class Practise(Course):
	pass

class CourseMainPage(Page):
	add_toc = models.BooleanField(_("Add TOC"), default=False,
		help_text=_("Include a list of child links"))

	class Meta:
		verbose_name = _("Course")
		verbose_name_plural = _("Courses Pages")