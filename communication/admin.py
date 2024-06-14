from django.contrib import admin

from .models import Message, Notification


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient", "subject", "sent_at", "read")
    list_filter = ("read",)
    search_fields = ("sender__username", "recipient__username", "subject")

    # disable message editing
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "created_at", "read")
    list_filter = ("read",)
    search_fields = ("user__username", "message")
