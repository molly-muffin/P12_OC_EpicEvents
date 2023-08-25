from django.contrib import admin
from clients.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", 
                    "first_name", 
                    "last_name", 
                    "company_name", 
                    "email", 
                    "phone")
