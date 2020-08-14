from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AnnouncementModelSerializer

from announcement.models import Announcement


class AnnouncementView(APIView):

    def get(self, request, *args, **kwargs):
        qs = Announcement.objects.all()
        serializer = AnnouncementModelSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AnnouncementModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'ok post', 'result': serializer.data}, status=status.HTTP_201_CREATED)


class UpdateDeleteAnnouncement(APIView):
    def get(self, request, pk, **kwargs):
        try:
            obj = Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            return Response({'error': 'Does not exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnnouncementModelSerializer(obj)
        return Response(serializer.data)

    def patch(self, request, pk, **kwargs):
        try:
            obj = Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            return Response({'error': 'Does not exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnnouncementModelSerializer(data=request.data, instance=obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'ok patch'})

    def delete(self, request, pk, **kwargs):
        try:
            obj = Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            return Response({'error': 'Does not exists'}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({'status':'Deleted'},status=status.HTTP_204_NO_CONTENT)