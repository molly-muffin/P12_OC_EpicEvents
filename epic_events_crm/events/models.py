from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.conf import settings
from contracts.models import Contract


class Event(models.Model):
    ALL_STATUS = ((1, 'Not attributed'),
                  (2, 'Started'),
                  (3, 'In Progress'),
                  (4, 'Ended'))
    event_status = models.PositiveSmallIntegerField(choices=ALL_STATUS, verbose_name="Status", default=1)
    name = models.CharField(max_length=100)
    contract = models.ForeignKey(Contract,
                                 on_delete=CASCADE,
                                 related_name="test",
                                 null=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=RESTRICT,
                                        related_name="event_assigned_to",
                                        null=True)
    event_date = models.DateTimeField()
    participants = models.IntegerField(default=0)
    notes = models.TextField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
