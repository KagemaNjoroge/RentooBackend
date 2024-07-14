from django.contrib import admin
from .models import Tenant, Lease


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "phone_number",
        "created_at",
        "updated_at",
    )
    search_fields = ("first_name", "last_name", "phone_number")
    list_filter = ("created_at", "updated_at")


@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = (
        "tenant",
        "house",
        "start_date",
        "end_date",
        "is_active",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "tenant__user__username",
        "tenant__user__first_name",
        "tenant__user__last_name",
        "house__property__name",
    )
    list_filter = ("is_active", "created_at", "updated_at")

