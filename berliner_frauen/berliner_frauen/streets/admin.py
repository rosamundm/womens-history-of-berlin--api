from django.contrib import admin
from .models import Category, District, Person, Street


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "eponym",
        "district",
        "slug",
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "street",
        "get_district",
        "core_data_added",
        "entry_complete",
        "slug",
    )

    def get_district(self, obj):
        return obj.street.district

    filter_horizontal = ("category",)

    get_district.short_description = "District"
    get_district.admin_order_field = "street__district"
