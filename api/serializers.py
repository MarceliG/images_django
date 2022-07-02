from urllib import request
from django.contrib.auth.models import User
from rest_framework import serializers
from images_app.models import ImageModel


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "email"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = [
            "id",
            # "client",
            "name",
            "image",
            "thumbnail_200px",
            "thumbnail_400px",
        ]
        extra_kwargs = {
            "name": {"read_only": True},
            "client": {"read_only": True},
            "thumbnail_200px": {"read_only": True},
            "thumbnail_400px": {"read_only": True},
        }


# class ClientSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source="user.username")
#     grup = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

#     class Meta:
#         model = Client
#         fields = ["id", "user", "grup"]
