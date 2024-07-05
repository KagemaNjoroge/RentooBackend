from django.contrib import admin
from .models import Agent


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone_number",
        "email",
        "website",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "phone_number",
        "email",
    )
