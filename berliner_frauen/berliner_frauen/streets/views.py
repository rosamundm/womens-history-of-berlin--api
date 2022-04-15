from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Category, District, Street
from .serializers import CategorySerializer, DistrictSerializer, StreetSerializer


# for "/"
def index(request):
    return render(request, "streets/index.html")


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all().order_by("name")
    serializer_class = DistrictSerializer
    lookup_field = "slug"
    authentication_class = JWTAuthentication
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    lookup_field = "slug"
    authentication_class = JWTAuthentication
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all().order_by("name")
    serializer_class = StreetSerializer
    lookup_field = "slug"
    authentication_class = JWTAuthentication
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
