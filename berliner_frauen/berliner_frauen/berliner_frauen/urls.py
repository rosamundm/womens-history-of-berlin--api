from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from streets.views import DistrictViewSet, PersonViewSet, StreetViewSet


router = routers.DefaultRouter()
# router.register(r"categories", CategoryViewSet)
router.register(r"districts", DistrictViewSet)
router.register(r"people", PersonViewSet)
router.register(r"streets", StreetViewSet)

district_router = routers.NestedSimpleRouter(router, r"districts", lookup="district")
district_router.register("streets", StreetViewSet, basename="streets")
district_router.register("person", PersonViewSet, basename="person")
# district_router.register("category", CategoryViewSet, basename="category")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("streets.urls")),
    path("api/v1/", include(router.urls)),
    path("api/v1/", include(district_router.urls)),
    path("api/v1/token-auth/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token-refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token-verify/", TokenVerifyView.as_view(), name="token_verify"),
]
