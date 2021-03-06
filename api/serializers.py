from dataclasses import field
from rest_framework import serializers
from images_app.models import Thumbnail, UserImage
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


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = [
            "id",
            "custom_user",
            "name",
            "image",
            "thumbnail",
        ]
        extra_kwargs = {
            "name": {"read_only": True},
            "custom_user": {"read_only": True},
            "thumbnail": {"read_only": True},
        }


class ThubmnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = [
            "id",
            "thumbnail_200px",
            "thumbnail_400px",
        ]
        extra_kwargs = {
            "thumbnail_200px": {"read_only": True},
            "thumbnail_400px": {"read_only": True},
        }
