from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from starseed.views import *

urlpatterns = [

    path('accounts/', include('allauth.urls')),
    path('', HomeView.as_view()),
    path('captcha/', include('captcha.urls')),
    path('thanks/', TemplateView.as_view(template_name='thanks.html')),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('admin/', admin.site.urls),



    path('accounts/profile/', ProfileView.as_view(), name="profile_user"),
    path("accounts/profile/<slug>/", ProfileDetailView.as_view(), name="profile_user"),
    path('error/', throw_error, name='error'),
]


admin.site.site_header = 'Starseed Admin'
admin.site.site_title = 'Starseed Admin'
admin.site.site_url = None # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.AdminSite.site_url
