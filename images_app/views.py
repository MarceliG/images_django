from django.http import HttpResponse
from django.shortcuts import render

from members.views import login_user
from .models import *
from .decorators import unathenticated_user, admin_only, allowed_users


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
