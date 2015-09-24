#from __future__ import absolute_import 
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

import datetime
from starseed.models import Product

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

class ProductView(ListView):
     template_name = "product.html"
     model = Product
    
class AddBountyView(TemplateView):
    template_name = "AddBounty.html"

class BountiesView(TemplateView):
    template_name = "bounties.html"

class DashboardView(TemplateView):
    template_name = "dashboard.html"

class MoonpieView(TemplateView):
    template_name = "moonpie.html"

class PartnersView(TemplateView):
    template_name = "partners.html"
#signup
#invte team members


from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<i>2b or !2b</i>')
