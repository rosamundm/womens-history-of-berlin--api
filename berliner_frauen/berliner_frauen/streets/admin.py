from django.contrib import admin
from .models import District, Street


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "entries_completed",
        "entries_with_photos_taken",
        "complete_from_available_photos",
    )

    def entries_completed(self, obj):
        try:
            divided = (
                obj.number_of_completed_streets / obj.number_of_added_streets
            )
            percentage = divided * 100
            percentage = round(percentage, 2)
            return f"{percentage}%"
        except ZeroDivisionError:
            return "Unknown"

    def entries_with_photos_taken(self, obj):
        try:
            divided = (
                obj.number_of_photos_taken / obj.number_of_added_streets
            )
            percentage = divided * 100
            percentage = round(percentage, 2)
            return f"{percentage}%"
        except ZeroDivisionError:
            return "Unknown"

    def complete_from_available_photos(self, obj):
        try:
            divided = (
                obj.number_of_completed_streets / obj.number_of_photos_taken
            )
            percentage = divided * 100
            percentage = round(percentage, 2)
            return f"{percentage}%"
        except ZeroDivisionError:
            return "Unknown"


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "district",
        "eponym_name",
        "eponym_core_data_added",
        "entry_complete",
        "image_available",
        "tag_list",
        "last_edited",
    )

    list_filter = ("district", "entry_complete", "image_available")

    ordering = ("name",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return u", ".join(tag.name for tag in obj.tags.all())
