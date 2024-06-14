from django.contrib import admin
from .models import Agent
from properties.models import Property


class PropertyInline(admin.TabularInline):
    model = Property
    extra = 1


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')

    inlines = [PropertyInline]
