from rest_framework import serializers

from announcement.models import Announcement


class AnnouncementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['Announce_msg', 'Is_pinned', 'File_id', 'DateCreated']

    def create(self, validated_data):
        return Announcement.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Announce_msg = validated_data['Announce_msg']
        instance.Is_pinned = validated_data['Is_pinned']
        instance.File_id = validated_data['File_id']
        instance.save()
        return instance
