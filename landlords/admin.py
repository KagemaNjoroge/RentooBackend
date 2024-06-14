from django.contrib import admin
from .models import Landlord
from properties.models import Property


class PropertyInline(admin.TabularInline):
    model = Property
    extra = 1


@admin.register(Landlord)
class LandlordAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')
    inlines = [PropertyInline]
