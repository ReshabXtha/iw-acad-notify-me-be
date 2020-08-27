# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser, JSONParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from announcement.models import Announcement
from .serializers import AnnouncementModelSerializer, FileModelSerializer


class AnnouncementView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FormParser, FileUploadParser)

    def get(self, request, *args, **kwargs):
        qs = Announcement.objects.all().prefetch_related('file')
        serializer = AnnouncementModelSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        image = dict(request.data.lists())['file']
        serializer = AnnouncementModelSerializer(data=request.data, context=image)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'ok post'}, status=status.HTTP_201_CREATED)


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


