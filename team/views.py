from django.views import generic

from team.models import Partner


# Create your views here.

class PartnerView(generic.DetailView):
    model = Partner
    template_name = 'frontend/partner/partner.html'


class TeamView(generic.DetailView):
    pass


class ProjectView(generic.DetailView):
    pass
