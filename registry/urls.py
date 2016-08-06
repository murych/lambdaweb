from . import views
from django.conf.urls import include, url

urlpatterns = [
	url(r'^project/(?P<slug>[\w-]+)$', views.ProjectView.as_view(), name='project'),
	url(r'^member/(?P<slug>[\w-]+)$', views.MemberView.as_view(), name='member'),
	url(r'^partner/(?P<slug>[\w-]+)$', views.PartnerView.as_view(), name='partner'),
	url(r'^event/(?P<slug>[\w-]+)$', views.EventView.as_view(), name='event'),
]
