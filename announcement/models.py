from django.db import models

# Create your models here.
from django.utils import timezone


class Announcement(models.Model):
    Announce_msg = models.TextField()
    Is_pinned = models.BooleanField(default=False)
    DateCreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.Announce_msg)


class Announcement_File(models.Model):
    Announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, blank=True, null=True, related_name='file')
    File = models.FileField(blank=True, upload_to='announcement/Media', null=True)

    def __str__(self):
        return str(self.File)


class AnnouncementReply(models.Model):
    Announcement_id = models.ForeignKey(Announcement, on_delete=models.CASCADE, blank=True, null=True,
                                        related_name='reply')
    Reply = models.TextField()

    def __str__(self):
        return str(self.Reply)
