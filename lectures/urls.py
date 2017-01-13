from django.conf.urls import patterns, include, url

# People patterns.
urlpatterns = patterns("lectures.views",
	# url("^category/(?P<category>.*)/$", "courses_list", name="courses_list_category"),
	# url("^person/(?P<slug>[-\w]+)/$", "course_detail", name="courses_detail"),
	# url("^$", "courses_list", name="person_list"),
	url("^category/(?P<category>.*)/$", "lectures_list", name="lectures_list_category"),
	url("^person/(?P<slug>[-\w]+)/$", "lecture_detail", name="lectures_detail"),
	url("^$", "lectures_list", name="lecture_list"),
)
