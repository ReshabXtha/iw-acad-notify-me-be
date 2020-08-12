from django.db import models


# Create your models here.
class Announcement(models.Model):
    Announce_msg = models.TextField()
    Is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Announce_msg)


class Announcement_File(models.Model):
    Announcement_id = models.ForeignKey(Announcement, on_delete=models.CASCADE, blank=True, null=True)
    File = models.FileField(blank=True, upload_to='Media')
