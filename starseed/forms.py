from django import forms
from captcha.fields import CaptchaField
from starseed.models import Project
from django.core.mail import EmailMessage
from django.conf import settings

class CaptchaTestModelForm(forms.ModelForm):
    captcha = CaptchaField()

    def send_email(self):
        email = EmailMessage(
            'Application from ' + self.cleaned_data["name"],
            'Name: ' + self.cleaned_data["person"] + \
            'Email: ' + self.cleaned_data["email"] + \
            'IdeaName: ' + self.cleaned_data["name"] + \
            'Description: ' + self.cleaned_data["description"],
            settings.SERVER_EMAIL,
            [settings.SERVER_EMAIL],
        )
        email.send()

    class Meta:
        fields =  '__all__'
        model = Project