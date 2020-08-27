from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import UserRegisterView, VerifyEmail, LoginAPIView, UserListView, UserDestroyView, UserActivationView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('email-verify/',VerifyEmail.as_view(), name='email-verify'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('delete/<int:pk>/', UserDestroyView.as_view(), name='user-delete'),
    path('activate/<int:pk>/', UserActivationView.as_view(), name='user-activation'),


    path('<int:pk>/profile/', include('user_profile.urls')),
    
]
