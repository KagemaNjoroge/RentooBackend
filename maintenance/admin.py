from django.contrib import admin

from .models import MaintenanceRequest


@admin.register(MaintenanceRequest)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        "property",
        "description",
        "requested_by",
        "request_date",
        "is_completed",
        "completed_date",
    )
    list_filter = ("is_completed",)
    search_fields = ("property", "description", "requested_by")

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
