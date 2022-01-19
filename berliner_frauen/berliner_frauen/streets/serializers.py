from django.urls import path, include
from .models import District
from rest_framework import routers, serializers


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = District
        fields = ["id", "name", "slug"]
