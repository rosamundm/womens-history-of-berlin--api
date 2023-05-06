from django.contrib import admin
from .models import District, Street


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "number_of_added_streets",
        "number_of_completed_streets",
    )


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "district",
        "eponym_name",
        "eponym_core_data_added",
        "entry_complete",
        "image_available",
    )

    ordering = ("name",)
