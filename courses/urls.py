from __future__ import unicode_literals

from django.conf.urls import patterns, url
from mezzanine.conf import settings


# Trailing slahes for urlpatterns based on setup.
_slash = "/" if settings.APPEND_SLASH else ""

# People patterns.
urlpatterns = patterns("courses.views",
	# url(r"^category/(?P<category>.*)/$", "courses_list", name="courses_list_category"),
	url(r'^(?P<slug>.*)%s$' % _slash, "course_detail", name='course_detail'),
	url(r"^$", "courses_list", name="courses_list"),
)
