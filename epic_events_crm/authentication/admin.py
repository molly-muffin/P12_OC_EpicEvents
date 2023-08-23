from django.contrib import admin
from authentication.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "last_name", "first_name", "role")
    list_filter = ("role", )
    fields = (("first_name", "last_name"), "username", "email", "role", "is_active")


