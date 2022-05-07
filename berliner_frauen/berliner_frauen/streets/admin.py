from django.contrib import admin
from .models import District, Street


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "added_street_count",
    )

    def added_street_count(self, obj):
        return obj.streets.count()


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "district",
        "eponym_name",
        "eponym_core_data_added",
        "entry_complete"
    )
