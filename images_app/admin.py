from django.contrib import admin
from .models import *


# admin.site.register(Client)


@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    readonly_fields = ("name", "thumbnail_200px", "thumbnail_400px")
