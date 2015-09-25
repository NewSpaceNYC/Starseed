from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from starseed.views import *

urlpatterns = patterns('',
    #url(r'^$', 'starseed.views.home', name='home'),
    url(r'^accounts/', include('allauth.urls')),
    (r'^accounts/', include('allauth.urls')),
    (r'^$', HomeView.as_view()),
    #(r'^product/', ProductView.as_view()),
    (r'^admin/', include(admin.site.urls)),
    (r'^add-bounty/', AddBountyView.as_view()),
    (r'^bounties/', BountiesView.as_view()),
    (r'^dashboard/', DashboardView.as_view()),
    (r'^moonpie/', MoonpieView.as_view()),
    (r'^partners/', PartnersView.as_view()),
) 

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += patterns('django.contrib.staticfiles.views',
#         #url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index.html'}),
#         url(r'^(?P<path>(?:js|css|img)/.*)$', 'serve'),
#     )

# https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#adminsite-attributes
admin.site.site_header = 'Starseed Admin'
admin.site.site_title = 'Starseed Admin'
admin.site.site_url = None # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.AdminSite.site_url


""" Notes
 - https://docs.djangoproject.com/en/1.8/intro/tutorial03/#write-your-first-view
 - http://django-suit.readthedocs.org/en/develop/#
"""
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
