from .models import Category, District, Street
from rest_framework import serializers


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ["id", "name", "slug"]


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ["id", "name", "slug", "get_streets"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
