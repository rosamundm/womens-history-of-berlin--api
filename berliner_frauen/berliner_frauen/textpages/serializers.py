from .models import TextPage
from rest_framework import serializers


class TextPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPage
        fields = ["id", "title", "body", "slug"]
        read_only_fields = fields
