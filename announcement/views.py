from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AnnouncementModelSerializer, FileModelSerializer

from announcement.models import Announcement


class AnnouncementView(APIView):
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)

    def get(self, request, *args, **kwargs):
        qs = Announcement.objects.all().prefetch_related('file')
        serializer = AnnouncementModelSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        file = request.data.get('file')
        context = {
            'File': file
        }
        serializer = AnnouncementModelSerializer(data=request.data, context=context)
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
        return Response({'status': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)


class UploadFile(CreateAPIView):
    serializer_class = FileModelSerializer


class UploadAnnounce(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileModelSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
