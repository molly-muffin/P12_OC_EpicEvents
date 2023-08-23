from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ["id",
                  "first_name",
                  "last_name",
                  "email",
                  "phone",
                  "company_name",
                  "commercial_contact",
                  "notes",
                  "creation_date",
                  "update_date",
                 ]
