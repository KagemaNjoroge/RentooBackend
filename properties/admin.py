from django.contrib import admin
from .models import Property, House, PropertyPhoto, HousePhoto

admin.site.site_header = 'Rentoo Property Management System'
admin.site.site_title = 'Rentoo PMS'
admin.site.index_title = 'Welcome to Rentoo PMS'


class PropertyPhotoInline(admin.TabularInline):
    model = PropertyPhoto
    extra = 1


class HousePhotoInline(admin.TabularInline):
    model = HousePhoto
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_at', 'updated_at')
    search_fields = ('name', 'address')
    list_filter = ('created_at', 'updated_at')
    inlines = [PropertyPhotoInline]


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('property', 'house_number', 'number_of_rooms', 'is_occupied', 'rent', 'created_at', 'updated_at')
    search_fields = ('property__name', 'house_number')
    list_filter = ('is_occupied', 'created_at', 'updated_at')
    inlines = [HousePhotoInline]


@admin.register(PropertyPhoto)
class PropertyPhotoAdmin(admin.ModelAdmin):
    list_display = ('property', 'image', 'caption', 'uploaded_at')
    search_fields = ('property__name', 'caption')
    list_filter = ('uploaded_at',)


@admin.register(HousePhoto)
class HousePhotoAdmin(admin.ModelAdmin):
    list_display = ('house', 'image', 'caption', 'uploaded_at')
    search_fields = ('house__house_number', 'caption')
    list_filter = ('uploaded_at',)
