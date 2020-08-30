from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from event.models import Event, EventReply
from event.serializers import EventModelSerializer, EventReplySerializer


class EventView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer


class EventCreate(CreateAPIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser, FileUploadParser)
    serializer_class = EventModelSerializer


class EventModify(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventModelSerializer


class EventReplyCreate(CreateAPIView):
    serializer_class = EventReplySerializer


class EventReplyModify(RetrieveUpdateDestroyAPIView):
    queryset = EventReply.objects.all()
    serializer_class = EventReplySerializer
