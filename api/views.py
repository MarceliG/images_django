from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from api.serializers import (
    ImageSerializer,
    CustomUserSerializer,
    TierSerializer,
    ThubmnailSerializer,
)
from images_app.models import Thumbnail, UserImage
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
            return UserImage.objects.prefetch_related("thumbnails").all()
        else:
            return user.user_image.prefetch_related("thumbnails").all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class ThumbnailViewSet(viewsets.ModelViewSet):
    serializer_class = ThubmnailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Thumbnail.objects.all()
        else:
            return user.thumbnails.all()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            thumbnail=self.request.user,
        )
