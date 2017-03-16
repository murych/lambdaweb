from django.shortcuts import render
from django.views import generic
from event.models import Event


# Create your views here.

class EventView(generic.DetailView):
    model = Event
    template_name = 'frontend/event/event.html'



