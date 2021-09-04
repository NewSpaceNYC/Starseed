from django import forms
from captcha.fields import CaptchaField
from starseed.models import Project
from django.core.mail import EmailMessage
from django.conf import settings
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To


class CaptchaTestModelForm(forms.ModelForm):
    captcha = CaptchaField()

    def send_email(self):
        if not self.cleaned_data.get("email3",""):

            message1 = Mail(
                from_email=settings.SERVER_EMAIL,
                to_emails=[
                    To(settings.SERVER_TO_EMAILS.split(",")[0], ""),
                    To(settings.SERVER_TO_EMAILS.split(",")[1], ""),
                ],
                subject="Application from " + self.cleaned_data["name"],
                
                html_content="Name: "
                + self.cleaned_data["person"]
                + "<br>Email: "
                + self.cleaned_data["email"]
                + "<br>IdeaName: "
                + self.cleaned_data["name"]
                + "<br>Equity: "
                + str(self.cleaned_data["equity"])
                + "<br>Description: "
                + self.cleaned_data["description"]
                + "<br>Email1: "
                + self.cleaned_data["email1"]
                + "<br>Email2: "
                + self.cleaned_data["email2"]
                + "<br>Email3: "
                + self.cleaned_data.get("email3","")
                + "<br>Captcha: "
                + str(self.cleaned_data["captcha"])
                + "",
            )

            message2 = Mail(
                from_email=settings.SERVER_EMAIL,
                to_emails=To(self.cleaned_data["email1"], ""),
                subject=self.cleaned_data["person"]
                + " suggests you apply for the Starseed - pico innovation fund",
                html_content="Hi There!: <br>"
                + self.cleaned_data["person"]
                + " suggested you apply for the Starseed pico innovation fund.<br><br>Apply today at https://starseed.fund ",
            )

            message3 = Mail(
                from_email=settings.SERVER_EMAIL,
                to_emails=To(self.cleaned_data["email1"], ""),
                subject=self.cleaned_data["person"]
                + " suggests you apply for the Starseed - pico innovation fund",
                html_content="Hi There!: <br>"
                + self.cleaned_data["person"]
                + " suggested you apply for the Starseed pico innovation fund.<br><br>Apply today at https://starseed.fund ",
            )

            message4 = Mail(
                from_email=settings.SERVER_EMAIL,
                to_emails=To(self.cleaned_data["email"], self.cleaned_data["person"]),
                subject="Starseed: Thank you for your application ",
                html_content="Summary: <br> Name: "
                + self.cleaned_data["person"]
                + "<br>Email: "
                + self.cleaned_data["email"]
                + "<br>IdeaName: "
                + self.cleaned_data["name"]
                + "<br>Equity: "
                + str(self.cleaned_data["equity"])
                + "<br>Description: "
                + self.cleaned_data["description"],
            )

            try:
                sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY", ""))
                response = sg.send(message1)
                response = sg.send(message2)
                response = sg.send(message3)
                response = sg.send(message4)
            except Exception as e:
                print(e)

    class Meta:
        fields = "__all__"
        model = Project
