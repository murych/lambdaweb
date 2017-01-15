from __future__ import unicode_literals

from django.conf.urls import url
from mezzanine.conf import settings

from lectures import views

"""
lectures/urls.py
"""

# Trailing slahes for urlpatterns based on setup.
_slash = "/" if settings.APPEND_SLASH else ""

# Blog patterns.
urlpatterns = [
	# url("^feeds/(?P<format>.*)%s$" % _slash,
	# 	views.blog_post_feed, name="blog_post_feed"),
	# url("^tag/(?P<tag>.*)/feeds/(?P<format>.*)%s$" % _slash,
	# 	views.blog_post_feed, name="blog_post_feed_tag"),
	# url("^tag/(?P<tag>.*)%s$" % _slash,
	# 	views.blog_post_list, name="blog_post_list_tag"),
	# url(r'^category/(?P<category>.*)/feeds/(?P<format>.*)%s$' % _slash,
	# 	views.blog_post_feed, name='lecture_feed_category'),
	url(r'^category/(?P<category>.*)%s$' % _slash,
		views.lectures_list, name='lectures_list_category'),
	# url(r'^author/(?P<username>.*)/feeds/(?P<format>.*)%s$' % _slash,
	# 	views.lecture_feed, name='lecture_feed_author'),
	url(r'^author/(?P<username>.*)%s$' % _slash,
		views.lectures_list, name='lectures_list_author'),
	# url("^archive/(?P<year>\d{4})/(?P<month>\d{1,2})%s$" % _slash,
	# 	views.lecture_list, name="lecture_list_month"),
	# url("^archive/(?P<year>\d{4})%s$" % _slash,
	# 	views.lecture_list, name="lecture_list_year"),
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>.*)%s$' % _slash,
		views.lecture_detail, name='lecture_detail_day'),
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>.*)%s$' % _slash,
		views.lecture_detail, name='lecture_detail_month'),
	url(r'^(?P<year>\d{4})/(?P<slug>.*)%s$' % _slash,
		views.lecture_detail, name='lecture_detail_year'),
	url(r'^(?P<slug>.*)%s$' % _slash,
		views.lecture_detail, name='lecture_detail'),
	url(r'^$', views.lectures_list, name='lecture_list'),

]
