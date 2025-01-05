from .models import Page
from rest_framework import serializers


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ["id", "title", "body", "slug"]
        read_only_fields = fields