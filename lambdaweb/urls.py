from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
# from .sitemap import *


urlpatterns = [
	# Examples:
	# url(r'^$', 'lambdaweb.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^registry/', include('registry.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)