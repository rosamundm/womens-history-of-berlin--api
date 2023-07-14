import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def api_client():
    user = User.objects.create_user(username="rosamund", password="123abc")
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"JWT {refresh.access_token}")
    return client


@pytest.fixture
def local_api_url():
    return "http://127.0.0.1:8000/api/v1/"

