from django.http import HttpResponse
from django.shortcuts import render, redirect
from members.views import login_user
from .models import *
from .forms import *
from .decorators import unathenticated_user, admin_only, allowed_users
from django.core.files.storage import FileSystemStorage


# @allowed_users(allowed_roles=["admin", "basic", "premium", "enterprice"])
def home(request):
    """Home(main) page

    Returns:
        Render html.
    """

    images = ImageModel.objects.all()
    user = request.user
    form = ImageForm(instance=user)
    context = {
        "images": images,
        "form": form,
    }
    return render(request, "home.html", context)
