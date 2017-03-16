from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^list$', views.article_list, name="article_list"),

    url(r'^events$', views.event_list, name="event_list"),
    url(r'^events/(?P<slug>[-\w]+)/$', views.event, name="event"),

    url(r'^partners$', views.patners_list, name="patners_list"),
    url(r'^partners/(?P<slug>[-\w]+)/$', views.patner, name="partner"),
]