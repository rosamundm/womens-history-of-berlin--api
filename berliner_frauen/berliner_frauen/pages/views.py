import environ
from django.shortcuts import redirect
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Page
from .serializers import PageSerializer


env = environ.Env()
environ.Env.read_env()


def home(request):
    return redirect(env("LOCAL_API_ROOT"))


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = "slug"
    authentication_class = JWTAuthentication
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
