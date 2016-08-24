from registry.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
	events_list = Event.objects.all()
	projects_list = Project.objects.all()
	feedback_list = Feedback.objects.all()
	return render_to_response('index.html', {'events_list'  : events_list,
	                                         'projects_list': projects_list,
	                                         'feedback_list': feedback_list})


def events(request):
	events_list = Event.objects.all()
	return render_to_response('events.html', {'events_list': events_list})


def members(request):
	members_list = Member.objects.all()
	return render_to_response('members.html', {'members_list': members_list})


def partners(request):
	partners_list = Partner.objects.all()
	return render_to_response('partners.html', {'partners_list': partners_list})


def projects(request):
	projects_list = Project.objects.all()
	return render_to_response('projects.html', {'projects_list': projects_list})


def handler404(request):
	response = render_to_response('404.html', {}, context_instance=RequestContext(request))
	response.status_code = 404
	return response


def handler500(request):
	response = render_to_response('500.html', {}, context_instance=RequestContext(request))
	response.status_code = 500
	return response
