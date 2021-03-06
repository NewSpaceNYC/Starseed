#from __future__ import absolute_import 
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView

import datetime
from .models import Project
from .forms import CaptchaTestModelForm

from django.views.generic import TemplateView

def throw_error(request):
    raise ValueError('error')

class HomeView(FormView):
    template_name = "index.html"
    form_class = CaptchaTestModelForm
    success_url = '/thanks/'

    def form_valid(self, form):
        human = True
        form.save()
        form.send_email()
        return super().form_valid(form)


class ProfileView(DetailView):
    template_name = 'account/profile.html'
    def get_object(self):
        return get_object_or_404(get_user_model(), pk=self.request.user.id)

class ProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = 'account/profile.html'