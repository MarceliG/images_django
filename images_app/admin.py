from django.contrib import admin
from .models import *

# admin.site.register(ImageModel)


@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    readonly_fields = ("thumbnail_200px", "thumbnail_400px")
