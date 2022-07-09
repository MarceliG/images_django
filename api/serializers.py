from dataclasses import field
from email.policy import default
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
            "user",
            "original_image",
            "name",
        ]
        extra_kwargs = {
            "name": {"read_only": True},
            "user": {"read_only": True},
        }


class ThubmnailSerializer(serializers.ModelSerializer):
    size = serializers.IntegerField(default=200)

    class Meta:
        model = Thumbnail
        fields = [
            "id",
            "user",
            "chose_image",
            "thumbnail",
            "name",
            "size",
        ]
        extra_kwargs = {
            "size": {"default": 200},
            "name": {"read_only": True},
            "user": {"read_only": True},
            "thumbnail": {"read_only": True},
        }
