from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^registry/', include('registry.urls')),
	url(r'^partners/$', views.partners, name="partners"),
	url(r'^projects/$', views.projects, name="projects"),
	url(r'^members/$', views.members, name="members"),
	url(r'^events/$', views.events, name="events"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)