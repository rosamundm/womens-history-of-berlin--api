import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory


@pytest.fixture
def api_request():
    return APIRequestFactory()


@pytest.fixture
def api_url():
    return "http://127.0.0.1:8000/api/v1/"


@pytest.fixture
def api_user():
    return User.objects.create(username="rosamund", password="123abc")
