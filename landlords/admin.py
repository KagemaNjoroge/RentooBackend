from django.contrib import admin
from .models import PropertyCareTaker


@admin.register(PropertyCareTaker)
class PropertyCareTakerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "phone_number",
        "created_at",
        "updated_at",
    )
    search_fields = ("first_name", "last_name", "phone_number")
    list_filter = ("created_at", "updated_at")
