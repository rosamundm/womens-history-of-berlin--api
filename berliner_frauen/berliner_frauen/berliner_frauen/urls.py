from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from streets import views as streets_views
from blog import views as blog_views

"""
django-extensions
run `./manage.py show_urls` to see all patterns
"""

router = routers.DefaultRouter()
router.register(r"districts", streets_views.DistrictViewSet)
router.register(r"streets", streets_views.StreetViewSet)
router.register(r"tags", streets_views.TagViewSet)
router.register(r"blog", blog_views.BlogPostViewSet)

district_router = routers.NestedSimpleRouter(router, r"districts", lookup="district")
district_router.register("streets", streets_views.StreetViewSet, basename="streets")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/", include(router.urls)),
    path("api/v1/", include(district_router.urls)),
    path("api/v1/token-auth/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token-refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/token-verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("tinymce/", include("tinymce.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
