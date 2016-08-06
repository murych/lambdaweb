from django.shortcuts import render, render_to_response
from registry.models import *
# from . import utils
from django.template import RequestContext
from django.db.models import Q

def index(request):
	return render_to_response('index.html', RequestContext(request))