from django.db import models
from django.db.models.deletion import RESTRICT
from django.conf import settings


class Client(models.Model):
  objects = None
  first_name = models.CharField(max_length=15)
  last_name = models.CharField(max_length=15)
  email = models.EmailField(max_length=150)
  phone = models.CharField(max_length=15)
  company_name = models.CharField(max_length=150)
  commercial_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                         on_delete=RESTRICT,
                                         related_name="client_assigned_to",
                                         null=True,
                                         blank=True
                                        )
  notes = models.CharField(max_length=150)
  creation_date = models.DateTimeField(auto_now_add=True)
  update_date = models.DateTimeField(auto_now=True)
