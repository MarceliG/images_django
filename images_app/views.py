from django.shortcuts import render
from .models import *
from .forms import *


# @allowed_users(allowed_roles=["admin", "basic", "premium", "enterprice"])
def home(request):
    """Home(main) page

    Returns:
        Render html.
    """

    images = ImageModel.objects.all()
    form = ImageForm()
    username = None

    if request.user.is_authenticated:
        if request.method == "POST":
            form = ImageForm(data=request.POST, files=request.FILES)
            form.object.client = request.user
            if form.is_valid():
                form.Client = request.user
                print(request.user)
                form.save()
                return render(
                    request,
                    "home.html",
                    context={"images": images, "form": form},
                )

    context = {
        "images": images,
        "form": form,
        "username": username,
    }
    return render(request, "home.html", context)
