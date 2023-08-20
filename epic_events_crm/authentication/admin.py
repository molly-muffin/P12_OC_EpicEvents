from django.contrib import admin
from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("username", "last_name", "first_name", "role")
    list_filter = ("role", )
    fields = (("first_name", "last_name"), "username", "email", "role", "is_active")


admin.site.register(User, UserAdmin)
