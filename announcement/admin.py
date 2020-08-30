from django.contrib import admin

# Register your models here.
from announcement.models import Announcement, Announcement_File, AnnouncementReply

admin.site.register(Announcement)
admin.site.register(Announcement_File)
admin.site.register(AnnouncementReply)
