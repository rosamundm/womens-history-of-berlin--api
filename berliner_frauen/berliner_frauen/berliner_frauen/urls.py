from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from streets import views as streets_views
from textpages import views as textpage_views


router = routers.DefaultRouter()
router.register(r"districts", streets_views.DistrictViewSet)
router.register(r"streets", streets_views.StreetViewSet)
router.register(r"textpages", textpage_views.TextPageViewSet)

district_router = routers.NestedSimpleRouter(
    router,
    r"districts",
    lookup="district"
)
district_router.register(
    "streets",
    streets_views.StreetViewSet,
    basename="streets"
)

urlpatterns = [
    path("", textpage_views.home, name="home"),

    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),

    path("api/v1/", include(router.urls)),
    path("api/v1/", include(district_router.urls)),
    path(
        "api/v1/token-auth/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        "api/v1/token-refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path(
        "api/v1/token-verify/",
        TokenVerifyView.as_view(),
        name="token_verify"
    ),

    path("tinymce/", include("tinymce.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
