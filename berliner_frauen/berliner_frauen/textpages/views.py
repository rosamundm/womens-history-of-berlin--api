import environ
from django.shortcuts import redirect
from rest_framework import permissions, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import TextPage
from .serializers import TextPageSerializer


env = environ.Env()
environ.Env.read_env()


def home(request):
    return redirect(env("LOCAL_API_ROOT"))


class TextPageViewSet(viewsets.ModelViewSet):
    queryset = TextPage.objects.all()
    serializer_class = TextPageSerializer
    lookup_field = "slug"
    authentication_class = JWTAuthentication
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
