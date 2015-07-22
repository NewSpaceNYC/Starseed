from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from starseed.views import *

urlpatterns = patterns('',
    (r'^accounts/', include('allauth.urls')),
    (r'^$', HomeView.as_view()),
    (r'^product/', ProductView.as_view()),
    (r'^admin/', include(admin.site.urls)),
    (r'^add-bounty/', AddBountyView.as_view()),
    (r'^bounties/', BountiesView.as_view()),
    (r'^dashboard/', DashboardView.as_view()),
    (r'^moonpie/', MoonpieView.as_view()),
    (r'^partners/', PartnersView.as_view()),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
