from __future__ import absolute_import 
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

import datetime
from .models import Product

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

class ProductView(ListView):
    template_name = "product.html"
    model = Product
    

#signup
#invte team members
#