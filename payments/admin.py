from django.contrib import admin
from .models import Payment, PaymentMethod


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "lease",
        "amount",
        "payment_date",
        "payment_method",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "lease__tenant__user__username",
        "lease__tenant__user__first_name",
        "lease__tenant__user__last_name",
    )
    list_filter = ("payment_date", "created_at", "updated_at")


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "description")
