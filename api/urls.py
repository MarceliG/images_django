from django.urls import path, include
from api.views import ImageViewSet, CustomUserViewSet, TierViewSet
from rest_framework import routers


router = routers.DefaultRouter()
<<<<<<< HEAD
router.register(r"users", CustomUserViewSet, "custom_user")
router.register(r"tier", TierViewSet, "tier")
router.register(r"images", ImageViewSet, "images")
=======
# router.register(r"users", UserViewSet)
router.register(r"images", ImageViewSet, "images")
# router.register(r"clients", ClientViewSet, 'clients')
>>>>>>> 3d1493e46cdb2afa6fd25b33238efb8f30c723a6


urlpatterns = [
    path("", include(router.urls)),
    path(
        "api-auth/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
]
