from django.urls import path

from announcement.views import AnnouncementView,UpdateDeleteAnnouncement

urlpatterns = [
    path('info/', AnnouncementView.as_view()),
    path('updel/<int:pk>/', UpdateDeleteAnnouncement.as_view()),
]
