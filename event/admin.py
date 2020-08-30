from django.contrib import admin

# Register your models here.
from event.models import Event, EventReply

admin.site.register(Event)
admin.site.register(EventReply)
