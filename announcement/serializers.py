from rest_framework import serializers

from announcement.models import Announcement, Announcement_File, AnnouncementReply


class ReplyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementReply
        fields = ['id','Announcement_id', 'Reply']


class FileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement_File
        fields = ['id', 'Announcement', 'File']


class AnnouncementModelSerializer(serializers.ModelSerializer):
    file = FileModelSerializer(many=True, read_only=True)
    reply = ReplyModelSerializer(many=True, read_only=True)

    class Meta:
        model = Announcement
        fields = ['id', 'Announce_msg', 'Is_pinned', 'DateCreated', 'file', 'reply']

    def create(self, validated_data):
        A1 = Announcement.objects.create(**validated_data)
        for i in self.context:
            file = {
                'File': i
            }
            Announcement_File.objects.create(Announcement=A1, **file)
        return A1

    def update(self, instance, validated_data):
        instance.Announce_msg = validated_data['Announce_msg']
        instance.Is_pinned = validated_data['Is_pinned']
        instance.File_id = validated_data['File_id']
        instance.save()
        return instance
