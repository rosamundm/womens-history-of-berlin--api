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

    def get_percentage(self, dividend: int, divisor: int) -> float | None:
        try:
            divided = dividend / divisor
            return round(divided * 100, 2)
        except ZeroDivisionError:
            return None

    def entries_completed(self, obj: District) -> str:
        if isinstance((percentage := self.get_percentage(
            obj.number_of_completed_streets, obj.number_of_added_streets
        )), float):
            return f"{percentage}%"
        return "Unknown"

    def entries_with_photos_taken(self, obj: District) -> str:
        if isinstance((percentage := self.get_percentage(
            obj.number_of_photos_taken, obj.number_of_added_streets
        )), float):
            return f"{percentage}%"
        return "Unknown"

    def complete_from_available_photos(self, obj: District) -> str:
        if isinstance((percentage := self.get_percentage(
            obj.number_of_completed_streets, obj.number_of_photos_taken
        )), float):
            return f"{percentage}%"
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

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields[
            "map_link"
        ].help_text = "If using a Google Maps link, omit surplus text after coordinates"
        return form

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())
