from django import forms
from django.contrib.auth.models import User
from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import SuitDateWidget, SuitTimeWidget, SuitSplitDateTimeWidget

# http://django-suit.readthedocs.org/en/develop/widgets.html#date-time-widgets
# class UserChangeForm(ModelForm):
#     class Meta:
#         model = User
#         fields = "__all__"
#         widgets = {
#             'last_login': SuitSplitDateTimeWidget,
#             'date_joined': SuitSplitDateTimeWidget,
#         }


""" Notes

 - Overriding specific field form: http://stackoverflow.com/questions/3469979/django-admin-overriding-the-widget-of-a-custom-form-field
 
"""