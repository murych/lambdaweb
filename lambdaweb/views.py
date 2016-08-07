from django.shortcuts import render, render_to_response
from registry.models import *
# from . import utils
from django.template import RequestContext
from django.db.models import Q
# TODO: change all `context_instance` to `dict` as in events()


def index(request):
	events_list = Event.objects.all()
	return render_to_response('index.html', {'events_list': events_list})


def events(request):
	template_name = 'events.html'
	events_list = Event.objects.all()
	return render_to_response(template_name, {'events_list': events_list})


def members(request):
	template_name = 'members.html'
	members_list = Member.objects.all()
	render_to_response(template_name, {'members_list': members_list},
								context_instance=RequestContext(request))


def partners(request):
	template_name = 'partners.html'
	partners_list = Partner.objects.all()
	render_to_response(template_name, {'partners_list': partners_list},
								context_instance=RequestContext(request))


def projects(request):
	template_name = 'projects.html'
	projects_list = Partner.objects.all()
	render_to_response(template_name, {'projects_list': projects_list},
								context_instance=RequestContext(request))
