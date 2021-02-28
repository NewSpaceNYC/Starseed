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
        # email = EmailMessage(
        #     'Application from ' + self.cleaned_data["name"],
        #     'Name: ' + self.cleaned_data["person"] + \
        #     'Email: ' + self.cleaned_data["email"] + \
        #     'IdeaName: ' + self.cleaned_data["name"] + \
        #     'Description: ' + self.cleaned_data["description"],
        #     settings.SERVER_EMAIL,
        #     [settings.SERVER_EMAIL],
        # )
        # email.send(fail_silently=False)

        message = Mail(
            from_email=settings.SERVER_EMAIL,
            to_emails=settings.SERVER_EMAIL,
            subject='Application from ' + self.cleaned_data["name"],
            html_content='Name: ' + self.cleaned_data["person"] + 'Email: ' + self.cleaned_data["email"] + 'IdeaName: ' + self.cleaned_data["name"] + 'Description: ' + self.cleaned_data["description"])
        print(message)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY', ''))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)


    class Meta:
        fields =  '__all__'
        model = Project