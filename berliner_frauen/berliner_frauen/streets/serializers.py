from .models import Category, District, Person, Street
from rest_framework import serializers


class StreetSerializer(serializers.ModelSerializer):
    district = serializers.SerializerMethodField()
    eponym = serializers.SerializerMethodField()

    class Meta:
        model = Street
        fields = ["id", "name", "district", "eponym", "slug"]
        read_only_fields = fields

    def get_district(self, obj):
        return obj.district.name

    def get_eponym(self, obj):
        return obj.eponym.name


class DistrictSerializer(serializers.ModelSerializer):
    streets = StreetSerializer(many=True).data

    class Meta:
        model = District
        fields = ["id", "name", "slug", "streets"]


class PersonSerializer(serializers.ModelSerializer):
    street = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
            "street",
            "category",
            "date_of_birth",
            "date_of_death",
            "place_of_birth",
            "place_of_death",
            "description",
        ]

    def get_street(self, obj):
        return obj.street.name


class CategorySerializer(serializers.ModelSerializer):
    people = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "people"]
        read_only_fields = fields

    def get_people(self, obj):
        return obj.people.all()
