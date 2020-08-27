from django.urls import path
from .views import ProfileRetrieveView, ProfileModelUpdateAPIView

urlpatterns = [
    path('', ProfileRetrieveView.as_view()),
    path('update/', ProfileModelUpdateAPIView.as_view(), name='profile-update'),
]
