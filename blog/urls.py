import event.views
import blog.views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^blog/(?P<slug>[\w-]+)$', blog.views.ArticleView.as_view(), name='articles'),
]
