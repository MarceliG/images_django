from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *
from images_app.models import *


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ImageModel.objects.all()
        # else:
        #     return user.client.imagemodel.all()

    # def perform_create(self, serializer):
    #     serializer.save(client=self.request.user.client)


# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
