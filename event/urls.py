import event.views
import blog.views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^event/(?P<slug>[\w-]+)$', event.views.EventView.as_view(), name='event'),
]
