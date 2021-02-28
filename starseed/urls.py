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
    path('product/', ProductView.as_view()),
    path('thanks/', TemplateView.as_view(template_name='thanks.html')),
    path('admin/', admin.site.urls),
    path('add-bounty/', AddBountyView.as_view()),
    path('bounties/', BountiesView.as_view()),
    path('dashboard/', DashboardView.as_view()),
    path('moonpie/', MoonpieView.as_view()),
    path('partners/', PartnersView.as_view()),
    path('accounts/profile/', ProfileView.as_view(), name="profile_user"),
    path("accounts/profile/<slug>/", ProfileDetailView.as_view(), name="profile_user"),
    path('error/', throw_error, name='error'),
]


admin.site.site_header = 'Starseed Admin'
admin.site.site_title = 'Starseed Admin'
admin.site.site_url = None # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.AdminSite.site_url
