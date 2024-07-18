from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')

    def has_add_permission(self, request):
        return Company.objects.count() < 1
