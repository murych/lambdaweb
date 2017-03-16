from django.views import generic

from event.models import Event


class EventView(generic.DetailView):
    model = Event
    template_name = 'frontend/event/event.html'
