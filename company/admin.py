from django.contrib import admin
from .models import Company, MailSettings


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "phone")

    def has_add_permission(self, request):
        return Company.objects.count() < 1


@admin.register(MailSettings)
class MailSettingsAdmin(admin.ModelAdmin):
    list_display = ("name", "port", "smtp_server", "is_default")
    search_fields = ("name", "description", "email")
