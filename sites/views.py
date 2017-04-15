from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.utils import timezone
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

from event.models import *
from team.models import *


def index(request):
    """
        Главная страница
    :param request:
    :return:
    """
    context = {}
    context['articles'] = Article.objects.all()[:3]
    context['events'] = Event.objects.all()[:6]
    return TemplateResponse(request, "frontend/index.html", context)


def article_list(request, page=1):
    """
        Список статей
    :param request:
    :return:
    """
    context = {}
    context['articles'] = Article.objects.all()
    context['articles_bg'] = context['articles'][:4]
    context['hit_tag'] = []
    # Я хз как нормально получить популряные тэги
    # ---------Мой костыль---------
    # Берем популярные тэги из популрных статей
    for i in HitCount.objects.all().order_by('-hits')[:10]:  # берем последние 10 статей
        if 'blog' == i.content_type.app_label:  # так как в hit_count есть и evet'ы сортируем на статьи
            for tag in i.content_object.tags.all():
                if tag not in context['hit_tag']:
                    context['hit_tag'].append(tag)  # из каждой статьи берем все тэги
    paginator = Paginator(context['articles'], 3)
    try:
        context['articles'] = paginator.page(page)
    except PageNotAnInteger:
        context['articles'] = paginator.page(1)
    except EmptyPage:
        context['articles'] = paginator.page(paginator.num_pages)
    return TemplateResponse(request, "frontend/blog/list.html", context)

from hitcount.views import HitCountMixin

def article(request, slug):
    context = {}
    context['article'] = Article.objects.get(slug=slug)
    context['meta'] = get_object_or_404(Article, slug=slug).as_meta(request)
    hit_count = HitCount.objects.get_for_object(context['article'])
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    return TemplateResponse(request, "frontend/blog/post.html", context)


def event_list(request):
    """
        Список мероприятий
    :param request:
    :return:
    """
    context = {}
    context['events'] = Event.objects.all()
    context['hit_tag'] = []

    # Я хз как нормально получить популряные тэги
    # ---------Мой костыль---------
    # Берем популярные тэги из популрных и evet'ов
    for i in HitCount.objects.all().order_by('-hits')[:10]:  # берем последние 10 evet'ов
        if 'event' == i.content_type.app_label:  # так как в hit_count есть и blog сортируем на evet
            if i.content_object.tags not in context['hit_tag']:
                context['hit_tag'].append(i.content_object.tags)  # из каждой статьи берем все тэги
    return TemplateResponse(request, "frontend/event/list.html", context)


def event(request, slug):
    """
        Мероприятие
    :param request:
    :param slug:
    :return:
    """
    context = {}
    context['event'] = Event.objects.get(slug=slug)
    date = abs(context['event'].end - context['event'].start)
    context['time'] = date.seconds / 60
    hit_count = HitCount.objects.get_for_object(context['event'])
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    context['meta'] = get_object_or_404(Event, slug=slug).as_meta(request)

    context['datetime_now'] = timezone.now()

    return TemplateResponse(request, "frontend/event/event.html", context)


def patners_list(request):
    """
        Список партнеров
    :param request:
    :return:
    """
    context = {}
    context['partners'] = Partner.objects.all()
    return TemplateResponse(request, "frontend/partner/list.html", context)


def patner(request, slug):
    """
        Партнер
    :param request:
    :param slug:
    :return:
    """
    context = {}
    context['partner'] = Partner.objects.get(slug=slug)
    return TemplateResponse(request, "frontend/partner/partner.html", context)


def project_list(request):
    """
        Партнер
    :param request:
    :param slug:
    :return:
    """
    context = {}
    context['projects'] = Project.objects.all()
    return TemplateResponse(request, "frontend/project/list.html", context)


def project(request):
    context = {}
    context['projects'] = Project.objects.all()
    return TemplateResponse(request, "frontend/project/list.html", context)
