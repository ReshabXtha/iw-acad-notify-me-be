from rest_framework import serializers
from rest_framework.parsers import FileUploadParser

from announcement.models import Announcement, Announcement_File


class FileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement_File
        fields = ['id', 'Announcement', 'File']


class AnnouncementModelSerializer(serializers.ModelSerializer):
    file = FileModelSerializer(read_only=True, many=True)

    class Meta:
        model = Announcement
        fields = ['id', 'Announce_msg', 'Is_pinned', 'DateCreated', 'file']

    def create(self, validated_data):
        A1 = Announcement.objects.create(**validated_data)
        Announcement_File.objects.create(Announcement=A1, **self.context)
        return A1

    def update(self, instance, validated_data):
        instance.Announce_msg = validated_data['Announce_msg']
        instance.Is_pinned = validated_data['Is_pinned']
        instance.save()
        return instance
