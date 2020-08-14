from django.db import models

# Create your models here.
from django.utils import timezone


class Announcement_File(models.Model):
    File = models.FileField(blank=True, upload_to='announcement/Media')


class Announcement(models.Model):
    Announce_msg = models.TextField()
    Is_pinned = models.BooleanField(default=False)
    File_id = models.ForeignKey(Announcement_File, on_delete=models.CASCADE, blank=True, null=True)
    DateCreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.Announce_msg)
