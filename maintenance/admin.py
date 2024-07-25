from django.contrib import admin
from .models import MaintenanceRequest, Maintainer, Maintenance


@admin.register(Maintainer)
class MaintainerAdmin(admin.ModelAdmin):
    list_display = ("name", "maintainer_type")
    search_fields = ("name", "description")


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ("request", "maintainer", "is_done")
    list_filter = ("is_done",)


@admin.register(MaintenanceRequest)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        "house",
        "description",
        "request_date",
        "is_completed",
        "completed_date",
    )
    list_filter = ("is_completed",)
    search_fields = (
        "house",
        "description",
    )

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
