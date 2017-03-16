from __future__ import unicode_literals

from django.conf.urls import patterns, url
from mezzanine.conf import settings

"""
lectures/urls.py
"""

# Trailing slahes for urlpatterns based on setup.
_slash = "/" if settings.APPEND_SLASH else ""

# People patterns.
urlpatterns = patterns("lectures.views",
	url(r"^category/(?P<category>.*)/$", "lectures_list", name="lectures_list_category"),
	url(r'^(?P<slug>.*)%s$' % _slash, "lecture_detail", name='lecture_detail'),
	url(r"^$", "lectures_list", name="lectures_list"),
)
