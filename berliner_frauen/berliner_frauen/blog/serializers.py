from .models import BlogPost
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ("id", "title", "published", "body", "slug",)
        read_only_fields = fields
