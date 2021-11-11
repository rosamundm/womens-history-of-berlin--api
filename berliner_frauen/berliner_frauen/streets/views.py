from django.shortcuts import render
from rest_framework import viewsets
from .models import District
from .serializers import DistrictSerializer


def index(request):
    return render(request, "streets/index.html")

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all().order_by("name")
    serializer_class = DistrictSerializer
    # permission_classes = [permissions.IsAuthenticated]