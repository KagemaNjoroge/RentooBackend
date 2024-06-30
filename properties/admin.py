from django.contrib import admin

from .models import Property, House, EntityPhoto, Unit

admin.site.site_header = "Rentoo Property Management System"
admin.site.site_title = "Rentoo PMS"
admin.site.index_title = "Welcome to Rentoo PMS"


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "created_at", "updated_at")
    search_fields = ("name", "address")
    list_filter = ("created_at", "updated_at")


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = (
        "property",
        "house_number",
        "number_of_rooms",
        "is_occupied",
        "rent",
        "created_at",
        "updated_at",
    )
    search_fields = ("property__name", "house_number")
    list_filter = ("is_occupied", "created_at", "updated_at")


@admin.register(EntityPhoto)
class PropertyPhotoAdmin(admin.ModelAdmin):
    list_display = ("image", "caption", "uploaded_at")
    search_fields = ("caption",)
    list_filter = ("uploaded_at",)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("unit_name", "property")
