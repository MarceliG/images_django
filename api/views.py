<<<<<<< HEAD
from rest_framework.permissions import IsAuthenticated
=======
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User
>>>>>>> 3d1493e46cdb2afa6fd25b33238efb8f30c723a6
from rest_framework import viewsets
from api.serializers import (
    ImageSerializer,
    CustomUserSerializer,
    TierSerializer,
)
from images_app.models import UserImage
from users.models import CustomUser, Tier


<<<<<<< HEAD
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class TierViewSet(viewsets.ModelViewSet):
    queryset = Tier.objects.all()
    serializer_class = TierSerializer
=======
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
>>>>>>> 3d1493e46cdb2afa6fd25b33238efb8f30c723a6


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
<<<<<<< HEAD
            return UserImage.objects.all()
        else:
            return user.user_image.all()

    def perform_create(self, serializer):
        serializer.save(custom_user=self.request.user)
=======
            return ImageModel.objects.all()
        # else:
        #     return user.client.imagemodel.all()

    # def perform_create(self, serializer):
    #     serializer.save(client=self.request.user.client)


# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
>>>>>>> 3d1493e46cdb2afa6fd25b33238efb8f30c723a6
