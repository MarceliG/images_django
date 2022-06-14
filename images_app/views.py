from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def home(request):
    """Home(main) page

    Returns:
        Render html.
    """
    images = Image.objects.all()
    context = {
        "images": images,
    }
    return render(request, "home.html", context)
