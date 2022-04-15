from .models import Category, District, Street
from rest_framework import serializers


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = District
        fields = ["id", "name", "slug", "streets"]

    def to_representation(self, instance):
        representation = dict()
        representation["streets"] = instance.streets


class StreetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Street
        fields = ["id", "name", "slug"]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
