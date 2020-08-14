from django.urls import path
from .views import UserRegisterView, VerifyEmail

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('email-verify/',VerifyEmail.as_view(), name='email-verify'),
]
