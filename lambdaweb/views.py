from calendar import month_name
from django.http import Http404
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from mezzanine.blog.models import BlogCategory, BlogPost
from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import paginate


def home(request, tag=None, year=None, month=None, username=None,
         category=None, template="blog/blog_post_list.html",
         extra_context=None):
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
    blog_posts = paginate(blog_posts, request.GET.get('page', 1),
                          settings.BLOG_POST_PER_PAGE,
                          settings.MAX_PAGING_LINKS)
    context = {"blog_posts": blog_posts}
    context.update(extra_context or {})
    templates.append(template)
    return TemplateResponse(request, templates, context)
