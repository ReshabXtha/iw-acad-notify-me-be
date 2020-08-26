from django.urls import path

from announcement.views import AnnouncementView, UpdateDeleteAnnouncement, UploadFile

urlpatterns = [
    path('info/', AnnouncementView.as_view()),
    path('updel/<int:pk>/', UpdateDeleteAnnouncement.as_view()),
    path('generic/', UploadFile.as_view()),

]
