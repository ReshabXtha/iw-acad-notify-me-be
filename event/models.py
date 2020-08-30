from django.db import models

# Create your models here.
from users.models import User


class Event(models.Model):
    Event_Topic = models.CharField(max_length=100)
    Event_Startdate = models.DateField(blank=True, null=True)
    Event_Enddate = models.DateField(blank=True, null=True)
    Event_Time = models.TimeField(blank=True, null=True)
    Event_Msg = models.TextField()
    Event_File = models.FileField(upload_to='event/Media', blank=True, null=True)

    def __str__(self):
        return str(self.Event_Topic)


class EventReply(models.Model):
    Event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reply')
    Reply = models.TextField()

    def __str__(self):
        return str(self.Reply)
