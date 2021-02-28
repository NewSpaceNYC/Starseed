from django import forms
from captcha.fields import CaptchaField
from starseed.models import Project


class CaptchaTestModelForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        fields =  '__all__'
        model = Project