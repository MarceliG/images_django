from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers
from images_app.models import ImageModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ["id", "name", "image"]
