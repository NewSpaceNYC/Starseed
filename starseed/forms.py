from django import forms
from captcha.fields import CaptchaField
from starseed.models import Project
from django.core.mail import EmailMessage
from django.conf import settings
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class CaptchaTestModelForm(forms.ModelForm):
    captcha = CaptchaField()

    def send_email(self):
        message1 = Mail(
            from_email=settings.SERVER_EMAIL,
            to_emails=settings.SERVER_TO_EMAILS,
            subject='Application from ' + self.cleaned_data["name"],
            html_content='Name: ' + self.cleaned_data["person"] + '<br>Email: ' + self.cleaned_data["email"] + '<br>IdeaName: ' + self.cleaned_data["name"] + '<br>Equity: ' + self.cleaned_data["equity"] + '<br>Description: ' + self.cleaned_data["description"])

        message2 = Mail(
            from_email=settings.SERVER_EMAIL,
            to_emails=self.cleaned_data["email1"],
            subject=self.cleaned_data["person"] + ' suggests you apply for the Starseed - pico innovation fund',
            html_content='Hi There!: <br>' + self.cleaned_data["person"] + ' suggested you apply for the Starseed pico innovation fund.<br><br>Apply today at https://starseed.fund ')

        message2 = Mail(
            from_email=settings.SERVER_EMAIL,
            to_emails=self.cleaned_data["email1"],
            subject=self.cleaned_data["person"] + ' suggests you apply for the Starseed - pico innovation fund',
            html_content='Hi There!: <br>' + self.cleaned_data["person"] + ' suggested you apply for the Starseed pico innovation fund.<br><br>Apply today at https://starseed.fund ')
        
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY', ''))
            response = sg.send(message1)
            response = sg.send(message2)
            response = sg.send(message3)
        except Exception as e:
            print(e.message)


    class Meta:
        fields =  '__all__'
        model = Project