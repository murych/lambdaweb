from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    url(r'^members$', cache_page(60 * 15)(views.members_list), name='members_list'),
]