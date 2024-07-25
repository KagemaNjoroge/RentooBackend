from django.contrib import admin
from .models import TemporaryFile


@admin.register(TemporaryFile)
class TemporaryFileAdmin(admin.ModelAdmin):
    list_display = ("created_at",)
