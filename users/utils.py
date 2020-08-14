from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.urls import reverse

from rest_framework_simplejwt.tokens import RefreshToken

class Util:
    @staticmethod
    def send_verification_email(request, user):
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        absolute_url = 'http://' + current_site + relative_link + '?token=' + str(token)
        email_body = 'Hi '+ user.username + '. Use link below to verify your email \n' + absolute_url
        email = EmailMessage(
            subject='Verify your Email',
            body = email_body,
            to = [user.email]
        )
        email.send()
