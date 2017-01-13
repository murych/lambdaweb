from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
# from django import VERSION

from .models import Course, Lecture
from mezzanine.conf import settings
from mezzanine.generic.models import AssignedKeyword, Keyword
from mezzanine.utils.views import render, paginate


# def courses_list(request, category=None, template="mezzanine_people/person_list.html"):
# 	"""
# 	Display a list of people that are filtered by category.
# 	Custom templates are checked for using the name
# 	``people/person_list_XXX.html`` where ``XXX`` is the category's slug.
# 	"""
# 	settings.use_editable()
# 	templates = []
# 	people = Person.objects.published()
# 	if category is not None:
# 		category = get_object_or_404(PersonCategory, slug=category)
# 		people = people.filter(categories=category)
# 		templates.append(u"mezzanine_people/person_list_%s.html" %
# 		                 str(category.slug))
#
# 	# requires Django VERSION >= (1, 4):
# 	people = people.prefetch_related("categories")
#
# 	people = paginate(people, request.GET.get("page", 1),
# 		settings.PEOPLE_PER_PAGE,
# 		settings.MAX_PAGING_LINKS)
# 	context = {"people": people, "category": category}
# 	templates.append(template)
# 	return render(request, templates, context)
#
#
# def course_detail(request, slug,
# 		template="mezzanine_people/person_detail.html"):
# 	"""
# 	Custom templates are checked for using the name
# 	``mezzanine_people/person_detail_XXX.html`` where ``XXX`` is the
# 	person's slug.
# 	"""
# 	# people = Person.objects.published()
# 	# person = get_object_or_404(people, slug=slug)
# 	# context = {"person": person, "editable_obj": person}
# 	# templates = [u"mezzanine_people/person_detail_%s.html" % str(slug), template]
# 	# return render(request, templates, context)


def lectures_list(request, category=None, template="lectures/lectures_list.html"):
	"""
	Display a list of people that are filtered by category.
	Custom templates are checked for using the name
	``people/person_list_XXX.html`` where ``XXX`` is the category's slug.
	"""
	settings.use_editable()
	templates = []
	lectures = Lecture.objects.all()
	# if category is not None:
	# 	category = get_object_or_404(PersonCategory, slug=category)
	# 	people = people.filter(categories=category)
	# 	templates.append(u"mezzanine_people/person_list_%s.html" %
	# 	                 str(category.slug))

	# requires Django VERSION >= (1, 4):
	# people = people.prefetch_related("categories")
	#
	# people = paginate(people, request.GET.get("page", 1),
	# 	settings.PEOPLE_PER_PAGE,
	# 	settings.MAX_PAGING_LINKS)
	# context = {"people": people, "category": category}
	context = {"lectures": lectures}
	templates.append(template)
	return render(request, templates, context)


def lecture_detail(request, slug,
		template="mezzanine_people/person_detail.html"):
	"""
	Custom templates are checked for using the name
	``mezzanine_people/person_detail_XXX.html`` where ``XXX`` is the
	person's slug.
	"""
	lecture = Lecture.objects.published()
	lecture = get_object_or_404(lecture, slug=slug)
	context = {"lecture": lecture, "editable_obj": lecture}
	templates = [u"lectures/lecture_detail_%s.html" % str(slug), template]
	return render(request, templates, context)
