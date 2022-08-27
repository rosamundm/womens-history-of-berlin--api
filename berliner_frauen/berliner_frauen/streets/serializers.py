from .models import District, Street
from rest_framework import serializers


class DistrictSerializer(serializers.ModelSerializer):
    streets = serializers.SerializerMethodField()

    class Meta:
        model = District
        fields = ["id", "name", "district_slug", "streets"]
        read_only_fields = fields

    def get_streets(self, obj):
        return obj.streets.all().values("id", "name", "street_slug")


class StreetSerializer(serializers.ModelSerializer):
    district = serializers.SerializerMethodField()
    district_slug = serializers.SerializerMethodField()

    class Meta:
        model = Street
        fields = [
            "id",
            "name",
            "district",
            "district_slug",
            "street_slug",
            "map_link",
            "eponym_name",
            "eponym_date_of_birth",
            "eponym_date_of_death",
            "eponym_place_of_birth",
            "eponym_place_of_death",
            "eponym_description",
            "image",
        ]
        read_only_fields = fields

    def get_district(self, obj):
        return obj.district.name

    def get_district_slug(self, obj):
        return obj.district.district_slug
