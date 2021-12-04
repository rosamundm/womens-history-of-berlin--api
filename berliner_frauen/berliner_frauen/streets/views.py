from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import District
from .serializers import DistrictSerializer


def index(request):
    return render(request, "streets/index.html")

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all().order_by("name")
    serializer_class = DistrictSerializer
    authentication_class = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]