from django.contrib import admin
from django.contrib import admin
from contracts.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", 
                    "client", 
                    "commercial_contact", 
                    "status", 
                    "amount", 
                    "payment_due", 
                   )