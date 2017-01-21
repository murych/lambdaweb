from __future__ import unicode_literals

from calendar import month_name

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _
from future.builtins import int, str
from mezzanine.blog.models import BlogCategory, BlogPost
from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import paginate

from mezzanine_people.models import Person, PersonCategory

User = get_user_model()


def home(request, tag=None, year=None, month=None, username=None,
                   category=None, template="blog/blog_post_list.html",
                   extra_context=None):
    """
    Display a list of blog posts that are filtered by tag, year, month,
    author or category. Custom templates are checked for using the name
    ``blog/blog_post_list_XXX.html`` where ``XXX`` is either the
    category slug or author's username if given.
    """
    templates = ["pages/index.html"]
    blog_posts = BlogPost.objects.published(for_user=request.user)
    if tag is not None:
        tag = get_object_or_404(Keyword, slug=tag)
        blog_posts = blog_posts.filter(keywords__keyword=tag)
    if year is not None:
        blog_posts = blog_posts.filter(publish_date__year=year)
        if month is not None:
            blog_posts = blog_posts.filter(publish_date__month=month)
            try:
                month = _(month_name[int(month)])
            except IndexError:
                raise Http404()
    if category is not None:
        category = get_object_or_404(BlogCategory, slug=category)
        blog_posts = blog_posts.filter(categories=category)
        templates.append(u"blog/blog_post_list_%s.html" %
                          str(category.slug))
    author = None
    if username is not None:
        author = get_object_or_404(User, username=username)
        blog_posts = blog_posts.filter(user=author)
        templates.append(u"blog/blog_post_list_%s.html" % username)

    prefetch = ("categories", "keywords__keyword")
    blog_posts = blog_posts.select_related("user").prefetch_related(*prefetch)
    blog_posts = paginate(blog_posts, request.GET.get("page", 1),
                          settings.BLOG_POST_PER_PAGE,
                          settings.MAX_PAGING_LINKS)
    # context = {"blog_posts": blog_posts}
    context = {"blog_posts": blog_posts, "year": year, "month": month,
               "tag": tag, "category": category, "author": author}
    context.update(extra_context or {})
    templates.append(template)
    return TemplateResponse(request, templates, context)


def members(request, category=None, template="mezzanine_people/person_list.html"):
    """
    Display a list of people that are filtered by category.
    Custom templates are checked for using the name
    ``people/person_list_XXX.html`` where ``XXX`` is the category's slug.
    """
    settings.use_editable()
    templates = ['pages/team.html']
    people = Person.objects.published()
    if category is not None:
        category = get_object_or_404(PersonCategory, slug=category)
        people = people.filter(categories=category)
        templates.append(u"mezzanine_people/person_list_%s.html" %
                          str(category.slug))

    people = people.prefetch_related("categories")

    people = paginate(people, request.GET.get("page", 1),
                      settings.PEOPLE_PER_PAGE,
                      settings.MAX_PAGING_LINKS)
    context = {"people": people, "category": category}
    templates.append(template)
    return TemplateResponse(request, templates, context)
