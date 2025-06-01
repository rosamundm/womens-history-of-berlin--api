from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from django_otp.plugins.otp_totp.models import TOTPDevice

from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from account.models import CustomUser
from blog.views import BlogPostViewSet
from pages.views import PageViewSet
from streets import views as streets_views

"""
django-extensions
run `./manage.py show_urls` to see all patterns
"""


class CustomOTPAdmin(OTPAdminSite):
    pass


# OTP
custom_admin = OTPAdminSite("CustomOTPAdmin")
custom_admin.register(CustomUser)
custom_admin.register(TOTPDevice, TOTPDeviceAdmin)

if CustomUser not in custom_admin._registry:
    custom_admin.register(CustomUser)

if TOTPDevice not in custom_admin._registry:
    custom_admin.register(TOTPDevice, TOTPDeviceAdmin)

# register other models from default admin to custom admin
for model_cls, model_admin in custom_admin._registry.items():
    if model_cls not in custom_admin._registry:
        custom_admin.register(model_cls, model_admin.__class__)

# API routes
router = routers.DefaultRouter()
router.register(r"districts", streets_views.DistrictViewSet)
router.register(r"streets", streets_views.StreetViewSet)
router.register(r"tags", streets_views.TagViewSet)

router.register(r"blog", BlogPostViewSet)
router.register(r"pages", PageViewSet)

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
    # admin
    path("admin/", custom_admin.urls),  # not django.contrib.admin.site.urls
    path("tinymce/", include("tinymce.urls")),

    # API
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)