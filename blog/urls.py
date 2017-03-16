from django.conf.urls import url

import blog.views

urlpatterns = [
    url(r'^blog/(?P<slug>[\w-]+)$', blog.views.ArticleView.as_view(), name='articles'),
]
