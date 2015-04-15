from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

class ProjectView(TemplateView):
    template_name = "project.html"
    

#signup
#invte team members
#