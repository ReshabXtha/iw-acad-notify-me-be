from django.urls import path

from announcement.views import AnnouncementView, UpdateDeleteAnnouncement, AnnouncementReplyCreate, \
    AnnouncementReplyModify

urlpatterns = [
    path('info/', AnnouncementView.as_view()),
    path('updel/<int:pk>/', UpdateDeleteAnnouncement.as_view()),
    path('reply',AnnouncementReplyCreate.as_view()),
    path('reply_modify/<int:pk>/',AnnouncementReplyModify.as_view())

]
