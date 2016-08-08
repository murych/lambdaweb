from django.views import generic
from .models import *


class PartnerView(generic.DetailView):
	model = Partner
	template_name = 'details/partner_details.html'


class MemberView(generic.DetailView):
	model = Member
	template_name = 'details/member_details.html'


class ProjectView(generic.DetailView):
	model = Project
	template_name = 'details/project_details.html'


class EventView(generic.DetailView):
	model = Event
	template_name = 'details/event_details.html'
