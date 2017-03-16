from django.shortcuts import render
from blog.models import *
from event.models import *
# Create your views here.
from django.template.response import TemplateResponse
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from django.utils import timezone
from team.models import *


def index(request):
    context = {}
    context['articls'] = Article.objects.all()[:3]
    context['events'] = Event.objects.all()[:6]
    return TemplateResponse(request, "frontend/index.html", context)


def article_list(request):
    context = {}
    context['articls'] = Article.objects.all()
    return TemplateResponse(request, "frontend/blog/list.html", context)


def event_list(request):
    context = {}
    context['events'] = Event.objects.all()
    return TemplateResponse(request, "frontend/event/list.html", context)


def event(request, slug):
    context = {}
    context['event'] = Event.objects.get(slug=slug)
    date = abs(context['event'].end - context['event'].start)
    context['time'] = date.seconds / 60
    hit_count = HitCount.objects.get_for_object(context['event'])
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    context['datetime_now'] = timezone.now()
    return TemplateResponse(request, "frontend/event/event.html", context)


def patner(request, slug):
    context = {}
    context['partner'] = Partner.objects.get(slug=slug)
    return TemplateResponse(request, "frontend/partner/partner.html", context)


def patners_list(request):
    context = {}
    context['partners'] = Partner.objects.all()
    return TemplateResponse(request, "frontend/partner/list.html", context)
