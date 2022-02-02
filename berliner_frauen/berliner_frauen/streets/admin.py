from tabnanny import verbose
from django.contrib import admin
from .models import Category, District, Person, Street


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "district",
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "street",
        "get_district",
        "core_data_added",
        "entry_complete",
    )

    filter_horizontal = ("category",)

    def get_district(self, obj):
        return obj.street.district
    get_district.short_description = "District"
    get_district.admin_order_field = "street__district"
