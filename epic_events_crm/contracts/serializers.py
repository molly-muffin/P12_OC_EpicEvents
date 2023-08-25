from rest_framework import serializers
from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", 
                  "client", 
                  "commercial_contact", 
                  "status", 
                  "amount", 
                  "payment_due", 
                  "creation_date", 
                  "update_date"]
