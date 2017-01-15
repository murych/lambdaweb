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

from .models import Lecture, LectureCategory

User = get_user_model()

"""
lectures/views.py
"""


def lectures_list(request, tag=None, year=None, month=None, username=None,
		category=None, template="lectures/lectures_list.html",
		extra_context=None):
	"""
	Display a list of lectures that are filtered by tag, year, month,
	author or category. Custom templates are checked for using the name
	``lecrures/lecures_list_XXX.html`` where ``XXX`` is either the
	category slug or author's username if given.
	"""
	templates = []
	lectures = Lecture.objects.published(for_user=request.user)
	# if tag is not None:
	# 	tag = get_object_or_404(Keyword, slug=tag)
	# 	lectures = lectures.filter(keywords__keyword=tag)
	if year is not None:
		lectures = lectures.filter(publish_date__year=year)
		if month is not None:
			lectures = lectures.filter(publish_date__month=month)
			try:
				month = _(month_name[int(month)])
			except IndexError:
				raise Http404()
	if category is not None:
		category = get_object_or_404(LectureCategory, slug=category)
		lectures = lectures.filter(categories=category)
		templates.append(u"lectures/lectures_list_%s.html" %
		                 str(category.slug))
	author = None
	if username is not None:
		author = get_object_or_404(User, username=username)
		lectures = lectures.filter(user=author)
		templates.append(u"lectures/lectures_list_%s.html" % username)

	prefetch = ("categories", "keywords__keyword")
	lectures = lectures.select_related("user").prefetch_related(*prefetch)
	lectures = paginate(lectures, request.GET.get("page", 1),
		settings.BLOG_POST_PER_PAGE,
		settings.MAX_PAGING_LINKS)
	# context = {"lectures_list": lectures, "year": year, "month": month,
	# 	"category"            : category, "author": author}
	context = {"lectures_list": lectures}
	context.update(extra_context or {})
	templates.append(template)
	return TemplateResponse(request, templates, context)


def lecture_detail(request, slug, year=None, month=None, day=None,
		template="lectures/lecture_details.html"):
	""". Custom templates are checked for using the name
	``blog/blog_post_detail_XXX.html`` where ``XXX`` is the blog
	posts's slug.
	"""
	lectures = Lecture.objects.published(
		for_user=request.user).select_related()
	lecture = get_object_or_404(lectures, slug=slug)
	related_lectures = lecture.related_lectures.published(for_user=request.user)
	# related_course = lecture.related_course.published(for_user=request.user)
	context = {"lecture": lecture, "editable_obj": lecture, "related_lectures": related_lectures}
	templates = [u"lectures/lecture_detail_%s.html" % str(slug), template]
	return TemplateResponse(request, templates, context)


# def blog_post_feed(request, format, **kwargs):
# 	"""
# 	Blog posts feeds - maps format to the correct feed view.
# 	"""
# 	try:
# 		return {"rss": PostsRSS, "atom": PostsAtom}[format](**kwargs)(request)
# 	except KeyError:
# 		raise Http404()
