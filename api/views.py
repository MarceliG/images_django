from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from api.serializers import (
    ImageSerializer,
    CustomUserSerializer,
    TierSerializer,
)
from images_app.models import UserImage
from users.models import CustomUser, Tier


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class TierViewSet(viewsets.ModelViewSet):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return UserImage.objects.all()
        else:
            return user.user_image.all()

    def perform_create(self, serializer):
        serializer.save(custom_user=self.request.user)
