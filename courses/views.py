from __future__ import unicode_literals

from calendar import month_name

from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _
from future.builtins import int, str
from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import paginate

from .models import Course

User = get_user_model()


def courses_list(request, tag=None, year=None, month=None, username=None,
		category=None, template="courses/courses_list.html",
		extra_context=None):
	"""
	Display a list of courses that are filtered by tag, year, month,
	author or category. Custom templates are checked for using the name
	``lecrures/lecures_list_XXX.html`` where ``XXX`` is either the
	category slug or author's username if given.
	"""
	templates = []
	courses = Course.objects.all()

	# author = None
	# if username is not None:
	# 	author = get_object_or_404(User, username=username)
	# 	courses = courses.filter(user=author)
	# 	templates.append(u"courses/courses_list_%s.html" % username)

	courses = paginate(courses, request.GET.get("page", 1),
		settings.BLOG_POST_PER_PAGE,
		settings.MAX_PAGING_LINKS)
	context = {"courses_list": courses}
	context.update(extra_context or {})
	templates.append(template)
	return TemplateResponse(request, templates, context)


def course_detail(request, slug, year=None, month=None, day=None,
		template="courses/course_details.html"):
	""". Custom templates are checked for using the name
	``blog/blog_post_detail_XXX.html`` where ``XXX`` is the blog
	posts's slug.
	"""
	courses = Course.objects.published(
		for_user=request.user).select_related()
	course = get_object_or_404(courses, slug=slug)
	# related_courses = course.related_courses.published(for_user=request.user)
	# related_course = course.related_course.published(for_user=request.user)
	context = {"course": course, "editable_obj": course}
	templates = [u"courses/course_detail_%s.html" % str(slug), template]
	return TemplateResponse(request, templates, context)

# def blog_post_feed(request, format, **kwargs):
# 	"""
# 	Blog posts feeds - maps format to the correct feed view.
# 	"""
# 	try:
# 		return {"rss": PostsRSS, "atom": PostsAtom}[format](**kwargs)(request)
# 	except KeyError:
# 		raise Http404()
