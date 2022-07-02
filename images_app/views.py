from django.shortcuts import render
from images_app.models import UserImage
from images_app.forms import ImageForm


# @allowed_users(allowed_roles=["admin", "basic", "premium", "enterprice"])
def home(request):
    """Home(main) page

    Returns:
        Render html.
    """

    images = []
    form = ImageForm()
    user = request.user
    if request.user.is_authenticated:
        if user.is_staff:
            images = UserImage.objects.all()
        # else:
        # images = user.client.imagemodel.all()

        if request.method == "POST":
            form = ImageForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                # form.Client = request.user
                form.save()
                return render(
                    request,
                    "home.html",
                    context={"images": images, "form": form},
                )

    context = {
        "images": images,
        "form": form,
    }
    return render(request, "home.html", context)
