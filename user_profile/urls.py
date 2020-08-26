from django.urls import path
from .views import ProfileRetrieveView, ProfileModelListAPIView, ProfileModelUpdateAPIView

urlpatterns = [
    path('', ProfileRetrieveView.as_view()),
    path('list/', ProfileModelListAPIView.as_view(), name='profile-list'),
    path('update/', ProfileModelUpdateAPIView.as_view(), name='profile-update'),
]
