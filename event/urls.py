from django.urls import path

from event.views import EventView, EventCreate, EventModify, EventReplyCreate, EventReplyModify

urlpatterns = [
    path('list/', EventView.as_view()),
    path('post/', EventCreate.as_view()),
    path('modify/<int:pk>/', EventModify.as_view()),
    path('reply/', EventReplyCreate.as_view()),
    path('reply_modify/<int:pk>/', EventReplyModify.as_view()),

]
