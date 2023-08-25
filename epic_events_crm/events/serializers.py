from rest_framework import serializers
from events.models import Event


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id",
                  "event_status",
                  "name",
                  "contract",
                  "support_contact",
                  "event_date",
                  "participants",
                  "notes",
                  "creation_date",
                  "update_date"]
