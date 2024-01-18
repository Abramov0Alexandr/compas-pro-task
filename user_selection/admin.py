from django.contrib import admin

from user_selection.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "email",
        "role_choice",
        "offer",
    )
    list_display_links = ("email",)
