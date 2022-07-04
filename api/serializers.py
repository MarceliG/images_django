from dataclasses import field
from rest_framework import serializers
<<<<<<< HEAD
from images_app.models import UserImage
from users.models import CustomUser, Tier


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "tier", "is_staff", "is_active"]

        extra_kwargs = {
            "username": {"read_only": True},
            "tier": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
        }


class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = ["id", "tier"]

        extra_kwargs = {
            "tier": {"read_only": True},
        }
=======
from images_app.models import ImageModel


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "email"]
>>>>>>> 3d1493e46cdb2afa6fd25b33238efb8f30c723a6


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = [
            "id",
<<<<<<< HEAD
            "custom_user",
=======
            # "client",
>>>>>>> 3d1493e46cdb2afa6fd25b33238efb8f30c723a6
            "name",
            "image",
            "thumbnail_200px",
            "thumbnail_400px",
        ]
        extra_kwargs = {
            "name": {"read_only": True},
            "custom_user": {"read_only": True},
            "thumbnail_200px": {"read_only": True},
            "thumbnail_400px": {"read_only": True},
        }


# class ClientSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source="user.username")
#     grup = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

#     class Meta:
#         model = Client
#         fields = ["id", "user", "grup"]
