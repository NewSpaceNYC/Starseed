from django.contrib import admin
from starseed.models import Tag
from django.contrib.auth.models import User


admin.site.register(Tag)

""" Example admin.py
from django.contrib import admin
from pishing.models import FreshPhish
from django.db import models
from forms import FreshForm
# Date and Time styling via DjangoSuit:
# http://django-suit.readthedocs.org/en/develop/widgets.html#date-time-widgets 
from django.forms import ModelForm
# from widgets import ToggleCheckbox


# Fresh Phish
class FreshAdmin(admin.ModelAdmin):
    
    # https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.formfield_overrides
    # formfield_overrides = {
    #     models.BooleanField: {'widget': ToggleCheckbox}, # https://docs.djangoproject.com/en/1.8/ref/forms/widgets/#checkboxinput
    # }
    
    form = FreshForm
    # addform = LabeledForm
    
    list_display = ('fresh_id', 'fresh_target', 'verification_time', 'submission_time')
    list_filter = ('fresh_target',)
    
    fieldsets = [ # DjangoSuit Tab code
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'fresh_url',
                'fresh_id', 
                'fresh_target',
                'live_phish',
                'verification_time',
                'country',
                'announcing_network',
                'fresh_ip',
                'cidr_block',
                'phishtank_url',
                'submission_time',
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-human_labeled',),
            'fields': ['screenshot_url', 'human_labeled', ]}),
    ]
    
    suit_form_tabs = (
                        ('general', 'Phish Details'),  # DjangoSuit Tab code
                        ('human_labeled', 'Image Label')
                    )
                 
    suit_form_includes = ( # DjangoSuit Includes: http://django-suit.readthedocs.org/en/develop/form_includes.html#example
        ('admin/labeler/index.html', '', 'human_labeled'),
    )
    

# http://stackoverflow.com/a/20413436/1762493
admin.site.register(FreshPhish, FreshAdmin)
"""

""" Notes

Customizing Admin CSS / JS
 - https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#modeladmin-asset-definitions
 - https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#overriding-admin-templates
 - https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
 - http://django-suit.readthedocs.org/en/develop/#

"""
