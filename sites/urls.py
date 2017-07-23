from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    url(r'^$', cache_page(60 * 3)(views.index), name='index'),
    url(r'^list$', cache_page(60 * 0.5)(views.article_list), name="article_list"),
    url(r'^posts/(?P<slug>[-\w]+)/$', cache_page(60 * 0.5)(views.article), name="article"),
    url(r'^list/page/(?P<page>[-\d]+)$', cache_page(60 * 0.5)(views.article_list), name="article_list_page"),
    url(r'^events$', cache_page(60 * 0.5)(views.event_list), name="event_list"),
    url(r'^events/(?P<slug>[-\w]+)/$', cache_page(60 * 0.5)(views.event), name="event"),
    url(r'^partners$', cache_page(60 * 3)(views.patners_list), name="patners_list"),
    url(r'^partners/(?P<slug>[-\w]+)/$', cache_page(60 * 3)(views.patner), name="partner"),
]