from rest_framework import filters, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import District, Street
from .serializers import DistrictSerializer, StreetSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all().order_by("name")
    serializer_class = DistrictSerializer
    lookup_field = "district_slug"
    authentication_class = JWTAuthentication
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    search_fields = ("name",)
    filter_backends = (filters.SearchFilter,)

    def create(self, request):
        return Response(
            {"message": "POST operation not possible via API"},
            status=status.HTTP_403_FORBIDDEN
        )

    def update(self, request, district_slug=None):
        return Response(
            {"message": "PUT operation not possible via API"},
            status=status.HTTP_403_FORBIDDEN
        )

    def partial_update(self, request, district_slug=None):
        return Response(
            {"message": "PATCH operation not possible via API"},
            status=status.HTTP_403_FORBIDDEN
        )

    def destroy(self, request, district_slug=None):
        return Response(
            {"message": "DELETE operation not possible via API"},
            status=status.HTTP_403_FORBIDDEN
        )


class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all().filter(entry_complete=True).order_by("name")
    serializer_class = StreetSerializer
    lookup_field = "street_slug"
    authentication_class = JWTAuthentication
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    search_fields = ("name", "eponym_name",)
    filter_backends = (filters.SearchFilter,)

    def create(self, request):
        return Response(
            {"message": "POST operation not possible via API"},
            status=status.HTTP_403_FORBIDDEN
        )

    def update(self, request, street_slug=None):
        return Response(
            {"message": "PUT operation not possible via API"},
            status=status.HTTP_403_FORBIDDEN
        )

    def partial_update(self, request, street_slug=None):
        return Response(
            {"message": "PATCH operation not possible via API"},
            status=status.HTTP_403_FORBIDDEN
        )

    def destroy(self, request, street_slug=None):
        return Response(
            {"message": "DELETE operation not possible via API"},
            status=status.HTTP_403_FORBIDDEN
        )
