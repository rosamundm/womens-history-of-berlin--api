from django.db.models import Q
from django.utils import timezone
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.filter(
        Q(ready_to_publish=True) & Q(published__lte=timezone.now())
    ).order_by("-published")
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    authentication_class = JWTAuthentication
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
