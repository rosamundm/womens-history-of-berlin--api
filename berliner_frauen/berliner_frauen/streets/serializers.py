from .models import Category, District, Street
from rest_framework import serializers


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ["id", "name", "slug"]

    def to_representation(self, instance):
        return instance.name


class DistrictSerializer(serializers.ModelSerializer):
    streets = StreetSerializer(many=True)
    
    class Meta:
        model = District
        fields = ["id", "name", "slug", "streets"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
