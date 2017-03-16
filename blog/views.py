from django.views import generic

from blog.models import Article


class ArticleView(generic.DetailView):
    model = Article
    template_name = 'frontend/event/event.html'
