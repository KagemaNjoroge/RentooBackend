from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group


admin.site.unregister([Group])


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number")
    search_fields = (
        "username",
        "email",
    )
    list_filter = ("is_staff",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                )
            },
        ),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "phone_number", "profile_picture")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
    ordering = ("username",)
    filter_horizontal = ("groups", "user_permissions")
