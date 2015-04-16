from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from starseed.views import HomeView, ProductView

urlpatterns = patterns('',
    # Examples:
    (r'^accounts/', include('allauth.urls')),
    (r'^$', HomeView.as_view()),
    (r'^$', ProductView.as_view()),
    (r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
