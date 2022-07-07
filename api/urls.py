from django.urls import path, include
from api.views import (
    ImageViewSet,
    CustomUserViewSet,
    TierViewSet,
    ThumbnailViewSet,
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"users", CustomUserViewSet, "custom_user")
router.register(r"tier", TierViewSet, "tier")
router.register(r"thumbnail", ThumbnailViewSet, "thumbnail")
router.register(r"images", ImageViewSet, "images")


urlpatterns = [
    path("", include(router.urls)),
    path(
        "api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
]
