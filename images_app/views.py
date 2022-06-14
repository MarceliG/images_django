from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

from members.views import login_user
from .serializers import UserSerializer
from .models import *
from .decorators import unathenticated_user, admin_only, allowed_users


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @allowed_users(allowed_roles=["admin", "basic", "premium", "enterprice"])
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
