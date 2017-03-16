from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from blog.models import Article
from django.views import generic


# Create your views here.

class ArticleView(generic.DetailView):
    model = Article
    template_name = 'frontend/event/event.html'
