from django.conf.urls import url

import event.views

urlpatterns = [
    url(r'^event/(?P<slug>[\w-]+)$', event.views.EventView.as_view(), name='event'),
]
