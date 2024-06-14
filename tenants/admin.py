from django.contrib import admin
from .models import Tenant, Lease, Payment


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')


@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'house', 'start_date', 'end_date', 'rent_amount', 'is_active', 'created_at', 'updated_at')
    search_fields = (
        'tenant__user__username', 'tenant__user__first_name', 'tenant__user__last_name', 'house__property__name')
    list_filter = ('is_active', 'created_at', 'updated_at')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('lease', 'amount', 'payment_date', 'payment_method', 'created_at', 'updated_at')
    search_fields = (
        'lease__tenant__user__username', 'lease__tenant__user__first_name', 'lease__tenant__user__last_name')
    list_filter = ('payment_date', 'created_at', 'updated_at')
