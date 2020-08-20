from rest_framework import serializers

from announcement.models import Announcement


class AnnouncementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['Announce_msg', 'Is_pinned', 'DateCreated']

    def create(self, validated_data):
        return Announcement.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Announce_msg = validated_data['Announce_msg']
        instance.Is_pinned = validated_data['Is_pinned']
        instance.save()
        return instance
