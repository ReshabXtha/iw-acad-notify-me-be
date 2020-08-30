from rest_framework import serializers

from event.models import Event, EventReply


class EventReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventReply
        fields = ['id', 'Event', 'Reply']


class EventModelSerializer(serializers.ModelSerializer):
    reply = EventReplySerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id','Event_Topic', 'Event_Startdate', 'Event_Enddate', 'Event_Time', 'Event_Msg', 'Event_File', 'reply']

    def create(self, validated_data):
        return Event.objects.create(**validated_data)