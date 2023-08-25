from django.contrib import admin
from events.models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", 
                    "name", 
                    "contract", 
                    "support_contact",
                    "event_date")
